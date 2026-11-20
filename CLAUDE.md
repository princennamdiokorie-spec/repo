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

## remember

Session memory lives in `.remember/` and is committed on purpose for the same
reason. `logs/`, `tmp/` and `config.json` inside it stay untracked.
