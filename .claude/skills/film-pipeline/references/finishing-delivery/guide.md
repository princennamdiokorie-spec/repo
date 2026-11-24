> Source: [finishing-delivery in Work](https://github.com/olegfedonyk-coder/Work/blob/main/skills/chatgpt/finishing-delivery/SKILL.md). Follow documented project decisions when available.
> Project locks and director authority override generic examples/defaults below.


# Finishing & Delivery

Transform an approved project state into a verified deliverable. Validate; do not redesign.

**Does not own:** creative changes (`directing`, `cinematography`, `editing-rhythm`), production problems of earlier stages (`ai-film-production`). Shared labels and skill map: `ai-film-production`.

## Workflow

`REQUIREMENTS → SOURCE MASTER → EXPORT SETTINGS → TECHNICAL CHECK → CREATIVE CHECK → DELIVERY STATUS`

1. **Requirements** — from the festival, platform or client spec the user provides: resolution, aspect ratio, frame rate, codec/container, colour space, audio format and channels, loudness, subtitles, naming, max file size, deadlines. If no spec is given, ask for it or the target; do not quote platform specs from memory as current — look them up or mark them unverified.
2. **Creative readiness** — approved edit version, continuity state, final graphics and titles, subtitles, sound state. Confirm with the user which version is the master.
3. **Technical check** — on an uploaded file, run `ffprobe` and report exact values; extract frames with an available tool such as ffmpeg to inspect image integrity (banding, compression blocks, black frames, flashes, crop errors). Report track count, channels, sample rate and duration. Check perceptual sync and sound quality only when audio review is available.
4. **Export verification** — compare output against source values and spec; check playback-critical flags (frame rate constant vs variable, pixel format, colour tags).
5. **Report** — status and findings.

Useful commands:
```
ffprobe -v error -show_format -show_streams -of json FILE
ffmpeg -i FILE -vf blackdetect=d=0.1:pix_th=0.10 -an -f null -   # black segments
ffmpeg -i FILE -af ebur128 -f null -                               # integrated loudness (LUFS)
```
Use available audio measurement tools for silence and true peak and report actual measurements. Music rights status per cue comes from `music-sound-supervision`; an unlicensed cue is a `REJECT` for public delivery unless the user accepts the risk.

## Professional knowledge

Master vs preview files; codec limits and generation loss; resolution, aspect and pixel-aspect rules; constant frame rate; colour tag mismatches (e.g. untagged Rec.709 shifting on platforms); audio channel layouts; subtitle timing and spelling; version control and naming. A technically valid file can still be the wrong deliverable.

AI-generated material: generated clips often arrive at different frame rates, resolutions and colour than the timeline; conform them before the master and list any upscaled or retimed shots.

## Status

- `PASS` — meets every stated requirement.
- `CONDITIONAL PASS` — deliverable with named, accepted deviations.
- `REJECT` — a requirement fails; name it and the fix.

## Control levels (definitions in `ai-film-production`)

`LOCK` required specs, approved master state, delivery format. `CONSTRAIN` technical and platform limits, archive rules. `GUIDE` optimization suggestions. `GENERATE` alternate exports only when requested.

## Checklist

□ resolution □ frame rate (constant) □ aspect ratio □ colour tags/space □ audio tracks, channels, duration match □ loudness if specified □ subtitles/text verified □ no black/flash/corrupt frames □ naming □ version identity documented

## Failure modes

Exporting the wrong version; changing creative content during finishing; ignoring platform specs; accepting corrupted generated frames; missed audio or subtitle issues; delivering without version tracking.

## Outputs

Delivery checklist, measured QC report, export settings, unresolved risks, final status.
