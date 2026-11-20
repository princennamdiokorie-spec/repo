# Kendrill Fleet Film — Claude Chat Runbook (free-trial unlimited)

Higgsfield refuses unlimited generations from Claude Code. They work from **Claude chat** (claude.ai or the Claude app) with the Higgsfield connector. Run every generation below there, during the 7-day free trial.

## Setup (once)

1. Open a new Claude chat with the **Higgsfield** connector turned on.
2. Attach two files: this runbook and `kendrill-lagos-fleet-film-v3.md`.
3. Paste the kickoff message below. Then send each step's message, approving results as you go.

### Kickoff message

> I'm producing a 1:30 vertical luxury car-hire ad for Kendrill Luxury in Lagos. The attached v3 script is the brief and the runbook has the steps. Rules for this whole chat: **use my unlimited / free-trial generations on every generation (use_unlim: true)**, and never fall back to credits. If a request isn't covered by unlimited, stop and tell me instead. Show me every result before moving on. Reuse the Higgsfield job IDs listed in the runbook as reference images exactly as given. Start with Step 1.

---

## Images already made (reuse by job ID, no need to regenerate)

| Tag | Job ID |
|---|---|
| `@car_escalade` | 4f8436eb-94f6-453f-9fe6-1da474077b8e |
| `@car_lx600` | 446f2014-cdfa-4f18-beaf-be036929cfd2 |
| `@car_landcruiser` | 242fc9f2-d03e-49cf-b3c9-295c520b0831 |
| `@car_g63` | fa3c2baf-4d4f-4800-a7f4-9704301e56d1 |
| `@car_cullinan` | 8594342f-b00a-45f9-ab44-fa97809ab891 |
| `@car_ghost` | 8d0a4f73-4a74-4d17-b3d6-a88df21d8639 |
| `@car_s580` | 18f2197a-1dce-426c-8f3a-6706cdff309a |
| `@car_corvette` | 2a45db75-6574-46c5-90ac-d09dedefc0cc |
| `@loc_ikoyi_road` | 76ee72e5-0480-4daa-9054-cb3eb9e7ad55 |
| `@loc_eko_boulevard` | 1e27bd58-5885-44ca-b43d-fe0d2543d829 (has a sign; replaced in Step 2) |
| `@loc_link_bridge` | 50fb317c-05e7-40f4-8872-0d7de13b6ba5 |
| `@loc_hotel_driveway` | 93bcefe1-03b0-4664-a458-d8c1cb9df741 |
| `@loc_eko_plaza` | 7c6ad2c4-e66f-43aa-9093-f25ce8488290 |
| `@loc_lagoon_aerial` | b0f9fb71-f0a7-4569-bc7e-55e2d3dba4c9 |

---

## Step 1 — Car sheets with KENDRILL plates (8 images)

> Step 1. For each of the 8 car job IDs in the runbook, make an edited version with GPT Image 2.6 (16:9, 2K, quality high, unlimited), attaching that car's job ID as the reference image, with this prompt: "Keep this exact car, its three views, background and lighting identical. Change only the licence plates, front and rear, in every view: a black plate with white uppercase serif lettering reading KENDRILL, crisp and correctly spelled." For the Ghost, add: "Also make the left front three-quarter view clearly a Rolls-Royce Ghost saloon, matching the centre and right views; not a Phantom." Show all 8 together.

## Step 2 — Eko Atlantic boulevard without the sign (1 image)

> Step 2. Edit job 1e27bd58-5885-44ca-b43d-fe0d2543d829 with GPT Image 2.6 (9:16, 2K, high, unlimited): "Keep this exact scene identical; remove the 'EKO ATLANTIC CITY' sign and any lettering from the building, leaving plain glass and stone."

## Step 3 — Host and chauffeur character sheets

> Step 3. Use the Higgsfield character-sheet workflow, Realism style, with unlimited, for the two characters in the v3 script's Assets section (`@char_host` with her full casting entry, and `@char_chauffeur`). Stop for my approval after each face, then make the outfit flat-lay and the 3-panel sheet.

## Step 4 — Video drafts (480p, all three parts)

> Step 4. Generate Part 1, Part 2 and Part 3 of the v3 script with Seedance 2.5: 30s, 9:16, mode omni_reference, audio on, **draft: true (480p)**, unlimited. Attach as image references the approved Step 1 car sheets, the location job IDs, and (Part 3) the approved host and chauffeur sheets. Use each part's prompt block from the v3 script exactly. If unlimited doesn't cover a 30s or omni_reference draft, tell me which settings it does cover before doing anything.

## Step 5 — Finals

> Step 5. Finalise the approved drafts at 1080p (draft_job_id), unlimited. If the free trial doesn't cover 1080p finals, tell me first.

---

After each step, bring the new job IDs back to the Claude Code session (or paste them here), so the project's `assets.md` stays the single record and the edit (music, captions, end card, cut-downs) can be put together.
