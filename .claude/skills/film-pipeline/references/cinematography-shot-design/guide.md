# Cinematography and Shot Design

Translate an approved dramatic intention into visible, shootable decisions. Every shot must have a function; do not add coverage by habit.

## Start from the dramatic beat

For each proposed shot, answer:

- What new information becomes visible?
- What should the viewer feel or anticipate?
- What changes before the cut?
- Why is this shot not redundant with the neighboring shot?

Choose framing, angle, lens, movement, focus, duration, blocking, light, and sound only after defining that function.

## Build the visual progression

- Use shot-size changes to express a change in access, distance, pressure, or recognition.
- Treat camera height and angle as point of view, not decoration.
- Preserve screen direction, eyelines, entrances, exits, prop state, hand actions, and body orientation across cuts.
- Prefer motivated movement. A static camera is valid when the world or performance supplies the change.
- Avoid simultaneous camera and blocking complexity unless both are necessary and independently controllable.
- Design sound bridges and match cuts as exact events with identifiable source, timing, and cut point.

When lens choice matters, describe the intended perspective and working distance as well as an approximate focal length. Do not imply that focal length alone determines the image.

## Shot-plan output

Use a table when planning several shots. Include only fields that help production:

| Field | Purpose |
| --- | --- |
| Shot ID | Stable reference across script, Blender, and generation tests |
| Dramatic function | Why the shot exists |
| Framing/angle | Shot size, height, orientation, and composition |
| Lens/camera | Approximate lens, position, movement, and focus behavior |
| Blocking/action | Exact character, prop, and hand actions |
| Sound/cut | Audio event and transition point |
| Continuity lock | Elements that must not change |
| Success criterion | Observable result required for acceptance |

Do not manufacture precise measurements when the scene has not been inspected. Mark provisional values clearly.

## Blender and generative-video handoff

- Blender is the spatial source of truth for geometry, scale, camera, positions, orientations, trajectories, and timing.
- Appearance references control identity, wardrobe, materials, lighting, and texture; they must not replace approved geometry.
- Seedance synthesizes movement and photorealism but does not design the shot.
- Convert frame-relative directions such as “left” and “right” into unambiguous world, camera-local, or screen-space instructions before implementation.
- For diagnosis, change one meaningful variable per test and state the expected observation and failure criterion in advance.
- Do not use a longer prompt to compensate for a contradictory reference image, camera path, or character pose.

## Project convention: “Люда”

The film's visual arc moves from system to person:

- Early imagery emphasizes repeated checkout geometry, routine, distance, and partial anonymity.
- Mid-scene framing gives increasing attention to Люда's hands, work rhythm, face, and reactions.
- The man may interrupt the routine, but the camera must not turn him into the protagonist.
- The basketball-to-meat transition is a precise movement-and-sound rhyme, not a tragic flashback climax.
- The cane belongs to present-day continuity without an insert or dramatic emphasis.
- The final frontal look makes the lens the position of the next customer. Protect its simplicity; avoid decorative movement that weakens the encounter.

## Review discipline

Classify each statement when ambiguity matters:

- **FACT** — directly visible or measured.
- **HYPOTHESIS** — plausible cause not yet proven.
- **PROPOSAL** — a change recommended for testing or approval.
- **TEST RESULT** — an observed outcome under stated settings.

When a render or generation fails, identify whether the defect comes from shot design, Blender blocking, appearance conversion, prompt interpretation, or synthesis. Do not rebuild an approved checkout scene until evidence shows the geometry or camera is the source of failure.
