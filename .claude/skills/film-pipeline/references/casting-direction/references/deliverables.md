# Reusable production deliverables

Use only sections the request needs. Source every locked assertion.

## Authority register

| Source ID | Path and revision | Approval | Governs | Conflict |
| --- | --- | --- | --- | --- |

Resolve conflicting sources by citing both and requesting an authorized decision. Keep the last confirmed version while a proposal is pending.

## Character and age sheet

| Field | Specification | Status | Source |
| --- | --- | --- | --- |
| Character ID, period, age | | | |
| Dramatic task and behavior | | | |
| Invariant identity | | | |
| Permitted age changes | | | |
| Face, hair, scale | | | |
| Voice and gesture | | | |
| Wardrobe and visible text | | | |
| Props and contact | | | |
| Visibility by shot | | | |

Create one sheet per age version, linked to the same identity ID. Distinguish actor from role and actual from apparent age if established.

## Reference manifest

| ID | Source/path | View and period | Use | Approval | Allowed edits | Limitations |
| --- | --- | --- | --- | --- | --- | --- |

Approval states: approved, candidate, rejected, unavailable. Preserve provenance. Verify consent or license before passing a real person's likeness into generation. A generated reconstruction is not a documentary photo.

## Continuity ledger

| Scene/shot/time | Identity/age | Entry state | Action/contact | Exit state | Matching shot | Evidence/status |
| --- | --- | --- | --- | --- | --- | --- |

For prop actions, record holder, hand, orientation, placement, and handoff point. Record changes in wardrobe and hair and their causes. Mark deliberately hidden facts instead of guessing.

## Generation handoff block

```text
CHARACTER ID / AGE VERSION / SHOT:
AUTHORITY: approved reference IDs and versions; screenplay/decision; previs/camera
IDENTITY LOCK: invariant face, scale, distinguishing features
PERMITTED TRANSFORMATION: age, period, wardrobe, light, expression
PERFORMANCE: objective, gesture, gaze, timed action
SPATIAL TRUTH: camera, positions, contact, blocking from previs
APPEARANCE: approved look references; proxy materials are placeholders
CONTINUITY: incoming state -> action -> outgoing state; adjacent shots
CHECK FRAMES: first, reveal, turn, contact, last; failure criteria
OPEN ITEMS: proposed, unknown, conflict; no implicit approval
```

Use actual frame numbers or timecodes when known.

## Release gate

- Locked facts have sources; references have approval states.
- Age versions preserve identity invariants and justify differences.
- Needed angles, body scale, and expressive views are available or marked missing.
- Costume, text, accessories, contacts, and entry/exit states match adjacent shots.
- The handoff preserves previs geometry and approved appearance authority.
- Conflicts and proposals are visible before labeling an asset final.
