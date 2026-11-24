---
name: film-pipeline
description: "An AI filmmaking workflow for script development, casting, acting, anime expression, production design, Blender previs, Seedance 2.5 video prompts, take review, continuity, editing, music, sound, color, delivery, and handoff. Use for requests such as Film Pipeline, review this take, how should we shoot this, write a Seedance prompt, or fix this cut."
---

# Film Pipeline

Use the table to open the guides relevant to the current task. For a request that spans several stages, apply those guides together and return one coherent result. Resolve supporting file paths relative to the guide that refers to them. Use bundled guides directly.

Reply in English by default. This language rule applies to every bundled guide, including examples or notes written in another language. Follow an explicit language request and keep dialogue, quoted material, filenames, and reference tags as supplied.

## Working rules

- Follow the director's current instruction and approved project decisions. Use the latest available source and identify the file and version when they affect the finding. Flag material conflicts, unknown facts, and working assumptions. Continue work that the available evidence supports.
- Distinguish observations, hypotheses, and proposals. Check geometry, timing, frame counts, and object counts against the source or measurements when precision matters. Report the ranges actually viewed and the audio actually heard. Use consecutive frames to check motion phase across a cut. Treat a contact sheet as a sample.
- Keep one approved master per asset or sequence. Record reference roles, priority, versions, and tags where they affect the result. Approved previs controls geometry and movement, and the character sheet controls identity. Mark proposals that require the director's creative approval.
- Use **Seedance 2.5** for video generation. Select the mode for the task and verify its available settings in the relevant interface. Use the references needed for the action. Keep supplied tags verbatim. Default to `@image1`, `@video1`, and `@audio1` when proposing tags. Use an explicit tag such as `@audio` when requested. Give one self-contained prompt when asked for the full prompt. Write prompt instructions in English by default and retain the requested dialogue language.
- For a diagnostic retry, choose the smallest useful change and state how success would be observed. The director approves the take and launches generation. Report only inspections and measurements actually performed.

## Guides

| Task | Guide |
| --- | --- |
| Screenplay, conflict, turns, and subtext | [Screenwriting](references/screenwriting-dramaturgy/guide.md) |
| Acting, reaction, blocking, and camera for performance | [Acting direction](references/ai-film-acting-direction/guide.md) |
| Stylized emotion, voice, and body language in anime | [Anime emotion staging](references/anime-emotion-staging/guide.md) |
| Casting, identity, and character sheets | [Casting](references/casting-direction/guide.md) |
| Composition, materials, and props | [Production design](references/film-production-design/guide.md) |
| Shot size, angle, lighting, and coverage | [Cinematography](references/cinematography-shot-design/guide.md) |
| Camera paths, character–prop contact, and previs checks | [Camera shot design](references/camera-shot-design/guide.md), [prop interaction](references/character-prop-motion/guide.md), [previs review](references/previz-shot-review/guide.md) |
| Shot preparation, references, acceptance, and take diagnosis | [AI film production](references/ai-film-production/guide.md) |
| Video prompts, extension, editing, and lip sync | [Seedance 2.5](references/higgsfield-seedance-prompt/guide.md) |
| Motion phase, take selection, cuts, and rhythm | [Editing](references/editing-rhythm/guide.md), [continuity](references/film-continuity/guide.md) |
| Score, Foley, ambience, and mix | [Film music](references/film-music-genre-composer/guide.md), [sound design](references/sound-design/guide.md), [mixing](references/sound-mixing-mastering/guide.md) |
| Color matching, master checks, and delivery | [Color grading](references/color-grade-matching/guide.md), [delivery](references/finishing-delivery/guide.md) |
| Status, decisions, and files for the next collaborator | [Handoff](references/production-handoff/guide.md) |

For an acting or reaction beat in anime, open both the acting direction and anime emotion staging guides. Tie the actor's objective to body language, voice, framing, and the timing of any graphic accent. When asked for a ready-to-use video prompt, also open the Seedance 2.5 guide and incorporate the chosen behavior and timing in one complete prompt.

For a short request such as “prompt” in an established video-generation conversation, open Seedance 2.5 and retain accepted revisions. For a cut on action, apply editing and continuity before drafting the prompt. For a generation failure, start with the actual take and open the guide closest to the first observable problem.
