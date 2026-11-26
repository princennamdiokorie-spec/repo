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
| Rolls-Royce Ghost | b2d526c0-2235-4042-bef8-df3dc77d0f9b | Plates checked ✓ (2026-11-25) |
| Rolls-Royce Cullinan | 69cfe77f-5331-4959-97f9-ea4bb56b596d | Plates checked ✓ (2026-11-25) |
| Mercedes S580 | 73adb5a8-deac-4bf4-93f5-718860b6abff | Plates checked ✓ (2026-11-25) |
| Ferrari SF90 (red) | 11ac39c6-0515-403d-8e04-7ac1db496f2a | Colour ✓ Rosso Corsa red, plates ✓; not in the film yet |

Not used: Land Cruiser/Prado aa13908b-89c0-4758-910a-dffe0f740aff · Corvette 3f18ecc5-77bf-4c64-897e-f6f693d86466 · black SF90 da3636a7-9d0e-401c-b43c-1c3b25a7cfe3.

Pre-plate originals: Escalade 4f8436eb-94f6-453f-9fe6-1da474077b8e · LX600 446f2014-cdfa-4f18-beaf-be036929cfd2 · Land Cruiser 242fc9f2-d03e-49cf-b3c9-295c520b0831 · G63 fa3c2baf-4d4f-4800-a7f4-9704301e56d1 · Cullinan 8594342f-b00a-45f9-ab44-fa97809ab891 · Ghost 8d0a4f73-4a74-4d17-b3d6-a88df21d8639 · S580 18f2197a-1dce-426c-8f3a-6706cdff309a · Corvette 2a45db75-6574-46c5-90ac-d09dedefc0cc.

## Characters

| Asset | Job / file | Status |
|---|---|---|
| Hero face (Soul Cinema) | hf_20261124_135842_458eb8ca-3f19-4ba7-8b02-02f6fac51e02 | Approved |
| Hero three-panel sheet, suit (Nano Banana Pro) | source job 2e8efd43-e480-4190-b057-b2e9806ceaa3 → fixed locally: `characters/hero-sheet-suit-v1-pocketfix.png` | Extra ticket pocket removed in code (`tools/patch_fabric.py`, regions x1221–1263 y467–525 and x1213–1264 y512–544); awaiting director approval |
| Hero arrival outfit, full body (Nano Banana Pro, 2:3) | df50fc48-5f2f-45d4-a173-cab50960f677 · `characters/hero-arrival-outfit-v1.png` | Awaiting director approval |
| Hero arrival outfit, two-panel sheet front+back (Nano Banana Pro, 16:9) | 19bbb172-d858-49cd-8b88-9311dae3ed3e · `characters/hero-arrival-sheet-v1.png` | Awaiting director approval — use this as the arrival reference |
| Hero night outfit, two-panel sheet front+back (Nano Banana Pro, made at 9:16) | b5d073e6-546f-461c-b757-d9353ab87d49 · `characters/hero-night-sheet-v1.png` | Checked ✓ (jacket buttoned, not open); awaiting director approval |
| Hero details (watch/button, shoe) | — | To make |
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

## Autonomous run, 2026-11-25 — all checked by Claude, awaiting director approval

### Supporting cast — Soul Cinema close-up → Nano Banana Pro three-panel sheet (16:9)

| Character | Close-up (Soul Cinema) | Sheet (Nano Banana Pro) | File |
|---|---|---|---|
| Girlfriend / host | 33722e90-a6c6-49a2-a620-36e93e1da054 | 73440d65-36ba-49a6-b061-518223c9c4dc | `characters/girlfriend-sheet-v1.png` |
| Chauffeur 1 (Ghost, hero) | 1398d4e5-9159-436e-944e-3b63a769e217 | 4aa5d8cd-f972-4d7b-acb3-c0fd95112652 | `characters/chauffeur1-sheet-v1.png` |
| Chauffeur 2 (Escalade, Friend 1) | 6f36f14b-177a-4669-bb62-a7d176745a5b | 2ef46bff-b415-46aa-9ca0-0b68795e67ea | `characters/chauffeur2-sheet-v1.png` |
| Chauffeur 3 (Escalade, Friend 2) | f0023148-5105-4ff6-8121-d9dbe075980e | 1618ef98-3574-483d-a16b-88863621f384 | `characters/chauffeur3-sheet-v1.png` |
| Friend 1 (olive blazer) | ed5736ac-46d5-43ce-a4a9-aa255463dfc2 | e1a5b9f9-d904-4c36-b064-a74fb0fb101e | `characters/friend1-sheet-v1.png` |
| Friend 2 (black blazer) | 316210b2-acca-4a04-9c52-74c386eb578a | 24746b62-29f0-4417-b2ec-b84182cd6ba2 | `characters/friend2-sheet-v1.png` |

Unused close-up takes: 912e2cd1 (girlfriend), 2e048354 (chauffeur), d76762cc (chauffeur), 50737e79 (chauffeur), 2e201542 (friend 1), edfb5411 (friend 2). All 12 on `characters/cast-closeup-options.jpg`.

### Locations — Nano Banana Pro 9:16, each built from a real photo (Wikimedia Commons, imported into Higgsfield)

| Location | Frame job | Real photo used (Higgsfield media ID ← Commons file) | File |
|---|---|---|---|
| Lekki–Ikoyi Link Bridge, day | a6873abc-5be1-4b9f-9e15-6756c20a2662 | 22f14775 ← Lekki_Ikoyi_Link_Bridge.jpg | `locations/bridge_day-v1.jpg` |
| Lekki–Ikoyi Link Bridge, night | 2a84a2d9-6f02-4299-a0d0-e4bd0d933052 | 22f14775 + 1674e6ad ← Lekki_link_bridge_at_night.jpg | `locations/bridge_night-v1.jpg` |
| MMIA arrivals kerb | 1a097bb1-fece-4b2f-a2b6-02f18bbd0b39 | e972e95b ← MMIA_T2_and_garage.png (new international terminal) | `locations/airport_kerb-v1.jpg` |
| MMIA runway, jet landing | 5d4fc8d8-84ec-4241-aa01-df8083fe5698 | 248053fa ← MMIA_Intl_Terminal_2019.jpg (control tower) | `locations/runway-v1.jpg` |
| Third Mainland Bridge | 4023abba-1fcc-4167-ae63-6f1fbebf8d22 | ddd8a42f ← Long_view_of_Third_Mainland_Bridge_from_Makoko.jpg | `locations/tmb-v1.jpg` |
| Banana Island mansion, gate | 373efe69-eb09-435f-a4d1-efcf7ec2f13c | 7b681103 ← Banana_Island_Lagos.jpg (panorama) | `locations/mansion_gate-v1.jpg` |
| Banana Island mansion, aerial | f5e5804b-2f39-4b17-82da-5ced673e2443 | gate frame + 7b681103 | `locations/mansion_aerial-v1.jpg` |
| Victoria Island tower (Civic Centre Towers), kerb | f3761d65-df4d-4efa-b298-9942bd932fbf (emblem removed; original c226fad7) | f86f067b + 6a7be98f ← Civic Towers photos | `locations/tower_kerb-v1.jpg` |
| Victoria Island tower, aerial | 7950cafc-d68f-4f04-bb82-255bc52850f6 | kerb frame + 6a7be98f | `locations/tower_aerial-v1.jpg` |
| Waterfront restaurant, night (VI lagoon, Civic Centre Towers across the water) | 722b7efd-3e85-4d97-addb-629d27a6d8ff | 6a7be98f | `locations/restaurant-v1.jpg` |
| Club entrance, night (Eko Atlantic towers behind) | af6c3ec0-1ed1-4319-85ce-5c684317c61f | 780b4706 ← Eko_Atlantic_(Lagos)_Skyline.jpg | `locations/club-v1.jpg` |

### Interior and details

| Asset | Job | File |
|---|---|---|
| Rolls-Royce Ghost rear cabin (16:9), from a real Ghost cabin photo (3e4021bc ← Rolls-Royce_Ghost_II_Mandarin_Navy_Blue_(4).jpg) | b3eae01d-815a-4360-a99e-ca2900bfe2f0 | `details/ghost-interior-v1.jpg` |
| Hero shoe stepping onto paving | 3203ddfd-14b1-4878-aa48-41a88a6f698e | `details/hero-shoe-v1.jpg` |
| Hero hands buttoning jacket + watch | 52d8e5ea-002f-4832-b7a1-533f465b090e (retry; first try f4f0c3a5 failed) | pending |

## Storyboards

| Clip | Job | File | Status |
|---|---|---|---|
| A · Bridge opener v2 (Nano Banana Pro) | edb4a9d1-1fcb-4d04-b38c-9e7651c3401f | `storyboards/clipA-storyboard-v2.png` | Panels 1–3 pass (Cadillac crest, G63 with chauffeur, Escalade wheel with Cadillac cap). Panel 4: side-on Escalade with chauffeur and correct pylon, but it drives right to left and only one car shows. Panel 5 fails: an extra wide panel was added, and the panels show 8–11 cars in two lanes instead of six in single file |
| A · Bridge opener v1 (5 panels, 0:00–0:08) | 1c19928e-dd0a-463d-82a7-0293d717f240 | `storyboards/clipA-storyboard-v1.png` | Fails checks: panel 3 wheel has a Mercedes hub (should be Escalade); panel 4 convoy comes head-on instead of passing side-on; panel 5 shows five cars, not six, and travels up-frame, not left to right |

**Model note (2026-11-26):** all autonomous-run images were submitted as `nano_banana_pro` (Nano Banana Pro) ✓. Higgsfield's job status reports Nano Banana Pro under the internal name `nano_banana_2`, while the catalogue model `nano_banana_2` is Nano Banana 2, reported as `nano_banana_flash`. Always submit `nano_banana_pro`. Only the Clip A storyboard v1 (1c19928e) was made on the wrong model (Nano Banana 2).
