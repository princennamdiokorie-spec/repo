---
id: 2
title: "Code retouch declared done after checking only the edited rectangle; the defect extended beyond it"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: [designs/kendrill/tools/patch_fabric.py]
siblings_checked: "none — no skill-families.md registry exists; no installed skill covers local image retouching"
area: "verifying a pixel-level image fix before reporting it"
date: 2026-11-25
session_context: "Removing an extra jacket pocket flap from an AI character sheet with a local texture-clone script"
parked_until:
resolved:
resolution:
reference: "designs/kendrill/characters/hero-sheet-pocketfix-before-after.jpg"
commands_verified: "run: patch_fabric.py on the sheet with one region (x1221-1263 y467-525) — the director saw the flap still present; a gridded 5x zoom of the whole hip showed the flap ran to y545; a second region fixed it"
next_actor: review
---

**Issue:** The extra pocket flap's extent was estimated from a coarse zoom; the fix covered only its top part and was checked by zooming into the edited rectangle itself, which looked clean. The director looked at the whole garment and saw the leftover band still reading as a second pocket.

**Suggested improvement:** Before reporting a retouch done, inspect the whole object the defect belongs to at a gridded high zoom (measure the defect's full bounds first), and compare the result against the reference count the user cares about (here: one pocket per hip), not only the patched area.

**Principle:** Verify a fix against the property the user will judge (the whole object, at their viewing scale), not against the region you changed; a clean patch can still leave the defect.
