# Kendrill Luxury — Asset Registry (v4)

Higgsfield job IDs, from the 2026-11-25 handover. The v4 script doc is the source of truth for prompts and status:
https://claude.ai/artifact/6RvGwCwauTaL1bTLQbWGmX

## Car sheets — 16:9, three views, gloss black, black KENDRILL plates

| Car | Job ID | Status |
|---|---|---|
| Cadillac Escalade | d923c693-1d09-4760-9068-6115a160673e | Plates checked ✓ |
| Mercedes G63 | 30a56c73-bf23-48fc-b34e-de95d4e7691c | Plates checked ✓ |
| Lexus LX600 | 5852fe56-990f-44b6-888d-fcf68703f3b3 | Plates checked ✓ |
| Jetour T2 | 710306cb-55a2-4058-97ff-1665397c328d | Approved by director |
| Rolls-Royce Ghost | b2d526c0-2235-4042-bef8-df3dc77d0f9b | Plates not yet checked |
| Rolls-Royce Cullinan | 69cfe77f-5331-4959-97f9-ea4bb56b596d | Plates not yet checked |
| Mercedes S580 | 73adb5a8-deac-4bf4-93f5-718860b6abff | Plates not yet checked |
| Ferrari SF90 (red) | 11ac39c6-0515-403d-8e04-7ac1db496f2a | Not in the film yet; colour to check |

Not used: Land Cruiser/Prado aa13908b-89c0-4758-910a-dffe0f740aff · Corvette 3f18ecc5-77bf-4c64-897e-f6f693d86466 · black SF90 da3636a7-9d0e-401c-b43c-1c3b25a7cfe3.

Pre-plate originals: Escalade 4f8436eb-94f6-453f-9fe6-1da474077b8e · LX600 446f2014-cdfa-4f18-beaf-be036929cfd2 · Land Cruiser 242fc9f2-d03e-49cf-b3c9-295c520b0831 · G63 fa3c2baf-4d4f-4800-a7f4-9704301e56d1 · Cullinan 8594342f-b00a-45f9-ab44-fa97809ab891 · Ghost 8d0a4f73-4a74-4d17-b3d6-a88df21d8639 · S580 18f2197a-1dce-426c-8f3a-6706cdff309a · Corvette 2a45db75-6574-46c5-90ac-d09dedefc0cc.

## Characters

| Asset | Job / file | Status |
|---|---|---|
| Hero face (Soul Cinema) | hf_20261124_135842_458eb8ca-3f19-4ba7-8b02-02f6fac51e02 | Approved |
| Hero three-panel sheet, suit (Nano Banana Pro) | source job 2e8efd43-e480-4190-b057-b2e9806ceaa3 → fixed locally: `characters/hero-sheet-suit-v1-pocketfix.png` | Extra ticket pocket removed in code (`tools/patch_fabric.py`, region x1221–1263 y467–525); awaiting director approval |
| Hero arrival outfit, night outfit, details (watch/button, shoe) | — | To make |
| Girlfriend / host | — | To make; voice to be fixed by reference or recording + lip sync |
| Chauffeurs 1–3 | — | To make; same uniform, clearly different faces |
| Friends 1–2 | — | To make; one outfit all day |
| Ghost interior | — | To make |

## Locations (v3 images, mostly being replaced by real-photo-based frames)

Ikoyi road 76ee72e5-0480-4daa-9054-cb3eb9e7ad55 · Eko boulevard 1e27bd58-5885-44ca-b43d-fe0d2543d829 · Link Bridge 50fb317c-05e7-40f4-8872-0d7de13b6ba5 (**wrong pylon — replace**) · hotel driveway 93bcefe1-03b0-4664-a458-d8c1cb9df741 · Eko plaza 7c6ad2c4-e66f-43aa-9093-f25ce8488290 · lagoon aerial b0f9fb71-f0a7-4569-bc7e-55e2d3dba4c9.

The real Lekki–Ikoyi Link Bridge: one grey concrete pylon splitting into two prongs at the top, octagonal base, white cables fanning to one side, black-and-white chequered median, blue banners on lamp posts.

## Video clips

| Clip | Job ID | Status |
|---|---|---|
| Bridge convoy multi-shot 30s draft | eaabf1ba-8323-488d-90f1-29986f567034 | **Keep 0–6s** (Cadillac crest 0–2s, G-Wagon headlight 2–4s, Escalade wheel 4–6s); rest rejected |
| Ikoyi Part 1 30s draft | a9b90331-d4bf-4fc5-a1f7-438c3c252fb9 | Dropped (proved 30s multi-shot works) |
| Grille test 4s | b7266e59-1447-40a6-a9ab-7a948a625f4f | Dropped |
| Dark opening test 8s | 380433b0-c54c-4033-bfbd-bf2750dd22b0 | Rejected |
| T-junction 30s draft | 6c3ab641-60f3-4104-b59c-5cba57c11ae1 | Dropped (never reviewed) |

## v4 clip plan

| Clip | Covers | Length |
|---|---|---|
| A Bridge opener | 0:00–0:08 | 4s kept + new 8s convoy (6 cars, locked order, single file, ~45° drone) |
| B1 Airport run + landing | 0:08–0:14 | 6s |
| B2 Arrivals + service ritual + montage 2 | 0:14–0:29 | 15s (start from an approved kerb still) |
| C Banana Island | 0:29–0:36 | 7s, ends on the door only |
| D Tower | 0:36–1:04 | 28s, starts on edited Clip C end frame |
| E Night pickup + dinner | 1:04–1:20 | 16s, starts on edited Clip D end frame |
| F Club + host | 1:20–1:38 | 18s, host line 1:25–1:33 |

Balance at handover: 2,659.01 credits (Ultra). Prices: Nano Banana Pro image 2 credits; Seedance 2.5 omni_reference 9:16 — 480p draft 3 cr/s, 720p 7 cr/s.
