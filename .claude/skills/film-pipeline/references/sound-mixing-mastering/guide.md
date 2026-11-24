> Source: [sound-mixing-mastering in Work](https://github.com/olegfedonyk-coder/Work/blob/main/skills/chatgpt/sound-mixing-mastering/SKILL.md). Follow documented project decisions when available.
> Project locks and director authority override generic examples/defaults below.


# Sound Mixing and Mastering

Balance and technically validate approved audio against a specified delivery.
Do not change the sound concept, add score or rewrite performance through mixing.

## Required inputs
Picture lock/version, approved dialogue/music/effects stems, common time origin,
sample rate, channel layout, intended destination and its supplied/current delivery
specification. Record missing stems and technical targets as TBD; there is no
single correct LUFS value for all platforms or types of programme.

## Session procedure
1. Preserve originals. Confirm durations, alignment, channel mapping, polarity
   problems and peak/clipping state before processing. Compare several sync points
   across the programme; don't align stems by filename or duration alone.
2. Set a repeatable monitoring level and listen in context. Establish dialogue
   intelligibility where dialogue is intended; silence and deliberately obscured
   speech follow the director's decision. Meter readings do not establish intent.
3. Balance stems and automate local masking problems before reaching for global
   compression. Record consequential processing. Audition EQ, dynamics and noise
   reduction at matched perceived level so louder is not mistaken for better.
4. Check transients, low-end buildup, phase/downmix compatibility, stereo placement,
   scene transitions, reverb tails and abrupt noise-floor changes. Evaluate on
   the specified channel layout; do not upmix or collapse channels silently.
5. Measure the complete exported programme for integrated loudness, loudness
   range and true peak using the required method. Short excerpts diagnose local
   trouble but cannot certify whole-programme compliance. Record tool/version,
   command/settings, measured range and target source.
6. Re-import or independently inspect the actual delivery file: codec, sample
   rate, channels, length, start offset, clipping and sync. Encoding may affect
   peaks; a compliant pre-encode session is not proof of the encoded result.

## Diagnosis order
- Dialogue unclear → check the recording, then processing, then balance; fix the
  presentation without damaging the natural performance. Capture problems go
  back to `production-sound-dialogue`.
- Music masks the moment → adjust the music/dialogue relationship before global
  processing; score changes belong to `music-score-supervision`.
- Scene feels flat → check dynamics, spatial depth and perspective before adding
  layers.
- Delivery check failed → fix and re-export, then measure the new file.
Typical failures: over-compression, flattened dynamics, music dominating dialogue,
inconsistent acoustic space, clipping, wrong loudness, invalid export.

## Boundaries
This skill owns how the audience hears the completed audio. What sounds exist
belongs to `sound-design`; how they were captured to `production-sound-dialogue`;
packaging and delivery to `finishing-delivery`.

## Verification and limits
Use representative difficult passages for processing comparisons, and the whole
export for final measurement/listening coverage. When listening is unavailable,
state that limitation and request a human check; do not call a meter-only pass
an approved mix. The bundled account `music-sound-supervision` audio measurement
helper can assist diagnostics but its onset estimates are not frame-accurate sync
proof. Confirm destination specs rather than importing historical platform values.

## Deliverable
Supply master/stems as requested, exact versions, format/channel map, sync offset,
processing summary, measurements versus targets and unresolved perceptual checks.
Separate TECHNICAL PASS from DIRECTOR APPROVAL. Coordinate final packaging with
`finishing-delivery` and preserve editable sources and the previous accepted mix.
