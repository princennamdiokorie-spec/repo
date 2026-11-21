---
id: 2
title: "Uploaded skills assume claude.ai paths and name sibling skills that are not installed here"
status: open
type: open-source
skill: [seedance-shotlist-html, gpt-image-2-prompt]
proposes_skill: []
target_file: []
siblings_checked: "none: no family registry entry; both checked — seedance-shotlist-html names seedance-single-prompt and seedance-multiref-prompt, gpt-image-2-prompt names image-prompt-generic, none installed"
area: "output path and routing to sibling skills"
date: 2026-11-21
session_context: "installing user-uploaded .skill bundles into .claude/skills in a Claude Code cloud session"
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** seedance-shotlist-html saves to `/mnt/user-data/outputs/shotlist.html`, a claude.ai chat path that does not exist in Claude Code (deliver via the working dir or an Artifact instead). Both skills route the user to sibling skills (seedance-single-prompt, seedance-multiref-prompt, image-prompt-generic) that were not uploaded or installed.

**Suggested improvement:** make the output location environment-neutral ("the session's outputs folder; in Claude Code, the repo or scratchpad, then SendUserFile/Artifact"), and either install the named siblings or reword the Do-NOT lines to not depend on them.

**Principle:** a skill ported between surfaces must not hard-code one surface's file paths, and any skill it routes to by name must be installed alongside it or the routing silently dead-ends.
