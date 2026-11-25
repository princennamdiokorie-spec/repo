---
id: 4
title: "Real reference photos can be imported server-side via media_import_url even when the sandbox network blocks the photo host"
status: open
type: open-source
skill: [higgsfield-generate]
proposes_skill: []
target_file: [CLAUDE.md]
siblings_checked: "none — no skill-families.md registry exists; higgsfield-generate is the only installed Higgsfield skill"
area: "sourcing real-location reference photos for generation"
date: 2026-11-25
session_context: "Autonomous run building Lagos location frames from real photos"
parked_until:
resolved:
resolution:
reference: "designs/kendrill/autonomous-run-ledger.md"
commands_verified: "run: media_import_url on commons.wikimedia.org/wiki/Special:FilePath/<file> — imported 12 Commons photos while direct fetches from the sandbox failed with ENOTFOUND"
next_actor: review
---

**Issue:** The sandbox and the web-fetch helper could not reach commons.wikimedia.org, so the obvious route (download, inspect, upload) failed. The generation service's own URL import fetched the same files server-side, and the imported copies were then downloadable from the service's CDN for inspection.

**Suggested improvement:** Add a line to the project's Higgsfield section: find free-licensed photos with a domain-filtered web search, import them with media_import_url using the Special:FilePath URL, then inspect the imported copy before using it as a reference.

**Principle:** When the sandbox network blocks a source, check whether a connected service can fetch it on its own servers before asking for a network change.
