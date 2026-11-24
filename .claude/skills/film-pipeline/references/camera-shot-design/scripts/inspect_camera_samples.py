#!/usr/bin/env python3
"""Inspect evaluated camera samples; never substitutes for render or scene review."""
import argparse
import json
import math
import sys
from pathlib import Path


def number(value, label, minimum=None, strictly_positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{label}: expected a finite number")
    if strictly_positive and value <= 0:
        raise ValueError(f"{label}: must be positive")
    if minimum is not None and value < minimum:
        raise ValueError(f"{label}: must be >= {minimum}")
    return value


def vector(value, size, label):
    if not isinstance(value, list) or len(value) != size:
        raise ValueError(f"{label}: expected {size} components")
    return [number(x, label) for x in value]


def angle(a, b):
    dot = min(1.0, max(0.0, abs(sum(x * y for x, y in zip(a, b)))))
    return math.degrees(2 * math.acos(dot))


def inspect(data):
    if not isinstance(data, dict):
        raise ValueError("root must be an object")
    fps = number(data.get("fps"), "fps", strictly_positive=True)
    pos_eps = number(data.get("position_epsilon_m", 0.0001), "position_epsilon_m", minimum=0)
    ang_eps = number(data.get("angle_epsilon_deg", 0.01), "angle_epsilon_deg", minimum=0)
    source = data.get("samples")
    if not isinstance(source, list) or len(source) < 2:
        raise ValueError("samples: provide at least two samples")
    samples = []
    for row in source:
        if not isinstance(row, dict):
            raise ValueError("each sample must be an object")
        frame = number(row.get("frame"), "frame")
        if int(frame) != frame:
            raise ValueError("frame: expected integer frame number")
        if samples and frame <= samples[-1]["frame"]:
            raise ValueError("frame numbers must strictly increase")
        pos = vector(row.get("position"), 3, "position")
        quat = vector(row.get("quaternion"), 4, "quaternion wxyz")
        norm = math.hypot(*quat)
        if not math.isfinite(norm) or norm == 0:
            raise ValueError("quaternion must have a finite nonzero norm")
        samples.append({"frame": int(frame), "position": pos, "quaternion": [q / norm for q in quat]})
    steps = []
    reversals = {axis: [] for axis in "xyz"}
    previous_direction = [0, 0, 0]
    for a, b in zip(samples, samples[1:]):
        dt = (b["frame"] - a["frame"]) / fps
        delta = [y - x for x, y in zip(a["position"], b["position"])]
        distance = math.hypot(*delta)
        degrees = angle(a["quaternion"], b["quaternion"])
        steps.append({"from_frame": a["frame"], "to_frame": b["frame"],
                      "sample_gap": b["frame"] - a["frame"],
                      "distance_m": distance, "speed_m_s": distance / dt,
                      "rotation_deg": degrees, "angular_speed_deg_s": degrees / dt})
        for i, axis in enumerate("xyz"):
            direction = 0 if abs(delta[i]) <= pos_eps else (1 if delta[i] > 0 else -1)
            if direction and previous_direction[i] and direction != previous_direction[i]:
                reversals[axis].append({"from_frame": a["frame"], "to_frame": b["frame"]})
            if direction:
                previous_direction[i] = direction
    contiguous = all(s["sample_gap"] == 1 for s in steps)
    span = samples[-1]["frame"] - samples[0]["frame"]
    report = {
        "scope": "sampled world positions and orientations only; no visual, collision or saved-state verification",
        "sample_count": len(samples), "first_frame": samples[0]["frame"], "last_frame": samples[-1]["frame"],
        "fps": fps, "every_frame_in_sampled_range": contiguous,
        "sample_time_span_seconds": span / fps,
        "nominal_continuous_range_duration_seconds": (span + 1) / fps,
        "duration_note": "Range duration assumes a continuous constant-fps export; actual video metadata is not checked.",
        "sampled_path_length_m": sum(s["distance_m"] for s in steps),
        "net_displacement_m": math.dist(samples[0]["position"], samples[-1]["position"]),
        "max_sampled_speed_m_s": max(s["speed_m_s"] for s in steps),
        "max_sampled_angular_speed_deg_s": max(s["angular_speed_deg_s"] for s in steps),
        "axis_direction_reversals": reversals,
        "reversal_note": "Diagnostic only: compare with the brief; intended orbits may reverse an axis.",
        "steps": steps,
    }
    if "hold_start" in data:
        start = number(data["hold_start"], "hold_start")
        if int(start) != start:
            raise ValueError("hold_start must be an integer frame")
        hold = [s for s in samples if s["frame"] >= start]
        covered = (len(hold) >= 2 and hold[0]["frame"] == start and
                   all(b["frame"] - a["frame"] == 1 for a, b in zip(hold, hold[1:])))
        h = {"requested_start_frame": start, "end_frame": samples[-1]["frame"],
             "every_frame_from_hold_start_to_last_sample": covered,
             "measured_sample_count": len(hold), "result": "INSUFFICIENT_SAMPLES"}
        if len(hold) >= 2:
            displacement = max(math.dist(hold[0]["position"], s["position"]) for s in hold)
            rotation = max(angle(hold[0]["quaternion"], s["quaternion"]) for s in hold)
            moving = displacement > pos_eps or rotation > ang_eps
            h.update({"reference_frame": hold[0]["frame"], "max_displacement_from_reference_m": displacement,
                      "max_rotation_from_reference_deg": rotation,
                      "result": "MOTION_DETECTED" if moving else
                      ("STATIC_AT_EVERY_SAMPLED_FRAME" if covered else "STATIC_AT_SPARSE_SAMPLES_ONLY")})
        report["hold"] = h
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("samples", type=Path, help="JSON file; see references/camera-checks.md")
    args = parser.parse_args()
    try:
        report = inspect(json.loads(args.samples.read_text(encoding="utf-8")))
        print(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False))
    except (OSError, ValueError, TypeError, OverflowError) as error:
        print(f"Invalid camera samples: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
