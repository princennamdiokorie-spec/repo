> Source: [AI Film Production in Work](https://github.com/olegfedonyk-coder/Work/blob/main/skills/chatgpt/ai-film-production/SKILL.md).
> Project locks and director authority override generic examples/defaults below.


# AI Film Production

Turn locked film facts into shots. The goal is not an attractive generation; it is a shot that preserves every locked fact and adds only the intended generative detail and motion. AI generation is an execution layer, never a new directing layer.

## Repository operating model

Use the relevant current shot records and approved project decisions when available. Record repository work through the project's existing workflow. The director owns creative decisions and approves takes. A current explicit director instruction governs the current task even before it is documented. Use the [Work production discipline](https://github.com/olegfedonyk-coder/Work/blob/main/skills/PRODUCTION_DISCIPLINE.md) when operating in that repository.

## Shared labels (canonical definitions — other film skills refer here)

Two independent axes. Do not mix them.

**Provenance — where a fact comes from:**
| Label | Meaning |
|-------|---------|
| `LOCKED` | approved canon/decisions and the approved spatial baseline. Measurements provide evidence; they do not approve a new baseline. Does not change without the user's approval. |
| `GIVEN` | supplied by the user: references, photos, assets, statements. |
| `AI-GENERATED` | proposed or produced by AI (including Claude). Never authority for the next generation and never canon until the user approves it. |
| `TBD` | needed but not confirmed. Label uncertainty, continue independent work and ask only when the missing decision materially affects the result. |

**Control level — how much a property may vary in a generation:**
| Label | Meaning |
|-------|---------|
| `LOCK` | must match exactly enough to keep story, identity or spatial truth |
| `CONSTRAIN` | may vary only inside a narrow stated range |
| `GUIDE` | model interpretation acceptable if direction survives |
| `GENERATE` | deliberately left to the model |

**Evidence — for diagnosis:** `FACT` (observed), `HYPOTHESIS` (possible cause), `PROPOSAL` (suggested change), `TEST RESULT` (verified by a test). One generation is never proof of a cause.

Never promote an assumption or an unapproved generation to `GIVEN` or `LOCKED`.

## Skill map — one owner per job

Use the specialist where available. Some entries are repository workflows, so verify availability before treating an entry as installed.

| Job | Owner skill |
|-----|------------|
| Script, scene structure, dialogue text | `screenwriting-dramaturgy` |
| Story canon document | `story-bible-builder` |
| Objectives, beats, blocking, acting direction, stillness | [Acting direction](../ai-film-acting-direction/guide.md) |
| Why and how a shot is photographed (size, lens intent, light, movement) | [Cinematography](../cinematography-shot-design/guide.md) |
| Blender camera path or camera previz review | `camera-shot-design` or `previz-shot-review`; use tools available in the selected environment. |
| Blender previz → Seedance photoreal pipeline and its stage diagnosis | `previz-to-photoreal` |
| Seedance prompt control architecture | explicitly selected template, including `cinema-director-v3`; do not mechanically merge templates |
| Higgsfield host prompt adaptation | `higgsfield-seedance-prompt`, subject to the selected template and current mode evidence |
| Character identity plates, sheets, outfits on the character | `character-builder` |
| Scene/location plates (stills without the character-building job) | `banana-pro-director-30` (scene-plate mode only) |
| Who the character is physically; identity anchors | `casting-direction` |
| Clothing concept | `costume-design` |
| Hair, makeup, age/condition look | `hair-makeup-design` |
| Appearance state shot to shot | `costume-hair-makeup-continuity` |
| Shot-to-shot continuity: props, axis, action phase, time, sound bridges | `film-continuity` |
| Body mechanics | `human-motion-biomechanics` |
| Sport action | `sports-action-choreography` |
| Hand–prop contact in 3D | `character-prop-motion` |
| Background people | `crowd-background-performance` |
| Cut order and rhythm | `editing-rhythm` |
| Music/score decisions and briefs | `music-score-supervision`; account `music-sound-supervision` supplies spotting and measurement methods |
| Dialogue cleanup and sync | `production-sound-dialogue` |
| Sound events, ambience and effects | `sound-design` |
| Mix, loudness and audio mastering | `sound-mixing-mastering` |
| Export and final master check | `finishing-delivery` |
| Plan, blockers, next step, generation budget | `production-management` |

Use the bundle index to locate available workflows. Specialist names elsewhere in these notes are descriptive when their instructions are absent from the bundle.

## Source priority

1. project canon (script, approved decisions);
2. approved shot description;
3. approved camera data;
4. Blender previz;
5. approved reference assets;
6. model-specific generation rules;
7. prompt text.

A lower source may realize a higher one but may not contradict, replace or silently reinterpret it. When two sources conflict, name both and ask which is current.

## Method

`SHOT REQUIREMENTS → CONSTRAINT CLASSIFICATION → SOURCE PACKAGE → MODEL / MODE CHOICE → PROMPT → RISK CHECK → LAUNCH HANDOFF → GENERATION → QC → DIAGNOSIS → ONE-VARIABLE REVISION → ACCEPTED MASTER`

### 1. Shot requirements
Read the current shot state, locked decisions, character references, camera/previz facts, design constraints and previous test results from the sources that exist. List what is missing as `TBD`.

### 2. Constraint classification
Split the shot into control domains and give each a control level: identity; wardrobe/appearance; environment/geometry; camera/lens; blocking; body motion; facial performance; hero props; light; materials; text/graphics; temporal continuity; sound (decided in `music-sound-supervision`). Typical `LOCK`: identity anchors, hero prop, required text/number, camera path, major architecture, action order, story-critical object count.

**One idea per shot.** State the shot's single controlling idea as a mechanical rule, then derive its 3–4 physical consequences ("the device is never visible" → no outside view, no hand holding it, no table with it). Prioritize diagnostic attention, but preserve every approved lock. Conflicting locks require a director decision; none silently yields. A shot with several equal ideas produces a beautiful background and nothing happening.

### 3. Source package
Record which source owns identity, geometry, camera, performance and design; approved stills/frames; previz render; motion references; aspect ratio, duration, resolution; crop/overscan; exposure caveats. Avoid references that imply different faces, cameras or spaces.

**Per reference, say what is taken and what is not.** A reference carries more than its role: people, hands, clothing, lighting, colour temperature, grade, depth of field, framing, aspect ratio, background, props, layout. For each reference name the one thing it supplies and treat everything else as not taken. An unnamed carry-over is contamination and is checked in QC.

**Missing asset.** Look in supplied and connected project sources within scope. When the exact asset is still missing and materially needed, ask for it. Never pick a similar replacement or infer identity from a filename.
```
NEEDED: [exact asset or information]
PURPOSE: [why the shot needs it]
AFFECTS: [shot / document / step]
REQUEST: can you send the exact file?
```
Until the exact input is confirmed, the item stays `TBD`.

### 4. Model and mode
For video, use Seedance 2.5 and choose a supported mode according to the dominant constraint. For still-image work, follow the project workflow.
| Dominant constraint | Mode |
|---------------------|------|
| free concept exploration | text-to-image |
| identity/design lock | reference-driven still (`character-builder`) |
| start appearance matters more than end | image-to-video |
| camera/spatial truth from Blender | reference-to-video with the previz render as camera & motion reference (`previz-to-photoreal`, `higgsfield-seedance-prompt`) |
| motion good, appearance wrong | video edit |
| clip too short, continuation needed | video extend |

Check the current model documentation before claiming a capability, slot, limit or setting. State unverified capabilities as unverified.

### 5. Prompt
Hand the prompt to the model's prompt skill. From this skill it receives: the control-level table, the reference binding (one role per reference, fixed order within a comparison series), the action order `START STATE → ACTION → REACTION → ACTION → END STATE`, what must not change, and the risk list. Camera locked by previz → no independent camera move in text. Negative wording follows the model skill's rules, not a general habit.

**Use sourced measurements.** State units, reference frame and method. Cross-check scale against available measured anchors; do not fabricate three comparisons to meet a template. A missing measurement is TBD, not an invitation to invent precision.

### 6. Risk check
Flag: hands and object contact; text, signage, logos; high object count; crowds; complex camera; physical interactions; identity preservation. Answer in one short block: what the model may change; what must not change; which references are critical; where drift is likely; what will be checked after. A risk flag does not authorize a creative change.

**Fail conditions.** For each predicted failure write one line decided before generation: "if [X], the shot is wrong" — size, pose, count, direction of movement, emotion, anything the shot cannot survive. Each line must be checkable on a viewed frame or a measurement. They are acceptance criteria for QC; whether any of them also enters the prompt is decided by the model's prompt skill, because naming an unwanted thing can invite it.

### 7. Validation
Check the prompt against every source that exists: camera vs approved camera data; composition vs shot description; character vs references; props vs approved assets; motion vs script and blocking; no new event; no unapproved object; bindings vs the manifest.

- A source that is **not available** → list the check as "not checked: [source missing]" and continue checks that can be completed.
- A **contradiction of a LOCKED fact** → report both sources and isolate the affected decision.
- A **story-critical TBD** → ask before generating.

### 8. Director launch and cost
Prepare a reviewable handoff: exact model/mode, approved settings, references,
duration, output count and quoted cost when available. Director launches manually.
Unknown host settings remain TBD.

### 9. QC
Inspect the actual take. Run `python3 scripts/contact_sheet.py CLIP --out QC_DIR --times 0.5,1.8` from the skill directory for metadata, a labelled contact sheet and frames near requested times. It uses FFmpeg, ffprobe and Pillow. Frame labels report the sampling requests. Use stream timestamps or contiguous playback when timing, motion, or a cut requires finer evidence; a contact sheet is a sample. Check audio perceptually where available. FFprobe provides track metadata, while audio metrics require a tool such as FFmpeg's ebur128 filter. Report what was measured and what was heard.

Check each control domain against its level, then each fail condition from the risk check, then reference carry-over (anything taken from a reference beyond its named role). Temporal failures to look for: identity morphing, geometry breathing, props appearing/disappearing, extra limbs/fingers, texture crawl, light pulsing, speed jumps, camera drift, background mutation. Motion checks: `human-motion-biomechanics`; sport: `sports-action-choreography`; appearance state: `costume-hair-makeup-continuity`; neighbours: `film-continuity`.

### 10. Diagnosis
Classify before revising: identity / camera / geometry / blocking / performance / body motion / prop / light-material / temporal / text / model capability limit. Fix the controlling source first, not the wording by habit.

### 11. One-variable revision
For a diagnostic test change exactly one meaningful variable. State in advance: the variable, the expected result, the success criterion. A production run that changes several variables is not a test and proves no cause. Do not repeat a failed setup without a new reason.

### 12. Escalation after repeated failure
Stop, summarize what was tried, then propose in this order: simplify the action; strengthen references/conditioning; split into smaller beats; build more spatial/motion truth in Blender; make a still master first; composite instead of one-model solutions; redesign the shot only with the user's approval and only if the intent survives.

## Candidate tests (borrowed ideas, not verified in this pipeline)

Treat these as `HYPOTHESIS`, to be run as one-variable tests and kept only if the result supports them:

- Negatives written as the inversions of this shot's own idea (if the rule is "the object stays, the world moves": ban "the object moves", "the world stays still", "the camera follows from outside") instead of a generic ban list. Tension with the observed rule that naming an unwanted object can invite it — test both.
- Numeric handheld character (amplitude, frequency, breath cycle, late reframes) written into the prompt, only for shots whose camera is not baked from previz.
- At a hard cut, the soundscape flips to the new space on the exact frame, with no crossfade.

## Experiment log (existing repository shot/test record)

One row per attempt:
```
| # | model / mode | refs (role) | duration / aspect / res | changed variable | expected | result (timecodes) | verdict | next |
```
Keep the exact prompt of each attempt available (in the reply or a file). When prior attempts exist in past chats, retrieve them before proposing a new test.

## Acceptance

PASS only when each story-critical domain passes independently: identity; camera/spatial truth; action order; performance readability; hero props/text; temporal stability; continuity with neighbouring shots; and no fail condition triggered. Beauty cannot compensate for a failed lock. A partial pass names the usable time range.

## Handoff to post

For an accepted shot note: usable range, compositing/VFX needs, colour match, crop/stabilization, temporal cleanup, sound sync, known residual defects.

## Outputs

Generation plan, source package (with what each reference does and does not supply), risk block with fail conditions, launch handoff, experiment log, QC report with timecodes, diagnosis, next test, accepted-master record, post handoff.

## Constraints

Tool-specific skills specialize execution but never override project canon. Never claim a tool capability or setting without verification. Never replace locked design, camera, identity, composition, blocking, story or approved references for model convenience. Never add an object, character or physical solution without approval.
