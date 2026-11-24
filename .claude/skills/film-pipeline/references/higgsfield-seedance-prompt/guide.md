# Seedance 2.5 Prompt Writer

Turn a script beat, storyboard, previz, reference set, or correction request into a prompt that Seedance 2.5 can execute as a visible, timed audiovisual scene.

Default deliverable: one standalone English prompt in a code block. Honor another language, format, or multiple variants when the user requests it.

## Model and host verification

Distinguish the model's advertised capabilities from the chosen host, mode and account. ByteDance's model page confirms joint audio-video generation, up to 30 seconds, two extensions, reference-video interpretation, white-model control and green-screen editing. These are model capabilities, with availability determined by the execution interface.

Before a launch handoff, use the supplied UI or current host documentation to check duration, reference types/slots, start/end-frame support, audio and output settings for the exact mode. Carry forward verified session settings. A draft prompt can proceed with declared assumptions when interface information is missing. Ask only for a setting that materially changes the requested result. Keep numeric delivery settings in a short handoff outside the visual prompt when applicable.

Read [dated evidence and host caveats](references/evidence.md) when checking limits, quoting model behavior or adapting Work observations. Check again when current product behavior is needed. Neither a word target nor an observed prompt failure establishes a hard character limit.

## Core principle: write what can be rendered

Translate intent into observable direction:

- emotion becomes gaze, breath, posture, facial tension, timing, and gesture;
- pace becomes beat duration, distance crossed, pauses, cuts, and camera speed;
- atmosphere becomes visible light, weather, particles, surface response, and sound;
- continuity becomes stable identity, geometry, screen direction, wardrobe, props, lighting, and action state.

Prefer a few decisive instructions over a dense inventory of adjectives. Use measurable details only when they help the shot. A number is not automatically more controllable than a clear visual relationship.

Before writing, mentally play the whole output from the first frame to the last. Resolve contradictions between the storyboard, references, action, camera path, duration, and requested edit.

## Choose the operation first

### New generation

Describe the complete clip as a self-contained scene. Establish the first frame, action progression, camera behavior, sound, and final frame.

### Continuation

Treat the source video's final visible and audible state as the new first frame. State:

- what is already in motion at the join;
- which identity, geometry, wardrobe, light, prop, camera-axis, and audio states continue;
- the new action only;
- the intended new final frame.

Do not recap the earlier clip as another event. Make the seam continuous unless the user requests a transition or cut. For a longer story, choose separate clips or supported extensions according to the current interface and editing needs. Give every segment a clear handoff frame. Reattach needed identity and scene references for separate generations.

### Video or audiovisual edit

Identify the source asset, the exact target change, where and when it occurs, how it interacts with the scene, and which visible and audible elements stay identical. Describe preservation positively: `all other actors, timing, camera motion, dialogue, lighting, and background remain identical to @video1`.

For local edits, avoid rewriting the whole scene as a new generation. Anchor the unchanged material to the source and spend detail on the changed region.

### Reference-guided generation

Assign one job to each reference. Do not ask several references to control the same property unless their relationship is explicit.

- image: identity, wardrobe, object appearance, location appearance, or target first/last frame;
- video: blocking, motion rhythm, framing, camera language, performance timing, or environmental behavior;
- audio: dialogue delivery, voice, music structure, rhythm, ambience, or synchronization;
- white-model/previz: spatial layout, character paths, eyelines, camera placement, camera path, and timing.

For a video reference, say what to interpret and what to reproduce. Do not assume `use @video1` means literal motion transfer.

## Intake and conflict handling

Use supplied materials before asking questions. Ask only when a missing choice would materially change the result, such as:

- operation: generate, continue, or edit;
- target duration or aspect ratio;
- which asset controls identity versus motion/camera;
- whether a storyboard frame or previz is authoritative when they conflict;
- whether the output is one continuous shot or an edited sequence;
- the exact first or final frame when it is essential to a match.

When references conflict, state the authority order inside the prompt. Example: `@image1 controls the actor's identity and wardrobe; @video1 controls only blocking and camera timing.`

## Reference tags

Use the exact tags the user or host interface provides. If the user has supplied assets without labels and the interface supports prompt tags, provide a proposed upload map by media type and order, using provisional tags such as `@image1`, `@image2`, `@video1`, `@audio1`. Mark these as proposed labels until confirmed. In an interface with an @ picker, bind each mention to its uploaded asset. Preserve user tags including capitalization and spaces.

Define each active reference once and only include references used in this generation:

```text
@image1 — identity and wardrobe reference for Lyuda; match her face, hair, age, yellow cashier shirt, and cane.
@video1 — camera path and checkout geometry only; preserve the overhead direction and timing, not the grey mannequin appearance.
```

Keep appearance prose concise when an image controls identity. Repeat only small or failure-prone details that must survive generation, such as badge text, handedness, product placement, or a distinctive prop.

## Length and revision discipline

Aim for a compact prompt that preserves the approved action, references and dialogue. About 150–400 words is a working target for many reference-guided scenes, with shorter simple shots and longer justified dialogue sequences allowed. Count characters, including spaces, when asked or when the interface has a verified cap. Count only the exact text the user will paste; label how it was counted.

Apply fixes locally, then return one complete updated prompt when requested. Incorporate all accepted corrections. Avoid appending conflicting versions of the same beat. State shared wardrobe attributes per relevant character and bind distinctive props or body features to their owner. Use state wording for stationary objects and event wording for motion. Favor concise positive targets; retain useful exclusions for reference scope and specific recurring failures. Treat Work test observations as local evidence.

## Start frames, character sheets and previz

A start frame can control opening composition and appearance. A character sheet supplies identity, proportions and wardrobe. Bind its subject and intended attributes so the output contains the scene character in the approved pose. A sheet does not prescribe its multi-panel layout for the output.

When using start image plus previz, assign look/first-frame appearance to the image and spatial layout, camera and timing to the previz. Resolve contradictions in the proposed brief before writing. Map visible proxies to real people or objects; retain necessary performance beats while avoiding a full prose retelling of reference motion.

Select references for new angles or entrances by what becomes visible. A character absent from the opening still can enter if appearance and entrance path are supplied. An exit needs an actual path through a stated frame edge and a final off-screen state. Use the smallest sufficient set. A separate still for every action phase is optional.

Choose an end image only when it matches the intended final pose, emotion and action state. Check whether it conflicts with an expression or movement meant to continue. Preserve approved handedness and asymmetry in anatomical terms, then specify what side the camera sees. Use screen-space directions for positions in the frame and distinguish a character's right from screen right. Describe response to an off-screen cue without inventing who or what caused it.

## Prompt architecture

Use only the sections the shot needs. Keep this order so references and spatial intent are established before detail:

```text
TASK
[Generate, continue, or edit; duration and aspect ratio if known.]

ACTIVE REFERENCES
[Each tag and the exact property it controls.]

SCENE AND LOCATION
[Place, time, foreground/midground/background, stable geometry.]

FIRST FRAME / CONTINUATION JOIN
[Composition, positions, orientations, gaze, prop state, active motion, audio state.]

TIMELINE
[Ordered beats or cuts with timing only where timing matters.]

CAMERA AND OPTICS
[Shot size, angle, height, axis, movement, focus behavior, optical character.]

ACTION AND PERFORMANCE
[Visible action, interaction, restrained physical acting, eyelines.]

LIGHTING AND COLOR
[Motivated sources, direction, exposure relationship, material response, grade.]

AUDIO
[Dialogue, voice source, ambience, effects, music, synchronization.]

PHYSICS AND CONTACT
[Weight, inertia, collisions, cloth, hair, fluids, shadows, foot and hand contact.]

FINAL FRAME
[Where the action, camera, gaze, and sound land.]

CONTINUITY / PRESERVE
[Short positive locks for likely failure points or unchanged edit regions.]
```

Do not turn headings into empty boilerplate. A simple shot may need only references, first frame, action, camera, light, audio, and final frame.

## Duration and story design

Use the selected duration deliberately.

- For a short shot, describe one action with a readable beginning and landing.
- For 10–20 seconds, use a small number of motivated beats and leave room for performance.
- For supported 20–30-second clips, establish a beginning, development, and final image; limit competing actions and unnecessary cuts.
- Use exact time ranges for synchronization, match cuts, dialogue cues, reveals, or hard editorial rhythm.
- Otherwise use ordered beats rather than assigning a timestamp to every action.

All timed ranges must fit the requested duration. Allow physical travel, dialogue, camera moves, and reaction pauses enough screen time to occur naturally.

Treat generated cut timing as a target to check against the result. Exact final durations and sync may require editing. Preserve an already chosen prompt template; use the architecture above only as an adaptable default.

### One continuous shot

State `one continuous shot` and describe one uninterrupted camera path. Tie camera movement to spatial landmarks and subject action. Do not accidentally introduce edit language such as `cut to`, a second incompatible lens position, or an impossible teleport between viewpoints.

### Multi-shot sequence

Use explicit `SHOT 1`, `HARD CUT`, or time ranges. For every shot, specify the new framing and preserve identity, geometry, action state, screen direction, light, wardrobe, and sound continuity. Request cuts only when they serve the story.

## Camera and previz translation

Separate subject motion from camera motion. Define:

- starting camera position and height;
- view direction and subject-relative axis;
- framing or field of view when it matters;
- path, speed character, and stabilization;
- focus target and any focus transition;
- end position and end framing.

For white-model or Blender previz, translate grey geometry into explicit semantic roles while preserving the layout:

```text
@video1 controls checkout-island geometry, character paths, camera trajectory, camera height, and timing. Replace the grey proxy figures with the referenced actors and the proxy surfaces with the described supermarket materials. Preserve the overhead camera path and spatial relationships exactly.
```

If the rendered reference disagrees with the storyboard, do not silently combine them. Use the user-selected authority or ask which controls the camera.

Use lens millimeters, field of view, or plain optical language according to the user's workflow. Do not impose a fixed FOV table. Consistency within a shot matters more than a particular notation.

## Performance and interaction

Direct behavior at muscle and contact level when it matters:

- `she glances at the door, holds for half a beat, then rubs the edge of her badge with her thumb`;
- `his fingers close around the paper cup before he lifts it; the cup deforms slightly under his grip`;
- `her eyes stay on the off-screen customer while her shoulders gradually release`.

When directing a performance beat, identify what the character is trying to do and the cue they can actually perceive. Translate the change into one or two actions legible at the shot scale: the hand stops folding a receipt when the character hears their name, then the gaze finds the speaker. A listener can react as soon as the relevant words land. Let the reaction carry into the next beat or cut. For a naturalistic ensemble, vary who notices, when, and how strongly. Use approved recurring habits only when the scene gives them a reason to surface. Preserve the character's vocal identity while adapting delivery when the shot calls for speech.

For stylized anime, specify when graphic signs, deformation or subjective color appear and when the normal design returns. Align voice, body tension and the emotional turn. Preserve the selected medium and stylization when describing skin, motion and physics.

For prop work, state approach, contact, grip, load transfer, manipulation, release, and resulting prop state. Keep hands, feet, and eyelines attached to the intended object or person.

## Audio-video direction

Treat audio as part of the timeline, not an afterthought. Identify visible or off-screen sound sources and synchronize important sounds to actions.

For dialogue, provide the exact line, speaker, delivery, language, and whether lips are visible. Use quotation marks around spoken text. Keep line length realistic for the allotted duration. Preserve room tone and sound bridges across cuts when continuity matters.

For a silent character beat, describe breath or intentional silence when relevant. If music is unwanted, specify needed dialogue, room tone and effects plus a concise music exclusion. Keep dialogue in its requested language and instructions in the requested prompt language.

When an audio reference controls timing, state which visual beats land on its cues. When editing only the picture, positively preserve the source audio unchanged.

## Green-screen editing

When the requested result uses a green-screen source or output:

- identify which element is keyed or retained;
- describe edge-sensitive areas such as hair, translucent fabric, motion blur, reflections, and contact shadows;
- define the replacement background's perspective, camera motion, light direction, exposure, and depth;
- match foreground and background through light spill, shadow, reflections, grain, blur, and atmospheric depth;
- state whether the deliverable should retain a clean green background or present the final composite.

Do not request contradictory outputs such as both a final composite and a pure green plate in one generation unless the interface explicitly supports separate outputs.

## Editing and preservation language

Use positive preservation constraints. Examples:

- `The cashier, customer, conveyor, products, camera movement, timing, and store lighting remain identical to @video1.`
- `Only the blank wall changes into a rain-streaked window; its perspective and reflections follow the existing camera move.`
- `The replacement logo stays fixed to the carton surface and follows its deformation, motion blur, and occlusion.`

Use exclusions only when a positive target cannot express the edit boundary clearly. Do not fill the prompt with generic negative terms.

## Final checks

Before returning a prompt, verify:

- operation and duration are clear;
- the first frame or continuation join is fully specified;
- every reference has one explicit job and every tag is actually used;
- storyboard, previz, and text have an authority order when they differ;
- subject and camera motion are separate and physically compatible;
- timed beats fit the clip length;
- identity, geometry, screen direction, wardrobe, props, lighting, and action state remain continuous;
- dialogue and sound cues fit the action;
- the final frame is intentional and useful for the next cut or extension;
- edit prompts clearly distinguish the changed element from preserved material;
- the prompt contains no unsupported interface settings or model guarantees.

## Output rules

- If the user asks for a prompt, return the prompt—not a lecture about prompting.
- Default to one self-contained English prompt in one code block.
- Keep asset tags exact and do not mention unavailable references.
- Preserve user-supplied wording that must remain verbatim, including dialogue, labels, and required prompt fragments.
- For diagnosis, explain the conflict first and then provide the corrected prompt when requested.
- Never present an unverified heuristic as a guaranteed Seedance 2.5 behavior.
