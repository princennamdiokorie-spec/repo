---
id: 3
title: "New character outfit made as a single view although the project's reference format is a multi-panel sheet"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: [CLAUDE.md]
siblings_checked: "none — no skill-families.md registry exists; the format lives in the project's asset checklist, not a skill"
area: "producing character reference assets"
date: 2026-11-25
session_context: "Making the hero's airport-arrival outfit reference for an AI video ad"
parked_until:
resolved:
resolution:
reference: "designs/kendrill/characters/hero-arrival-sheet-v1.png"
commands_verified: none
next_actor: review
---

**Issue:** The established reference for the hero was a multi-panel sheet (close-up, front, back). Asked for a casual outfit, the agent generated one full-body front image and then offered the back view as a separate paid step. The director pointed out it should have been one multi-panel sheet from the start.

**Suggested improvement:** Add a line to the project instructions: every character outfit reference is one multi-panel sheet (front and back, plus close-up when the face is new) in a single generation, matching the existing sheets.

**Principle:** When a project already has a reference format, every new asset of that kind follows it in one pass; splitting it into separate pieces costs the user extra steps and an extra approval.
