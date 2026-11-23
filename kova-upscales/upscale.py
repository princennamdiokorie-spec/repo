"""4x AI upscale with Real-ESRGAN realesr-general-x4v3, without PyTorch.

Reads the .pth weights directly (zip + pickle), builds the SRVGGNetCompact
network as an ONNX graph, runs it with onnxruntime in overlapping tiles, then
resizes to the requested final size with Lanczos.

Usage: python3 upscale.py <weights.pth> <in.png> <out.png> <width> <height>
"""
import pickle
import sys
import zipfile

import numpy as np
import onnx
import onnxruntime as ort
from onnx import TensorProto, helper, numpy_helper
from PIL import Image

DTYPES = {'FloatStorage': np.float32, 'HalfStorage': np.float16}


def load_pth(path):
    zf = zipfile.ZipFile(path)
    root = zf.namelist()[0].split('/')[0]

    class Storage:
        def __init__(self, name): self.name = name

    class U(pickle.Unpickler):
        def find_class(self, mod, name):
            if mod == 'torch._utils' and name == '_rebuild_tensor_v2':
                def rebuild(storage, offset, size, stride, *a):
                    dtype, key = storage
                    buf = np.frombuffer(zf.read(f'{root}/data/{key}'), dtype=dtype)
                    n = int(np.prod(size)) if size else 1
                    arr = buf[offset:offset + n] if all(s == 0 for s in []) else None
                    full = np.lib.stride_tricks.as_strided(buf[offset:], shape=size,
                                                           strides=[s * buf.itemsize for s in stride])
                    return np.array(full, dtype=np.float32)
                return rebuild
            if mod == 'torch' and name in DTYPES:
                return Storage(name)
            if mod == 'collections' and name == 'OrderedDict':
                import collections
                return collections.OrderedDict
            return super().find_class(mod, name)

        def persistent_load(self, pid):
            _, stype, key, _, _ = pid
            return (DTYPES[stype.name], key)

    sd = U(zf.open(f'{root}/data.pkl')).load()
    return sd.get('params', sd.get('params_ema', sd))


def build(sd):
    convs = sorted({int(k.split('.')[1]) for k in sd if k.endswith('.bias')})
    nodes, inits = [], []
    cur = 'x'
    for i in convs:
        w, b = f'w{i}', f'b{i}'
        inits += [numpy_helper.from_array(sd[f'body.{i}.weight'], w), numpy_helper.from_array(sd[f'body.{i}.bias'], b)]
        nodes.append(helper.make_node('Conv', [cur, w, b], [f'c{i}'], pads=[1, 1, 1, 1]))
        cur = f'c{i}'
        pk = f'body.{i + 1}.weight'
        if pk in sd:                                     # PReLU after every conv but the last
            s = f's{i}'
            inits.append(numpy_helper.from_array(sd[pk].reshape(-1, 1, 1), s))
            nodes.append(helper.make_node('PRelu', [cur, s], [f'p{i}']))
            cur = f'p{i}'
    nodes.append(helper.make_node('DepthToSpace', [cur], ['ps'], blocksize=4, mode='CRD'))
    inits.append(numpy_helper.from_array(np.array([1, 1, 4, 4], np.float32), 'sc'))
    nodes.append(helper.make_node('Resize', ['x', '', 'sc'], ['up'], mode='nearest'))
    nodes.append(helper.make_node('Add', ['ps', 'up'], ['y']))
    g = helper.make_graph(nodes, 'srvgg', [helper.make_tensor_value_info('x', TensorProto.FLOAT, [1, 3, None, None])],
                          [helper.make_tensor_value_info('y', TensorProto.FLOAT, [1, 3, None, None])], inits)
    m = helper.make_model(g, opset_imports=[helper.make_opsetid('', 17)]); m.ir_version = 8
    return m.SerializeToString()


def upscale(sess, img, tile=256, pad=12):
    h, w, _ = img.shape
    out = np.zeros((h * 4, w * 4, 3), np.float32)
    for y in range(0, h, tile):
        for x in range(0, w, tile):
            y0, x0 = max(y - pad, 0), max(x - pad, 0)
            y1, x1 = min(y + tile + pad, h), min(x + tile + pad, w)
            t = img[y0:y1, x0:x1].transpose(2, 0, 1)[None]
            r = sess.run(None, {'x': t})[0][0].transpose(1, 2, 0)
            yy, xx = (y - y0) * 4, (x - x0) * 4
            th, tw = min(tile, h - y) * 4, min(tile, w - x) * 4
            out[y * 4:y * 4 + th, x * 4:x * 4 + tw] = r[yy:yy + th, xx:xx + tw]
    return out


if __name__ == '__main__':
    wpath, src, dst, W, H = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
    sess = ort.InferenceSession(build(load_pth(wpath)), providers=['CPUExecutionProvider'])
    img = np.asarray(Image.open(src).convert('RGB')).astype(np.float32) / 255
    big = (upscale(sess, img).clip(0, 1) * 255).round().astype(np.uint8)
    Image.fromarray(big).resize((W, H), Image.LANCZOS).save(dst)
    print(src, img.shape[1::-1], '->', (W, H))
