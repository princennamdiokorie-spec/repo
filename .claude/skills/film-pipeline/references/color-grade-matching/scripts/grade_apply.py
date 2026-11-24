"""Apply timeline-enabled color filters to SDR MP4/MOV without retiming."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import re
import subprocess
import tempfile

FILTERS = (
    "colorbalance", "colorchannelmixer", "colorcorrect", "colorlevels",
    "colortemperature", "curves", "eq", "huesaturation", "lut3d",
    "selectivecolor", "vibrance",
)


def probe(path):
    result = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_streams", "-of", "json", str(path),
    ])
    return json.loads(result)["streams"]


def frame_times(path, time_base):
    result = subprocess.check_output([
        "ffprobe", "-v", "error", "-select_streams", "v:0", "-show_frames",
        "-show_entries", "frame=best_effort_timestamp", "-of", "json", str(path),
    ])
    return [
        int(frame["best_effort_timestamp"]) * time_base
        for frame in json.loads(result)["frames"]
    ]


def stream_time(stream, key):
    value = stream.get(key)
    return None if value is None else int(value) * Fraction(stream["time_base"])


def verify(src_streams, dst_streams, src_times, dst_times):
    src_video, *src_audio = src_streams
    dst_video, *dst_audio = dst_streams
    if src_times != dst_times:
        raise ValueError(
            f"Video timestamps changed ({len(src_times)} → {len(dst_times)} frames)"
        )
    for key in ("width", "height", "pix_fmt", "sample_aspect_ratio",
                "color_range", "color_space", "color_transfer", "color_primaries"):
        if src_video.get(key) != dst_video.get(key):
            raise ValueError(f"Video property changed: {key}")
    if stream_time(src_video, "duration_ts") != stream_time(dst_video, "duration_ts"):
        raise ValueError("Video duration changed")
    if len(src_audio) != len(dst_audio):
        raise ValueError("Audio track count changed")
    for index, (before, after) in enumerate(zip(src_audio, dst_audio), 1):
        for key in ("codec_name", "channels", "channel_layout", "sample_rate"):
            if before.get(key) != after.get(key):
                raise ValueError(f"Audio track {index}: {key} changed")
        for key in ("start_pts", "duration_ts"):
            if stream_time(before, key) != stream_time(after, key):
                raise ValueError(f"Audio track {index}: {key} changed")


def grade(source, output, specs):
    if source.suffix.lower() not in (".mp4", ".mov") or (
        source.suffix.lower() != output.suffix.lower()
    ):
        raise ValueError("Use MP4 or MOV and keep the same container extension")
    if output.exists():
        raise ValueError("Output already exists")
    streams = probe(source)
    video = [s for s in streams if s["codec_type"] == "video"]
    audio = [s for s in streams if s["codec_type"] == "audio"]
    if len(video) != 1 or len(video) + len(audio) != len(streams):
        raise ValueError("Expected one video stream with optional audio streams")
    video = video[0]
    if video.get("pix_fmt") != "yuv420p" or video.get("color_transfer") in (
        "smpte2084", "arib-std-b67",
    ):
        raise ValueError("This workflow expects SDR 8-bit yuv420p")
    if video.get("field_order") not in (None, "unknown", "progressive"):
        raise ValueError("This workflow expects progressive video")
    if video.get("side_data_list"):
        raise ValueError("Video has side metadata requiring a separate workflow")
    time_base = Fraction(video["time_base"])
    times = frame_times(source, time_base)
    if not times:
        raise ValueError("No video frames found")

    filters = []
    for spec in specs:
        match = re.fullmatch(r"(\d+)-(\d+)=(.+)", spec)
        if not match:
            raise ValueError(f"Expected START-END=FILTER: {spec}")
        start, end = map(int, match.group(1, 2))
        if not 0 <= start < end <= len(times):
            raise ValueError(f"Frame range outside video: {start}-{end}")
        expression = match.group(3)
        name, _, options = expression.partition("=")
        if name not in FILTERS or not options or not re.fullmatch(
            r"[A-Za-z0-9_./:+*= -]+", options
        ):
            raise ValueError("Use one supported filter with simple named options per argument")
        if re.search(r"(?:^|:)enable\s*=", options):
            raise ValueError("Frame selection is supplied by START-END")
        filters.append(f"{expression}:enable='between(n,{start},{end - 1})'")

    with tempfile.TemporaryDirectory(dir=output.parent) as stage:
        candidate = Path(stage) / output.name
        subprocess.run([
            "ffmpeg", "-nostdin", "-v", "error", "-copyts", "-i", str(source),
            "-map", "0:v:0", "-map", "0:a?", "-map_metadata", "0",
            "-map_chapters", "0", "-vf", ",".join(filters), "-c:v", "libx264",
            "-pix_fmt", "yuv420p", "-crf", "14", "-preset", "veryfast",
            "-fps_mode:v", "passthrough", "-enc_time_base:v", str(time_base),
            "-video_track_timescale", str(time_base.denominator),
            "-c:a", "copy", "-avoid_negative_ts", "disabled", str(candidate),
        ], check=True)
        output_streams = probe(candidate)
        output_video = next(s for s in output_streams if s["codec_type"] == "video")
        verify(
            [video, *audio], output_streams, times,
            frame_times(candidate, Fraction(output_video["time_base"])),
        )
        output.hardlink_to(candidate)
    print(f"Verified {len(times)} video frames and {len(audio)} audio tracks: {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("grades", nargs="+", metavar="START-END=FILTER")
    args = parser.parse_args()
    try:
        grade(args.source, args.output, args.grades)
    except (ValueError, KeyError, OSError, subprocess.SubprocessError) as error:
        parser.exit(1, f"{error}\n")
