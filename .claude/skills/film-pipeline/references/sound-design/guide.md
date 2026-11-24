> Source: [sound-design in Work](https://github.com/olegfedonyk-coder/Work/blob/main/skills/chatgpt/sound-design/SKILL.md). Follow documented project decisions when available.
> Project locks and director authority override generic examples/defaults below.


# Sound Design

Translate approved action and environment into a timed sound plan or review.
Do not add story events, implied characters or emotional music through sound.

## Source and intent
Read the canonical scene, picture version, director's sound decisions and existing
tracks. Distinguish approved silence, diegetic sound, subjective treatment, score
and temporary audio. If the task is only review, do not create a new sound world.

## Scene function and sonic point of view
Before listing cues, state what the scene does and whose perception the audience
shares: objective room sound, a character's subjective focus or memory. That
choice decides what is heard, how distance, reflections, occlusion and materials
shape it, and where silence is meaningful. A recurring sound motif needs a
narrative purpose and director approval; generic library beds without purpose,
ambience used as decoration and effects replacing drama are failures.

## Event mapping
1. Watch/listen to the available material and record coverage. Build a cue ledger:
   event ID, source object/action, start/end, contact/sync point, perspective,
   reference, layer, status and owner. Use actual timebase; a still cannot establish
   timing. Mark inferred sound character as a proposal.
2. For each cue distinguish visible cause, established off-screen cause and new
   invention. Off-screen diegetic sound is legitimate only when supported by the
   scene/decision; absence from frame alone does not forbid it.
3. Specify physical qualities from approved materials and practical references:
   contact, weight, surface, distance, enclosure and decay. If unknown, request
   the exact reference. Do not decide how equipment works from its appearance.
4. Layer only what the event needs: onset/contact, body, mechanism and tail where
   supported. Avoid automatically adding every layer or filling every pause.
5. Check continuity across cuts: which source persists, changes perspective or
   stops? Sound bridges, subjective isolation and silence transitions affect
   storytelling and require approval rather than being technical defaults.

## Asset and implementation discipline
Record origin, exact version and usage rights/status for each supplied or selected
sound. Request missing library elements before searching personal archives.
Do not rename a similar sound as the approved asset. Preserve stems and editable
timing; do not bake music into an effects-only delivery. Generated audio must be
reviewed for invented speech, score, crowds and extra events before use.

## QC and handoff
Audition in scene context, then isolate problem cues. Check sync, recognizability,
perspective, continuity, masking of dialogue and whether the cue leaks a reveal.
Waveforms and loudness statistics do not prove these perceptual properties.
Report what was actually heard/measured and what needs human review.
Deliver the cue ledger, approved/proposed distinction, source list and stems with
time origin and channel layout to `sound-mixing-mastering`. Route score decisions
to `music-score-supervision`, dialogue repairs to `production-sound-dialogue`.
Director approval and generation launch remain outside this skill's authority.

## Outputs and boundaries
Typical outputs: scene sound map, location acoustic profile, Foley list,
off-screen event map, motif plan, transition plan and the mix hierarchy for
`sound-mixing-mastering`. Boundaries: `production-sound-dialogue` = captured
reality; `sound-design` = the created sonic world; `sound-mixing-mastering` =
final master; `finishing-delivery` = package.
