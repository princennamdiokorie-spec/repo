> Canonical repository version: [editing-rhythm](https://github.com/olegfedonyk-coder/Work/blob/main/skills/chatgpt/editing-rhythm/SKILL.md). Use project production discipline when applicable.
> Project locks and director authority override generic examples/defaults below.


# Editing Rhythm

Control of audience experience through time. Protect dramatic intention, attention and emotional continuity while turning shots into a sequence — and, for AI footage, decide which seconds of each generation can be trusted at all.

Respond in English by default. Preserve source filenames, identifiers and timecodes.

**Does not own:** music and sound decisions (`music-sound-supervision`), story structure (`screenwriting-dramaturgy`), staging (`directing`), shot design (`cinematography`), continuity tracking (`film-continuity`, `costume-hair-makeup-continuity`), generation failures (`ai-film-production`), export (`finishing-delivery`). Shared labels and skill map: `ai-film-production`.

## When not to use

Rewriting structure without naming consequences; replacing directing decisions; hiding weak writing with speed; changing approved chronology without review.

## Canon first

Project facts come from the canon, never from this skill: locked shot order and reveal order, target runtime, project frame rate, which beats are essential. Mark unknown project facts and state working assumptions for reversible proposals. If sources conflict on approved order or content, name the conflict and continue on unaffected decisions. Ask only when the missing decision materially affects the requested result.

Every cut decision is `ПРЕДЛОЖЕНО` until the author approves it. A cut that merely looks right to Claude is never `ЗАЛОЧЕНО`.

## Pick the mode first

| Mode | When | Output centre |
|---|---|---|
| **Plan** | before generating: shots exist as script/shot list only | cut plan, shot durations to request, handles, cover shots needed |
| **Assemble** | clips exist; build the sequence | usable ranges, edit map, pairs, joins |
| **Review** | a cut exists; "does it work?" | audience pass, redundant/missing beats, fixes |
| **Repair** | a cut or join is broken | which source to fix: trim, cover, regenerate |

Infer the mode from the request and supplied material. Combine modes when useful.

## Workflow

1. **Dramatic intent** — scene purpose, directing notes, emotional destination.
2. **Information flow** — what the audience knows before and after each shot: setup, reveal, reaction, payoff. Locked reveal order is not negotiable here.
3. **Shot function** — why each shot exists, what it gives, its emotional job. A shot without a function is a candidate for removal, however beautiful.
4. **Cut logic** — pick one reason per cut (Cut reasons), then check the pairing of the two shots (Editing grammar).
5. **Rhythm** — compression, expansion, pauses, repetition, acceleration, deceleration; checked against the numbers in the edit map.
6. **Joins** — every cut between two generations goes through the join check.
7. **Audience pass** — where attention drops, what repeats, which beat is missing.

## Cut reasons

| Reason | Use when | Check before committing |
|---|---|---|
| Information change | a new fact enters | the previous shot gave the audience time to take the old one |
| Reaction | the consequence matters more than the event | the reaction is truthful and long enough to read |
| Power shift | control passes between characters | eyelines and screen direction agree (`film-continuity`) |
| Action continuation | momentum must carry across | subject position and motion direction match on both sides, measured on frames |
| Viewpoint change | the audience needs a different relation to the space | geography stays readable |
| Rhythm change | tempo must break or lock | the change is motivated by the scene, not by boredom |
| Sound connection | image follows an audio event | a sound plan exists (`music-sound-supervision`) |

Default transition is the hard cut. A dissolve, fade, whip or other device needs a stated reason; "smoother" is not one.

## Editing grammar: what joins with what

A cut works when the two shots **differ enough** to bring something new (size, angle, content) and **agree enough** to keep one space, one time and one thought (geography, light, motion direction, eyeline, character state). Judge every adjacent pair on both axes. The rules below are working defaults of continuity editing, not laws: breaking one is allowed when it is a named decision with a reason.

### Size and angle

- Adjacent shots of the same subject must change shot size or camera angle clearly. As a rule of thumb, a camera move of roughly 30° or more, or a visible step in size. A near-identical pair reads as a jump cut — use it only deliberately.
- Build up: wide → medium → close raises intimacy and tension. Release: close → wide opens the context, isolates, or lets the pressure go.
- Jumping several sizes (wide → extreme close) is a shock or emphasis device. Spend it on a beat that deserves it.
- Different subjects at the same size cut cleanly; the same subject at the same size and angle does not.

### Axis and screen direction

- Keep the camera on one side of the line of action (the 180° line between two subjects, or along a path of travel). Crossing it needs a neutral shot on the line, a visible camera move across it, or a cutaway.
- A subject leaving frame right enters the next shot from the left, and the other way round, unless a neutral shot or a motivated reversal says otherwise.
- Geometry is measured, not eyeballed: take positions and directions from the previz (`blender-previz`) or from viewed frames; tracking belongs to `film-continuity`.

### Pairs

| Pair | Reads as | Works when | Watch for |
|---|---|---|---|
| Establishing wide → closer | orient, then intensify | geography is clear before the audience is asked to care | opening on a close shot when the space matters |
| Shot → reverse shot (dialogue, over-shoulder) | exchange between two | the reverse camera positions stay on the same side of the action/eyeline axis; eyelines meet; sizes mirror unless power imbalance is intended | both people looking the same screen direction |
| Look → object (eyeline match) | what the character sees | gaze direction and height agree with where the object is; the shot shows what could be seen from that position | an object shot taken from where the character cannot be |
| Action → action (cut on movement) | momentum carries | the movement continues in the same direction at a similar speed; the cut falls mid-movement, not at rest | repeating the action on both sides instead of overlapping it |
| Action → reaction | event, then consequence | the reaction gets its time; the event was readable first | cutting to the reaction before the event registered |
| Static → moving camera (and back) | change of energy | the move is motivated; enter or leave it at matching speed | cutting between a pan and a frozen frame of the same size |
| Moving → moving | continuous energy | direction and speed agree across the cut | opposed directions with no reason |
| Detail / insert → master | specific thing, then its context | the insert is placed in the space; the master shows what changed | an insert that could belong to any scene |
| Match cut (graphic, movement, idea) | link between two things | position in frame, shape or motion rhyme across the cut | a rhyme with no meaning |
| Cutaway | relief, or cover for a join | related to the scene; the return keeps time and state consistent | an unrelated cutaway implying a connection |
| Cross-cutting (parallel action) | two lines move together | linked by time, theme or consequence; segments shorten toward convergence | alternation with no relation between the lines |
| Time or place change | ellipsis, flashback | the boundary is marked by a rhyme, a sound bridge, a change in grade or age (`film-continuity`) | an unmarked jump that reads as an error |

### Juxtaposition makes meaning

The audience links any two adjacent shots (the Kuleshov effect): a face followed by an object means "looks at it"; a face followed by something sad means "feels it". So check each pair for an **unintended** relation. This matters especially with AI footage, where leftover generations from different prompts, locations or lighting land side by side.

### What to match and what to vary between neighbours

- Match: light direction and colour temperature within a scene, grade, lens feel, subject scale for the same character, headroom, eye height, state of costume and props.
- Vary: shot size, angle, subject placement in frame (alternate sides), content.
- Two generations of the same shot description are alternate takes, not coverage — they rarely differ enough for a clean cut and rarely agree enough for a join.

### Scene shape (default order, adjust to intent)

1. Establish the space once, as wide as the geography requires.
2. Enter close to the first event, not before it.
3. Alternate coverage by who holds the audience's attention, not by who speaks.
4. Step closer as tension or intimacy rises; hold the strongest size for the strongest beat.
5. Release or isolate with a wider shot; leave early on an image that carries the next scene's question.

### Sound across the cut

J-cut (sound of the next shot leads the picture) and L-cut (sound of the previous shot lingers) soften and connect; a hard sound-and-picture cut hits. Cut on a sound event when the audience should feel the image follow it. Sound design and measurement belong to `music-sound-supervision`.

## Edit map

```
| # | shot | source clip (file+version) | in–out (s / frames) | duration | function | cut reason | pair check (size · angle · axis · eyeline · light) | usable-range status | join check | sound across the cut | status |
```

Rules for the map:

- Name it with a version; keep exactly one editable master (the edit map or the NLE project — one, declared). Everything else is derived and read-only.
- **Runtime is the sum of the duration column, recomputed every time.** Report it next to the canon target and name any gap. Never quote a target as if it were the result.
- Report average shot length and the spread (shortest, longest). A run of several shots with near-equal durations is a flag for mechanical rhythm — justify it or break it.
- Durations in frames at the project frame rate from the canon; confirm each clip's real fps with `ffprobe` and flag mismatches before any timing is trusted.
- Fill the pair check from viewed frames or previz numbers. An unfilled cell is `НЕИЗВЕСТНО`, not passed.

## Duration and rhythm

Duration depends on information density, emotional processing time, performance detail, tension, composition complexity and surrounding rhythm. Cut on thought when psychology matters; cut on action when momentum matters; hold after important moments; enter close to the active event unless atmosphere needs delay. Preserve truthful reactions, pauses and hesitation; respect breath and gaze timing; do not repeat the same realization.

Starting estimates, to be replaced by measurement: spoken Russian runs roughly 2.5–3.5 words per second; subtitles read at about 15–17 characters per second. Measure the real dialogue track (`audio_measure.py`) or use the canon's timing when it exists, and let that overrule the estimate.

A shot must earn its length by something it contains: a thought, a movement, a change. "It looks nice" earns a frame, not a second.

## AI clips: choosing the usable range

Choose by stability, not length. Run it as a procedure, not an impression.

1. **Probe.** Real duration, fps, frame count, audio presence — `contact_sheet.py` writes `meta.txt`; for a frame-exact count: `ffprobe -v error -select_streams v:0 -count_frames -show_entries stream=nb_read_frames,avg_frame_rate -of csv=p=0 CLIP`. Flag an fps that differs from the project's.
2. **Coarse pass.** `python3 ../ai-film-production/scripts/contact_sheet.py CLIP --count 12` — view the sheet.
3. **Fine pass at the candidate edges.** `--start S --end E --count N` and `--times t1,t2,...` around the planned in and out, a frame before and a frame after each; view them. State exactly which timecodes were viewed.
4. **Artifact checklist** at every viewed frame: face and identity drift; hands and fingers; props appearing, vanishing or changing; wardrobe and accessory state; signage and text; feet contact and limb mechanics; unplanned camera drift or reframing; light, exposure or colour pumping; background pop-in and cloned or frozen extras; mouth versus speech; object scale.
5. **Mark the range.** Record the first frame where each defect appears. `out` = last clean frame minus a margin; `in` = first frame where pose, light and identity have settled. Starts often settle and ends often degrade — expect to trim both.
6. **Label the result:** `CLEAN` (usable as is) · `COVER` (usable only with a planned cutaway, reaction or occlusion at a named time) · `REJECT` (no stable range that serves the shot's function).
7. **State the limit.** Still frames cannot prove motion quality: flicker, jitter, foot sliding and weightlessness are `unverified in motion` until the author plays the clip. Never mark them passed on stills alone. If the clip could not be opened or frames could not be viewed, the review is `blocked`, not passed.

`REJECT` is a finding about the source, not a licence to keep broken footage because it is longer. Hand the failure to `ai-film-production` for diagnosis rather than papering over it in the cut.

## Coverage and approval boundary
An unverified join remains unverified until both clips are inspected. Do not invent
a reaction, insert, cutaway or shorter take to hide it. Proposed repair may use
existing approved coverage; new coverage or changed duration requires a director
decision. Technical rejection is a recommendation, not authority to discard an
accepted performance. Locked black/silence/sparse sound overrides room-tone defaults.

## Cutting around artifacts

Preferred, in order: trim before the defect; cut away on a reaction or insert the story already supports; hide the join in an occlusion or pass-through that exists in the shot; change angle so the defective element leaves frame. Speed changes belong on non-performance elements only — retiming a body or a face changes its weight and psychology. Freezes and reversals only where nothing physical reads. Do not interpolate frames to stretch a performance. Do not use "fast cutting" to hide a failed take; that is speed hiding weak footage.

## Joins between generations

Drift is most visible at the join. Before approving any cut between two generations, check on viewed frames of both sides:

- identity anchors and wardrobe/prop state (`costume-hair-makeup-continuity`, `film-continuity`)
- light direction and colour temperature, exposure level, grade
- lens feel and subject scale; screen direction and eyeline
- motion vector at the cut: the subject leaves and enters frame in agreeing directions at agreeing speed
- room tone and ambience, as flagged to `music-sound-supervision`

A join mid-action is allowed only when the action-continuation check passes on both sides. When the check cannot be made, the join is `unverified` and a cut on a motivated reaction or cutaway replaces it.

## Plan mode: cut before you generate

The cut decides what to generate, not the other way round.

- For each shot, give the duration the edit needs, plus handles for the settling start and the degrading end — then request the length that contains both.
- Plan the pairs: for each cut, state the size and angle change, the axis side, and the screen direction of motion, so that coverage is generated to cut together rather than as isolated pretty shots.
- Name each shot's required last frame when the next shot depends on it (position, pose, light), so the next generation can start from it.
- Inventory cheap cover — reactions, inserts, environment — for every shot flagged high artifact risk.
- Count generations needed against budget with `production-management`; do not buy a long take where two short shots and a cut give the same information.

## Sound

Claude cannot listen. Sound bridges, J/L cuts, music cues and beat times are designed on the edit map and sourced from `music-sound-supervision`; cutting on a beat uses onset times measured with `audio_measure.py`. Every claim about sound sync is `blocked — author's ear` until the author listens.

## Audience pass

This is an analytical simulation from the edit map and viewed frames, not a viewing of the cut. Say so. Check: what a first-time viewer knows after each shot; where information repeats; where nothing new arrives for too long; which beat the sequence needs but lacks; whether the picture alone carries the story; whether any adjacent pair implies a relation nobody intended. Do not claim how it feels to watch — claim what it contains.

## Control levels (definitions in `ai-film-production`)

`LOCK` approved reveal order, essential beats, character state. `CONSTRAIN` continuity, geography, performance timing. `GUIDE` stylistic rhythm, transition options. `GENERATE` alternative pacing experiments — only when asked.

## Decision questions before changing a cut

Clearer story? Better emotional timing? Psychology preserved? Continuity kept? Supports the directing language? Does it cost a locked beat?

## Failure modes

Cutting only because a shot feels long; equal-duration mechanical rhythm; speed hiding weak scenes; losing reactions to coverage; keeping beautiful redundant shots; ignoring sound-driven transitions; breaking continuity for convenience; keeping broken AI footage because it is longer; trusting a clip's nominal duration instead of its real length; approving a join on one side's frames only; calling stills proof of smooth motion; stretching a performance with interpolation or slow-down; generating long takes to cut down instead of planning short shots; treating a liked generation as locked; cutting two near-identical shots of one subject (accidental jump cut); crossing the axis without a neutral shot; leaving an unintended relation between neighbouring shots; opening on a close shot when geography matters; alternating by who speaks instead of who holds attention.

## Examples (generic)

- *Unexpected news:* hold on the reaction; the audience needs time.
- *Generated clip with unstable last seconds:* keep the stable section, design the transition before the artifact, and mark the range with the first defect's timecode.
- *Two characters repeating a realization from several angles:* keep the strongest moment, drop the rest.
- *Two generations of one location with different light:* the join fails the check; cut on a reaction or insert, or send the light difference back as a source fix — do not grade the mismatch away silently.
- *Dialogue between two people:* wide to place them, then over-shoulder reverse pairs on the same side of the action/eyeline axis with matched eyelines; step closer on the line that shifts power; return to the wide to release.
- *Character looks off-screen:* cut to what they see only if the object shot is taken from a position consistent with their gaze direction and height.

## Outputs

Edit map with recomputed runtime and its gap to target; cut points with reasons; pair checks for every cut; usable ranges for AI clips with viewed timecodes and `CLEAN/COVER/REJECT`; join checks; transition notes; pacing notes; list of missing or redundant beats; every item marked `unverified in motion` or `blocked` that could not be checked; for each decision the rejected alternative and why, so it does not return later as a fresh idea.

## Self-check

Mode named? Canon and reveal order respected? Runtime summed, not quoted? Real fps and length probed? Viewed timecodes stated? Motion-dependent claims marked unverified? Each adjacent pair checked for size, angle, axis, eyeline, light and unintended meaning? Every inter-generation join checked on both sides? Sound claims marked blocked? Rejected alternatives recorded? Own errors named separately, not fixed silently?
## Cutting rules

Source: the director's documents `Zanussi_1.doc` and `Zanussi_2.doc` (2026-10-06): «О монтаже любительского фильма», chapters on shot sizes, camera movement and cutting. Preserve this attribution for the supplied digest. The operational qualifications below distinguish continuity checks, useful starting heuristics and deliberate directing choices; they are not verbatim claims from those documents.

Use this checklist when building a Blender cut list, preparing a Seedance multishot handoff, and reviewing generated clips. Approved project decisions and previz remain authoritative. A heuristic mismatch alone is not a failed shot and does not authorize changing the approved camera, action or edit.

### Contents

- Source rules (Zanussi, classic baseline)
- Terms and planning order
- When to cut
- Shot size and camera angle
- Lens, light and composition
- Movement across a cut
- Camera movement instead of cutting
- Application to previz, prompts and review
- Technical references

### Source rules (Zanussi, classic baseline)

The rules as the source states them, paraphrased. They are the classic continuity baseline of 1970s amateur-film practice: use them as the starting point; the sections below give the current, qualified reading, which wins when they differ. Items marked ⚠ are corrected below.

1. Cut when the current shot's content is exhausted; every new shot must bring something new.
2. Wide shots run longer than close shots; a place already shown can return briefly.
3. Do not cut two shots of the same person at the same size, nor at adjacent sizes; cut «через один» (CU↔MS, MS↔FS, MCU↔MLS). Skipping several sizes is an accent («столкновение»), not a smooth cut.
4. No «прыжок по оси»: change the camera direction by 30–90° between consecutive shots of the same people.
5. Keep the camera on one side of the eyeline axis; in adjacent shots a person keeps the same profile; a character at the frame edge stays on that side in the closer shot.
6. Cut on a small action (sit, stand, pick up, turn); give about ¾ of the movement to the wider shot and ¼ to the closer one; shoot overlaps («захлёсты»).
7. Do not cut away from an unfinished simple action; keep ~15 frames of tail.
8. A camera move starts and ends with at least 1 s of static frame; do not cut from one move straight into another.
9. Keep the screen direction of movement; to reverse it, show an on-axis shot in between.
10. Similar shot sizes in one scene use the same lens; reverse shots keep the same camera height.
11. ⚠ "A closer shot comes out overexposed because illuminance falls with the square of the distance to the camera" — physically wrong: subject illuminance depends on the distance to the light, not to the camera (see Exposure below).
12. ⚠ "A zoom deforms space" — at a fixed viewpoint a zoom changes only the angle of view; perspective changes with camera position (see Zoom below).
13. ⚠ "A POV pan runs opposite to the head turn" — derive pan direction from the gaze and the layout (see Pans below).

### Terms

- **План (shot size)** — detail (ECU) → close-up (CU) → medium close-up (MCU) → medium (MS) → medium long / cowboy (MLS) → full figure (FS) → wide (WS) → extreme wide (EWS). Boundaries vary with subject and framing; state the actual crop.
- **Кадр (shot)** — one continuous camera take; size can change within it through camera or actor movement.
- **Монтажный скачок (jump)** — an unintended discontinuity of framing, action or space. A deliberately used jump cut is a stylistic choice.
- **Монтажное столкновение (collision)** — an intended contrast across a cut. It is one possible choice, not the required name for every departure from a heuristic.
- **«Тактичный» (tactful)** — a cut or move that follows the viewer's attention and does not call attention to itself.
- **Error classes:** material continuity (props, costume, pose, time); visual continuity (composition, light, contrast, lens); direction (movement, gaze, geography); information and rhythm (wrong reveal, premature or late cut). Treat a difference as a defect only when it contradicts the intended continuity or approved brief.

### Planning order (the viewer's questions)

Plan how the scene answers **«Где?»**, **«Кто?»**, **«Что происходит?»**. A wide can establish geography; a full or medium shot can introduce a person and their action; a close-up or detail can focus attention on a reaction or object. This is a useful coverage pattern, not a mandatory shot order. A scene can start close and reveal its geography later when the story calls for it.

### When to cut

1. Cut when a new image, reaction, sound or withheld piece of information serves the scene. Readability and emotional timing matter more than exhausting every action in the current shot.
2. Allow enough time to orient in a new wide; a familiar place can register faster. Size alone does not determine duration.
3. For a self-contained gesture that the audience needs to read in one shot, let it resolve and retain a usable tail (about 15 frames is a starting handle). For continuous action covered by two shots, a cut **during** the gesture can hide the transition: follow rules 20–22. Do not turn gesture completion into a blanket ban on cutting on action.
4. Capture/generate sufficient head and tail handles for the intended edit. Handles belong to coverage; the final edit need not retain them.

### Shot size across a cut (same subject)

5. Two shots with nearly identical size, angle and composition can produce an unwanted jump. The same size from a meaningfully different angle, or a motivated reverse shot, can cut smoothly.
6. Adjacent sizes (CU↔MCU, MCU↔MS, MS↔MLS, MLS↔FS) need a clear change of viewpoint, attention or action; they are not automatically errors.
7. Cutting **«через один»** (for example CU↔MS or MS↔FS) is a useful starting pattern for distinct coverage. Judge the actual images and action rather than the size labels alone.
8. A large size change (CU↔WS) can create an accent, establish geography or reveal context. Record an intended contrast when relevant; a size gap alone does not prove a collision or failed continuity.

### Camera angle across a cut

9. A change of roughly 30° or more **around the subject** is a common starting heuristic for two similar-size views. It is not a universal 30–90° requirement. An axial cut can be usable with a clear size change or motivated action; avoid an accidental near-identical punch-in. Changing focal length at one viewpoint changes the crop, not the viewpoint itself.
10. **Eyeline axis (180° line):** preserve the intended left/right relationship of people and gaze. For dialogue, choose camera positions on the same side of the interaction axis unless a visible crossing, neutral view, re-establishment or deliberate disorientation motivates a change. Derive over-the-shoulder placement from this geography; do not impose a blanket left-profile/left-shoulder formula.
11. Keep an established character's screen position across a closer cut when it supports attention and orientation. A purposeful repositioning or reveal can be valid; state it when continuity depends on it.
12. Reverse shots can use matched or deliberately different sizes. Their gaze directions, subject placement and relationship must agree with the intended geography and identification.
13. Match or deliberately vary camera height to serve eyelines and subject scale. Equal camera height is a coverage option, not a rule that every reverse shot must share an identical horizon.
14. Motivate a POV with a readable look, action, sound or established viewpoint. A preceding medium or close view often helps, but a wide does not inherently make the POV unreadable.
15. An over-the-shoulder or other spatial bridge can establish geography and connect separately filmed spaces. Check that the resulting screen relationship is coherent.

### Lens, light and composition across a cut

16. Check viewpoint, camera-to-subject distance, FOV, relative subject/background scale, depth of field and lens rendering. Similar shot sizes do not require the same focal length. A focal-length change at a fixed viewpoint changes magnification/FOV; changing camera position changes perspective. Evaluate whether the images join as intended.
17. Preserve believable source direction, subject exposure, colour and contrast within a continuous moment. Different angles can naturally show different light; correct an unintended lighting jump rather than forcing all shots into identical front/back lighting or tonal shapes.
18. **Exposure:** compare actual subject luminance and highlights. A closer crop is not inherently brighter at fixed manual exposure and unchanged illumination. Framing can affect automatic metering, a moved camera/light can affect illumination, and grading can introduce a mismatch. Correct the measured cause; do not change exposure merely because the shot is closer.
19. Composition can carry attention across a cut through subject placement, visual weight and the gaze target. Matching geometric shapes is one option; it is not mandatory in every adjacent image.

### Movement across a cut

19a. **Pose recording for matching:** at a setup change, record the actor's pose, head angle and prop contact so coverage can be reproduced. In previz, record the outgoing and incoming action phases. An exact held-pose match is appropriate for a cut during a hold; motion should normally advance across adjacent frames rather than freeze or repeat a frame automatically.

20. **Cut on action (малое монтажное движение):** a turn, sit, reach, lift or release can hide a cut. Capture overlapping coverage of the same action, with matching direction, phase, contact and plausible timing, then select the edit point.
21. **¾ / ¼ split:** as an initial trial, give more of the gesture to the wide and its completion to the closer view. This ratio is illustrative; cut where the actual performance reads best, including the reverse order when motivated.
22. **Overlap (захлёст):** repeat the action in coverage to give the editor options. The assembled action normally advances continuously; retaining repeated time or a freeze is a deliberate edit choice, not an automatic matching requirement.
23. **Screen speed:** compare apparent direction and speed at the chosen cut, accounting for image scale and camera angle. Adjust the cut point or coverage when authorized; do not slow the actor, alter physical timing or retime a locked previz solely to force equal pixel speeds.
24. **Camera-move handles:** a static lead-in and settle of about 1 s can provide editing options when the shot design allows them. Cuts between moving shots, or during a move, can work when action, direction and rhythm motivate them. Preserve approved previz timing; do not add obligatory pauses or reject a move-to-move cut automatically.
25. **Screen direction:** keep the established direction for continuous travel unless the subject visibly turns, the camera crosses/re-establishes the axis, or disorientation is intended. An on-axis view or spatial bridge can help establish a change.
26. **Exits and entries («пассажи»):** for continuous left-to-right travel across two lateral views, exit frame right and enter the next frame from the left; reverse this for right-to-left travel. Entering from the same edge as the previous exit reverses the apparent direction and needs a motivated turn or new geography. Empty-frame holds can suggest elapsed time; choose them for the intended rhythm.
27. **Same person, different situation:** a direct cut between places or times is an available ellipsis or match cut. Establish the new context when the story requires it; leaving frame, an insert or an empty-room opening are options, not prerequisites.
28. Movement in neighbouring shots can carry attention across a transition. Check its meaning and direction; unrelated gestures do not automatically guarantee a smooth or meaningful cut.

### Moving the camera instead of cutting

29. A size change can happen through camera movement, actor movement or both. Choose continuous observation or a cut according to the scene's information and rhythm; a cut need not be consciously noticed.
30. **Motivated moves:** follow action, a gaze, a reveal, a spatial relationship or dramatic attention. A moving object is one motivation; a still subject or location can also justify a move.
31. **Emphatic moves:** use a deliberate push, pull or reveal for the intended dramatic effect. An accent need not be reserved for the climax.
32. Match move speed to the scene and the approved timing. Very slow pushes are possible; speed is a directing choice, not a realism score.
33. **Pans:** a following pan can track action; an empty or POV pan can reveal geography or follow attention. Derive the pan direction from the character's gaze and the world's layout, not an automatic direction opposite to the head turn. A whip pan (швенк, смазка) is a deliberate fast transition; verify its spatial and temporal meaning.
34. **Zoom:** change focal length to alter magnification and angle of view. At a fixed camera viewpoint, zoom does not by itself change perspective. A dolly changes the viewpoint and foreground/background relationship; a dolly zoom combines both. Distinguish lens distortion, focus breathing and the stylistic visibility of a zoom from perspective. Zoom is not restricted to flat compositions.
35. A long take can develop through framing, blocking, performance, sound or a changing point of attention. Do not add movement merely to avoid a static shot.

### How to apply this (AI previz and generation)

- **Previz cut list:** record the size pair, camera positions and subject/eyeline axis, screen direction, outgoing/incoming action phase, attention target and timing. When judging angle change, measure camera positions around the subject as well as aim direction: the angle between optical view vectors alone does not establish axis side or a meaningful viewpoint change.
- **Matching action:** distinguish a hold cut from a motion cut. For a hold, preserve pose and gaze. For motion, preserve a continuous phase and contact state without an accidental temporal repeat. Read the current shot record before using a historical example; SB10 versions change gaze timing, framing and handle length. A superseded version is not a current generation input.
- **Seedance multishot:** state the approved cuts and action phases. Follow the current previz's timing and movement; do not redesign it to satisfy size-step, angle-change, action-split or handle heuristics.
- **Review:** check intended story/reveal → geography and axis → screen direction/eyeline → action phase/contact → framing and apparent speed → lighting/exposure/colour → lens rendering. If a mismatch exists, describe its visible effect and evidence. Do not fail a shot solely because a heuristic is not followed.
- **Authorized variation:** record the intent when a cut deliberately departs from established continuity. A motivated reverse shot, ellipsis, axial cut or size change need not be reclassified as a collision. Propose changes to locked shot design to the director before implementation.

### Technical references

- [Sony — Focal length, angle of view and perspective](https://www.sony.com/ug/electronics/focal-length-angle-of-view-perspective): distinguish focal-length/FOV changes from perspective changes caused by camera distance.
- [Adobe — The 180-degree rule](https://www.adobe.com/uk/creativecloud/video/discover/what-is-the-180-degree-rule.html): establish the interaction axis and distinguish continuity from an intentional axis crossing.
