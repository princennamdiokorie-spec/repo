---
id: 1
title: "Higgsfield unlimited generations are refused from Claude Code; the CLAUDE.md Higgsfield section does not say so"
status: open
type: open-source
skill: [higgsfield-generate]
proposes_skill: []
target_file: [CLAUDE.md]
siblings_checked: "none — no skill-families.md registry exists; higgsfield-generate is the only installed Higgsfield skill"
area: "Higgsfield section of CLAUDE.md; unlimited-allowance offers"
date: 2026-11-20
session_context: "Generating car and location reference images for a video-ad script via the Higgsfield connector"
parked_until:
resolved:
resolution:
reference:
commands_verified: "run: generate_image_batch with use_unlim true from Claude Code — all 8 items rejected: unlimited generations are not available in Claude Code, only Claude chat, Claude Cowork, ChatGPT"
next_actor: review
use_evidence:
  - 2026-11-21 used — quoted credit cost only, no unlimited offer, for a flyer background
---

**Issue:** The user asked whether their Higgsfield unlimited image generations could be used. models_explore reported unlim available false and the connector docs say to send the flag and let the backend decide; the batch submission was then refused for every item because unlimited is not offered from Claude Code at all. The agent had already told the user it could try, and the CLAUDE.md Higgsfield section is silent on this.

**Suggested improvement:** Add one line to the CLAUDE.md Higgsfield section: unlimited generations are unavailable from Claude Code (only Claude chat, Claude Cowork, ChatGPT); when the user wants them, hand over the saved prompts for one of those surfaces, otherwise quote the credit cost.

**Principle:** When an allowance or entitlement depends on the client surface, record the surface restriction where the next session reads it, so the offer is made accurately the first time instead of being discovered by a refused submission.
