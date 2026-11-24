"""Build a labelled contact sheet and export selected frames from a clip."""
import argparse
import io
import json
import math
from pathlib import Path
import subprocess

from PIL import Image, ImageDraw


def probe(clip):
    data = json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_streams", "-show_format",
        "-of", "json", str(clip),
    ]))
    video = next((stream for stream in data["streams"]
                  if stream["codec_type"] == "video"
                  and not stream.get("disposition", {}).get("attached_pic")), None)
    if video is None:
        raise ValueError("No video stream found")
    duration = float(video.get("duration") or data["format"].get("duration", 0))
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError("No usable video duration")
    return data, video["index"], duration


def extract(clip, stream_index, time):
    data = subprocess.check_output([
        "ffmpeg", "-nostdin", "-v", "error", "-ss", f"{time:.9f}",
        "-i", str(clip), "-map", f"0:{stream_index}", "-frames:v", "1",
        "-c:v", "png", "-threads", "1", "-f", "image2pipe", "-",
    ])
    if not data:
        raise ValueError(f"No frame available at or after {time:.3f}s")
    with Image.open(io.BytesIO(data)) as frame:
        return frame.convert("RGB")


def make_sheet(args):
    metadata, stream_index, duration = probe(args.clip)
    start = args.start
    end = duration if args.end is None else args.end
    if not 0 <= start < end <= duration or min(args.cols, args.count, args.thumb) < 1:
        raise ValueError("Use a valid sampling range and positive grid settings")
    requested = {float(value) for value in args.times.split(",") if value.strip()}
    if any(not 0 <= time < duration for time in requested):
        raise ValueError("Explicit timestamps must be within the clip")
    regular = {start + (end - start) * (index + 0.5) / args.count
               for index in range(args.count)}
    thumbs = []
    stills = {}
    for time in sorted(regular | requested):
        try:
            image = extract(args.clip, stream_index, time)
        except ValueError as error:
            if time in requested:
                raise
            print(f"Skipped sample: {error}")
            continue
        if time in requested:
            stills[time] = image.copy()
        image.thumbnail((args.thumb, args.thumb), Image.Resampling.LANCZOS)
        thumbs.append((time, image))
    if not thumbs:
        raise ValueError("No frames decoded")

    columns = min(args.cols, len(thumbs))
    label_height = 22
    tile_height = max(image.height for _, image in thumbs) + label_height
    rows = math.ceil(len(thumbs) / columns)
    sheet = Image.new("RGB", (columns * args.thumb, rows * tile_height))
    draw = ImageDraw.Draw(sheet)
    for index, (time, image) in enumerate(thumbs):
        x = index % columns * args.thumb
        y = index // columns * tile_height
        sheet.paste(image, (x + (args.thumb - image.width) // 2, y + label_height))
        draw.text((x + 5, y + 3), f"Seek {time:.3f}s", fill="white")

    out = args.out or Path(f"qc_{args.clip.stem}")
    out.mkdir(parents=True, exist_ok=True)
    for index, (time, image) in enumerate(sorted(stills.items()), 1):
        image.save(out / f"f_{index:03d}_{time:.6f}.png")
    sheet.save(out / "contact.jpg", quality=90)
    (out / "meta.txt").write_text(json.dumps(metadata, indent=2) + "\n")
    print(f"{len(thumbs)} samples and {len(stills)} individual stills: {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("clip", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--cols", type=int, default=4)
    parser.add_argument("--count", type=int, default=12)
    parser.add_argument("--thumb", type=int, default=480)
    parser.add_argument("--start", type=float, default=0.0)
    parser.add_argument("--end", type=float)
    parser.add_argument("--times", default="")
    try:
        make_sheet(parser.parse_args())
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        parser.exit(1, f"{error}\n")
