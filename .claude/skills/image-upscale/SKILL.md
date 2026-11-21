---
name: "image-upscale"
description: "Upscale MOE's flyers, graphics or photos 4x (or 2x) with Real-ESRGAN run locally in code, no Higgsfield credits. Use when he asks to upscale, sharpen, clean up or enlarge an image."
---

# Image upscale (local Real-ESRGAN, no credits)

Upscale an image 4x with Real-ESRGAN running locally through onnxruntime. No Higgsfield credits, no cost quote needed. Never use Higgsfield upscale_image unless MOE explicitly asks for it.

## Why it is built this way
- PyTorch can NOT be installed in the workspace: download.pytorch.org is blocked and the PyPI torch wheel (CUDA deps) times out. Do not try again.
- Instead: download the .pth weights from GitHub, convert them to ONNX with the torch-free converter below (parses the .pth zip/pickle directly), and run with onnxruntime (already installed). Only `onnx` needs pip installing.

## Model choice
- Flyers, posters, illustrations, text-heavy graphics (default): RealESRGAN_x4plus_anime_6B (18 MB, fast, ~2 min for a 1080x1350 flyer on 2 CPUs)
  https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth
- Real photos (skin, fabric, product packshots): RealESRGAN_x4plus (64 MB, 23 blocks, ~4x slower, more natural texture)
  https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
The converter reads the block count from the weights, so both work unchanged.

## Steps
1. Setup (skip any step already done in this session):
   ```bash
   mkdir -p ~/upscale/models && cd ~/upscale
   pip install --break-system-packages -q onnx
   curl -sSfL -o models/anime6B.pth https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth
   ```
   Write `esrgan_onnx.py` and `upscale.py` (below) with the Write tool, then:
   ```bash
   python3 esrgan_onnx.py models/anime6B.pth models/anime6B.onnx
   ```
2. Copy the source image to the working dir (uploads are read-only). Prefer a lossless PNG of the final design if one exists in the session.
3. Test a small crop first (~240x200) and view a before/after side by side to confirm quality.
4. Run the full image: `python3 upscale.py models/anime6B.onnx in.png out_4x.png` (run with a long timeout; prints per-tile progress).
5. Check: build a zoomed sheet of 3-4 crops (headline, small text, a detailed illustration, phone number/contact) and look at it before sending.
6. Export: `Image.open('out_4x.png').save('<Name>_4K.jpg', quality=95, subsampling=0)`. If he wants 2x instead, resize the 4x result down by half with Image.LANCZOS before saving.
7. Send with SendUserFile (display render). Tell him the new size and that no credits were used, in one or two lines. Note that faint paper grain/texture gets slightly smoothed.

## esrgan_onnx.py
```python
"""Load a Real-ESRGAN RRDBNet .pth without torch and export it as ONNX."""
import sys, zipfile, pickle, collections
import numpy as np
import onnx
from onnx import helper, TensorProto, numpy_helper

PTH, OUT = sys.argv[1], sys.argv[2]

zf = zipfile.ZipFile(PTH)
names = zf.namelist()
root = names[0].split('/')[0]
pkl = [n for n in names if n.endswith('data.pkl')][0]

DT = {'FloatStorage': np.float32, 'HalfStorage': np.float16, 'DoubleStorage': np.float64,
      'LongStorage': np.int64, 'IntStorage': np.int32}

class StorageType:
    def __init__(self, name): self.name = name

def rebuild_tensor(storage, offset, size, stride, *args):
    dtype, key = storage
    raw = np.frombuffer(zf.read(f'{root}/data/{key}'), dtype=dtype)
    if len(size) == 0:
        return raw[offset].copy()
    itemsize = raw.itemsize
    arr = np.lib.stride_tricks.as_strided(raw[offset:], shape=tuple(size),
                                          strides=tuple(s * itemsize for s in stride))
    return np.ascontiguousarray(arr).astype(np.float32)

class U(pickle.Unpickler):
    def find_class(self, mod, name):
        if mod == 'torch._utils' and name.startswith('_rebuild_tensor'):
            return rebuild_tensor
        if mod == 'torch' and name.endswith('Storage'):
            return StorageType(name)
        if mod == 'collections' and name == 'OrderedDict':
            return collections.OrderedDict
        if mod == 'torch._utils' and name == '_rebuild_parameter':
            return lambda data, *a: data
        return super().find_class(mod, name)
    def persistent_load(self, pid):
        st, key = pid[1], pid[2]
        return (DT[st.name], key)

sd = U(zf.open(pkl)).load()
if 'params_ema' in sd: sd = sd['params_ema']
elif 'params' in sd: sd = sd['params']
nblocks = 1 + max(int(k.split('.')[1]) for k in sd if k.startswith('body.'))
print('blocks', nblocks, 'keys', len(sd))

nodes, inits = [], []
cnt = [0]
def nm(p): cnt[0] += 1; return f'{p}_{cnt[0]}'
def const(arr, p='c'):
    n = nm(p); inits.append(numpy_helper.from_array(np.asarray(arr, np.float32), n)); return n
def conv(x, key):
    w = const(sd[key + '.weight'], 'w'); b = const(sd[key + '.bias'], 'b'); o = nm('conv')
    nodes.append(helper.make_node('Conv', [x, w, b], [o], pads=[1, 1, 1, 1], kernel_shape=[3, 3])); return o
def lrelu(x):
    o = nm('lr'); nodes.append(helper.make_node('LeakyRelu', [x], [o], alpha=0.2)); return o
def cat(xs):
    o = nm('cat'); nodes.append(helper.make_node('Concat', xs, [o], axis=1)); return o
def add(a, b):
    o = nm('add'); nodes.append(helper.make_node('Add', [a, b], [o])); return o
def mul(a, s):
    o = nm('mul'); nodes.append(helper.make_node('Mul', [a, const(np.array(s, np.float32))], [o])); return o
scales2 = None
def up2(x):
    global scales2
    if scales2 is None: scales2 = const(np.array([1, 1, 2, 2], np.float32), 'sc')
    o = nm('up'); nodes.append(helper.make_node('Resize', [x, '', scales2], [o], mode='nearest')); return o

def rdb(x, p):
    x1 = lrelu(conv(x, p + '.conv1'))
    x2 = lrelu(conv(cat([x, x1]), p + '.conv2'))
    x3 = lrelu(conv(cat([x, x1, x2]), p + '.conv3'))
    x4 = lrelu(conv(cat([x, x1, x2, x3]), p + '.conv4'))
    x5 = conv(cat([x, x1, x2, x3, x4]), p + '.conv5')
    return add(mul(x5, 0.2), x)

feat = conv('input', 'conv_first')
h = feat
for i in range(nblocks):
    o = rdb(rdb(rdb(h, f'body.{i}.rdb1'), f'body.{i}.rdb2'), f'body.{i}.rdb3')
    h = add(mul(o, 0.2), h)
feat = add(feat, conv(h, 'conv_body'))
feat = lrelu(conv(up2(feat), 'conv_up1'))
feat = lrelu(conv(up2(feat), 'conv_up2'))
out = conv(lrelu(conv(feat, 'conv_hr')), 'conv_last')
nodes.append(helper.make_node('Identity', [out], ['output']))

g = helper.make_graph(nodes, 'rrdb',
                      [helper.make_tensor_value_info('input', TensorProto.FLOAT, [1, 3, 'H', 'W'])],
                      [helper.make_tensor_value_info('output', TensorProto.FLOAT, [1, 3, 'H4', 'W4'])],
                      inits)
# ir_version=8: the installed onnxruntime rejects newer IR versions
m = helper.make_model(g, opset_imports=[helper.make_opsetid('', 13)], ir_version=8)
onnx.checker.check_model(m)
onnx.save(m, OUT)
print('saved', OUT)
```

## upscale.py
```python
import sys, time
import numpy as np
import onnxruntime as ort
from PIL import Image

MODEL, SRC, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
TILE, PAD, S = 192, 16, 4

opts = ort.SessionOptions(); opts.intra_op_num_threads = 2
sess = ort.InferenceSession(MODEL, opts, providers=['CPUExecutionProvider'])
img = np.asarray(Image.open(SRC).convert('RGB')).astype(np.float32) / 255.0
H, W, _ = img.shape
out = np.zeros((H * S, W * S, 3), np.float32)
t0 = time.time()
ys = list(range(0, H, TILE)); xs = list(range(0, W, TILE))
n = 0
for y in ys:
    for x in xs:
        y0, y1 = max(y - PAD, 0), min(y + TILE + PAD, H)
        x0, x1 = max(x - PAD, 0), min(x + TILE + PAD, W)
        tile = img[y0:y1, x0:x1].transpose(2, 0, 1)[None]
        r = sess.run(None, {'input': tile})[0][0].transpose(1, 2, 0)
        ty, tx = (y - y0) * S, (x - x0) * S
        hh, ww = (min(y + TILE, H) - y) * S, (min(x + TILE, W) - x) * S
        out[y * S:y * S + hh, x * S:x * S + ww] = r[ty:ty + hh, tx:tx + ww]
        n += 1
        print(f'tile {n}/{len(ys)*len(xs)}  {time.time()-t0:.0f}s', flush=True)
Image.fromarray((np.clip(out, 0, 1) * 255 + 0.5).astype(np.uint8)).save(OUT)
print('done', out.shape, f'{time.time()-t0:.0f}s')
```

## Notes
- Images with transparency: upscale RGB as above, upscale the alpha channel separately with Image.LANCZOS 4x and re-attach.
- Very large inputs (over ~2500 px on a side): the 4x result gets huge; offer 2x instead or upscale once and downsize.