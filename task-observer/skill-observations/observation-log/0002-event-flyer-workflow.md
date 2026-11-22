---
id: 2
title: "Event-flyer production is a repeatable workflow with a per-client taste profile; no skill captures it"
status: open
type: open-source
skill: []
proposes_skill: [event-flyer-design]
target_file: []
siblings_checked: "none — no skill-families.md registry exists; canvas-design and higgsfield-generate each cover one step, not the pipeline"
area: "new skill: event flyer from references to layered deliverables"
date: 2026-11-22
session_context: "Kova Night Club grand opening flyer, kova-flyer/README.md and designs/flyer-preferences.md"
parked_until:
resolved:
resolution:
reference: "kova-flyer/build/ (render.js, export-layers.js, build_psd.py, transplant_nameplate.py); designs/flyer-preferences.md"
commands_verified: "run: build_psd.py flatten check, mean diff 0.40/255 after fixing two isolation bugs; run: transplant_nameplate.py, 2302 ORB inliers"
next_actor: review
---

**Issue:** A full flyer job took one long session of trial and correction: hero title generated on a transparent background, layout and backgrounds built in HTML/CSS and rendered with Playwright, contact details moved and resized four times, palette matched to the client's own post then partly reverted, a nameplate re-lettered with an AI editor and registered back onto the clean asset, then a layered PSD and a native 4K render. Two export bugs cost rebuilds: Chrome still paints SVG filter output under visibility:hidden, and a decoration drawn as ::before vanished from every isolated layer while the overall flatten check still looked fine. The client asked that their taste be learned so the next flyer needs little direction.

**Suggested improvement:** A skill `event-flyer-design` covering: read the client taste profile first; generate cut-out hero assets on transparent; compose in HTML/CSS with measured (not eyeballed) spacing; for text inside rendered art use an AI editor plus feature-registered transplant; export layers with display:none for non-target subtrees and a dedicated layer for pseudo-element decorations; verify the PSD flatten per region, not only the global mean; deliver PNG, native 4K, PSD, and a Canva-editable PDF.

**Principle:** A global average can hide a missing small element: verify layered exports region by region. And when a client asks to be learned, the taste profile must live where every future session loads it, with each preference tied to the pick or correction that produced it.
