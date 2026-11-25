# Project instructions

## task-observer

Invoke the `task-observer` skill before the first tool call of each session.

Workspace (pinned): the `task-observer/` folder at the root of this repository,
i.e. the directory that contains this CLAUDE.md. All task-observer paths derive
from it:

- `task-observer/skill-observations/observation-log/` (the log)
- `task-observer/skill-observations/cross-cutting-principles.md`
- `task-observer/skill-updates/` (staging root)
- `task-observer/skill-updates/PENDING.md` (staging manifest)

It is committed to git on purpose, so observations persist across cloud
sessions. Resolve it from the repository root, not from the current working
directory, and never from inside a git worktree under `.claude/worktrees/`.

## Higgsfield

The `higgsfield-generate` skill is installed as a reference (model catalog,
prompt engineering, Marketing Studio). Do not follow its Step 0: do not install
the `higgsfield` CLI (no `curl … | sh`) and do not run `higgsfield auth login`.
Use the connected Higgsfield MCP tools (`mcp__Higgsfield__*`) for discovery and
generation instead, and map any CLI command in the skill to the matching tool.
Show the credit cost and get approval before any paid generation.

## Kendrill Luxury film — director's rules (from the 2026-11-25 handover)

Source of truth: the v4 script doc https://claude.ai/artifact/6RvGwCwauTaL1bTLQbWGmX
(tabs: Script, Asset checklist, Storyboards). Read it with the Claude Docs tools.
Asset job IDs: `designs/kendrill/assets.md`. Older files (v2, v3, runbook) are superseded.

1. Never generate a video without explicit approval. Show the exact prompt,
   settings, references and credit cost first, then wait for a clear "go".
   This includes 480p drafts.
2. Until the director says otherwise: no video generation at all. Image
   generation only after it has been discussed.
3. The director makes most images himself in the Higgsfield web app with
   Unlimited on. Our job: exact prompts, and checking his results.
   Unlimited does not work through the connector; connector generations cost credits.
4. Everything is chauffeur-driven: every moving car shows a chauffeur at the wheel.
5. 9:16 vertical only. 480p drafts first, 720p finals. No 1080p, no landscape.
6. No text generated in clips. All on-screen text is added in the final edit.
7. Real-life references for every location, so places match Lagos.
8. Never copy a real person's likeness for any character.

## remember

Session memory lives in `.remember/` and is committed on purpose for the same
reason. `logs/`, `tmp/` and `config.json` inside it stay untracked.
