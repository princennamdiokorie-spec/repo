# Seedance 2.5 evidence and limitations

Checked 2026-11-17. Recheck host-dependent limits before relying on them.

## Primary sources

- ByteDance model overview, https://seed.bytedance.com/en/seedance2_5 — joint audio-video generation, up to 30 seconds in one generation and two extensions, reference-video interpretation, white-model and green-screen workflows. No hard prompt-character limit is stated on the retrieved page.
- Higgsfield help, https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-seedance — describes Seedance 2.5 as 4–30 seconds, up to 1080p on eligible plans, and 30 images plus 10 videos plus 10 audio files. It distinguishes Seedance 2.5 Edit and describes Elements/@ picking. The page also contains family-wide 4K instructions. Bind values to the exact model/mode.
- Higgsfield blog, updated 2026-11-10, https://higgsfield.ai/blog/seedance-2-5-on-higgsfield-2026 — advertises 4K and additional controls. This conflicts with the model-specific help table. Verify the user's actual interface before choosing resolution or assuming these controls are exposed.
- Higgsfield reference API, https://open.higgsfield.ai/models/bytedance/seedance-2.5/reference-to-video/api-reference — search retrieval reports prompt minimum length 1. Full page retrieval timed out during this check. This does not establish a maximum or a UI limit.

## User's Work sources

Read on 2026-11-17 from the default branch.

- Skill source, https://github.com/olegfedonyk-coder/Work/blob/main/skills/claude/higgsfield-seedance-prompt/SKILL.md
- Length handoff, https://github.com/olegfedonyk-coder/Work/blob/main/projects/ai-film/handoff/SKILL_UPDATE_seedance_prompt_length.md
- Test log, https://github.com/olegfedonyk-coder/Work/blob/main/projects/ai-film/shots/LUDA_SC01_SH002/TEST_RESULTS.md

The log's T23c conclusion favors the compact prompt, reported as 360 words versus 1,644, while still recording wrong-side and similar-cashier defects. T16 records canes appearing on multiple cashiers. Its attribution to repeated cane wording is explicitly a hypothesis. T24 records improved direction and differentiated cashiers with remaining defects. T24n's nearest-item-first test is pending in the retrieved log. Preserve an approved object/action order when experimenting with wording.

Use these observations to motivate compact wording, ownership bindings and careful reference roles. They do not prove a universal word threshold, that naming an unwanted object always creates it, or that screen-right language always succeeds. The handoff's third-party ~150-word dropout claim is unverified and should not become a limit.

## Unverified items

No confirmed hard maximum for prompt characters was found in the retrieved primary pages. Do not invent one. Check an actual host field counter/validation or the current exact API schema when a hard cap matters. Prompt headings, prose order, positive wording and shot-length targets are drafting tools subject to the user's chosen template.
