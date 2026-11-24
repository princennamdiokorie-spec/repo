"""Measure selected decoded RGB frames using ffmpeg and Python's standard library."""
import argparse
import json
import subprocess


def samples(video, frames, crop):
    filters = "select='" + "+".join(f"eq(n,{frame})" for frame in frames) + "'"
    if crop:
        filters += ",crop=" + ":".join(map(str, crop)) + ":exact=1"
    filters += ",scale=160:160:flags=area,format=rgb24"
    data = subprocess.check_output([
        "ffmpeg", "-nostdin", "-v", "error", "-i", video, "-map", "0:v:0",
        "-vf", filters, "-fps_mode", "passthrough", "-frames:v", str(len(frames)),
        "-threads", "1", "-f", "rawvideo", "-",
    ])
    size = 160 * 160 * 3
    if len(data) != size * len(frames):
        raise ValueError("One or more requested frame indices are outside the video")
    for index, frame in enumerate(frames):
        yield frame, data[index * size:(index + 1) * size]


def stats(data):
    pixels = list(zip(data[::3], data[1::3], data[2::3]))
    ordered = sorted(pixels, key=luma)
    count = len(ordered)
    bright = mean_rgb(ordered[-max(1, count // 50):])
    return {
        "rgb_mean": mean_rgb(ordered),
        "luma_p01_p50_p99": [round(luma(ordered[int((count - 1) * p)]), 2)
                             for p in (.01, .50, .99)],
        "highlight_rgb": bright,
        "highlight_red_minus_blue": round(bright[0] - bright[2], 2),
    }


def luma(rgb):
    red, green, blue = rgb
    return .2126 * red + .7152 * green + .0722 * blue


def mean_rgb(pixels):
    return [round(sum(channel) / len(pixels), 2) for channel in zip(*pixels)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video")
    parser.add_argument("frames", nargs="+", type=int, help="zero-based decoded frame indices")
    parser.add_argument("--crop", type=int, nargs=4, metavar=("W", "H", "X", "Y"))
    args = parser.parse_args()
    if min(args.frames) < 0 or (args.crop and
        (min(args.crop[:2]) <= 0 or min(args.crop[2:]) < 0)):
        parser.error("Frame indices and crop offsets must be nonnegative, crop size positive")
    try:
        for index, pixels in samples(args.video, sorted(set(args.frames)), args.crop):
            print(json.dumps({"frame": index, **stats(pixels)}))
    except (ValueError, OSError, subprocess.SubprocessError) as error:
        parser.exit(1, f"{error}\n")
