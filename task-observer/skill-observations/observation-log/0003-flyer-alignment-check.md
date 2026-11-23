---
id: 3
title: "Flyers sent without a measured alignment check despite a saved rule; client corrected centring and spacing again"
status: open
type: open-source
skill: []
proposes_skill: [event-flyer-design]
target_file: [designs/flyer-preferences.md]
siblings_checked: "none — no skill-families.md registry exists; extends observation 0002's proposed skill"
area: "pre-delivery self-check for flyer layout"
date: 2026-11-23
session_context: "Kova monochrome Noir flyer with the client's chrome title (kova-mono/)"
parked_until:
resolved:
resolution:
reference: "kova-mono/build/check_alignment.py; designs/flyer-preferences.md 'Self-check before sending'"
commands_verified: "run: check_alignment.py on kova-mono-1-raw-B.png, all rows within 2px of centre after fixing a 9px title offset"
next_actor: review
---

**Issue:** The preferences file already said "inspect every render for alignment and spacing before sending", and the client had corrected alignment before. A flyer was still sent with the hero title about 9 px off centre (its thin swash tip faded at the smaller size, so the visible ink was lopsided) and uneven gaps; the client had to repeat the command. The checks that were run looked at the image by eye, not by measurement.

**Suggested improvement:** Make a measured check part of the delivery step: run check_alignment.py (row centres vs flyer centre, gaps between rows) on every flyer before it is sent, and centre hero art on its rendered visible ink, not its image box. This is the second occurrence of the same rule failing, so the fix is a tool that prints numbers, not a louder sentence.

**Principle:** A visual rule that has failed twice needs a measuring instrument in the delivery path; centre artwork on what is visible after scaling, because thin details fade and shift the optical centre.
