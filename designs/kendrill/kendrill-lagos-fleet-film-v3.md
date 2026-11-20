# Kendrill Luxury — Lagos Fleet Film (1:30) · Script v3

Builds on v2 (`kendrill-lagos-fleet-film-v2.md`). v3 works the two reference films into the ad: their camera habits, their realism and their branded plates. It doesn't copy them shot for shot; it uses them to make one story.

**The story: one day with Kendrill in Lagos.** The morning fleet rolls out in Ikoyi (Part 1), the city by afternoon (Part 2), and the chauffeured arrival at golden hour (Part 3). The light moves through the day, so the three parts feel like one film rather than three clips.

---

## What v3 adds

| # | Change | Taken from |
|---|---|---|
| 1 | **Kendrill plates on every car**: a black plate with white uppercase **KENDRILL** lettering, front and rear, on the whole fleet. It's the brand's quiet signature in every shot, the way "AVANTGARDE" runs through Reference 1. | Ref 1 |
| 2 | **Natural, real-camera look**: true-to-life colour, soft natural light, glossy deep blacks on the paint, gentle contrast, a slight handheld feel on the street shots. It replaces v2's "punchy, saturated, lens flares", which neither reference has. | Ref 1 and 2 |
| 3 | **An 8-second opening**: the convoy is already mid-distance in frame 1 (so it hooks), then rolls in calmly and fans into a V (so it feels unhurried, as in the reference). A middle ground between v2's 5s and the reference's 19s. | Ref 1 |
| 4 | **Foreground framing**: an SUV passes close behind an estate wall in the foreground (Part 1); a planter frames the plaza arrival (Part 3). | Ref 1 (wall), Ref 2 (planter) |
| 5 | **Tilted detail shots**: the grille and badge macros are shot at a slight angle, with the camera gliding. | Ref 1 |
| 6 | **Cars rolling across the frame**: the exotic tier passes along a Victoria Island street, seen from pavement level. | Ref 2 |
| 7 | **The car stops huge in frame**: the Cullinan drives straight at the low camera on a city street and stops filling the frame. | Ref 2 |
| 8 | **A plate close-up as the brand moment** (Part 1, 10–12s): the first time the viewer reads "KENDRILL". | Ref 1 |

Everything else from v2 stays: the chauffeured Ghost as hero, the host's lines and WhatsApp call to action, the character sheets, the edit plan, safe zones, captions, cut-downs and the generation order.

---

## Keeping the plates consistent

AI video models often garble text, so the plate is controlled at three levels:

1. **In the references.** Every car reference sheet is regenerated with the KENDRILL plate on it. Image models render text well, and Seedance copies what it sees in the reference.
2. **In the prompts.** Every part repeats one fixed line: *"Every car wears a black licence plate with white uppercase KENDRILL lettering, front and rear."*
3. **Where it's readable.** The plate is only legible where it matters: the plate close-up in Part 1, the Cullinan stopping in frame in Part 2, and the Ghost's arrival in Part 3. In wide and moving shots it's too small to read, so small imperfections don't show.

**Safety net:** if a draft garbles the plate in one of those three readable shots:
- **Plate close-up:** generate it on its own. Make a still of the plate shot first (an image, so the lettering is exact), then animate it with a gentle camera move (Seedance with that still as the start frame).
- **Any other shot:** cover the plate in the edit with a clean KENDRILL plate graphic. On a short shot that's quick.

The 480p drafts will show which, if any, of these are needed before anything is finalised.

**Plate design:** a black plate with white uppercase serif lettering reading **KENDRILL**. Keep it to the one word, because short text survives generation far better than "KENDRILL LUXURY".

---

## Assets

- **Car reference sheets:** regenerate the 8 sheets **with KENDRILL plates**, using the approved sheets as the starting image so the cars stay the same (`assets.md`). The Ghost's front view also gets fixed in this pass.
- **Locations:** as generated (`assets.md`). Redo the Eko Atlantic boulevard without the "EKO ATLANTIC CITY" sign.
- **Characters:** `@char_host` and `@char_chauffeur`, as in v2.

---

## Part 1 (0:00–0:30) — Morning: The Fleet Rolls Out

Settings: Seedance 2.5 · 30s · 9:16 · 1080p · audio ON · `omni_reference` (car sheets, `@loc_ikoyi_road`, `@loc_eko_boulevard`, `@loc_lagoon_aerial`).

```
30-second vertical 9:16 luxury chauffeur-fleet commercial in Lagos, Nigeria, on a soft overcast morning: four gloss-black SUVs roll toward a road-level camera on a tree-lined Ikoyi road and fan into a V, then close details, a car passing behind an estate wall, a lagoon aerial, and the four arriving side by side on an Eko Atlantic boulevard. Real-camera realism, clean frame with no on-screen text.

REFERENCES
@car_escalade @car_lx600 @car_landcruiser @car_g63 — each car's exact body, grille, lights, wheels and plates.
@loc_ikoyi_road @loc_eko_boulevard @loc_lagoon_aerial — the places.

LOOK
Natural real-camera footage. True-to-life colour, soft overcast daylight in Ikoyi, brighter open daylight at Eko Atlantic, glossy deep blacks on the paint, gentle contrast. Wides 24mm at road level; details 85–100mm, shallow depth of field, slight handheld drift.

PLATES
Every car wears a black licence plate with white uppercase KENDRILL lettering, front and rear.

CARS — all gloss black, dark tinted windows
@car_escalade (lead): tall full-size SUV, vertical LED light bars, large crest grille.
@car_lx600: spindle grille, triple-beam headlights.
@car_landcruiser: boxy modern SUV, horizontal LED light bar.
@car_g63: square body, round headlights, vertical-slat grille.

SHOTS
0–8s — FIRST FRAME: camera low on the centre line of the Ikoyi road, 24mm, locked. The lead SUV is already mid-distance, rolling toward the lens at a calm pace, the three others tight behind it. From 3s they fan out behind it into a V; at 7s the lead stops 4 metres from the lens, the V settled behind it.
8–10s — 100mm, camera tilted at a slight angle, gliding slowly across the lead SUV's grille and crest, trees reflected in the chrome.
10–12s — 85mm, slight tilt, slow push-in on the lead SUV's front plate: black with white KENDRILL lettering, crisp and sharp.
12–16s — Camera low behind the top edge of a cream estate wall, the wall filling the bottom third of frame; the square SUV rolls past close behind it, left to right, bougainvillea at frame edge.
16–19s — Ground level 35mm: the boxy SUV's front wheel rolls slowly past the lens.
19–21s — Low rear three-quarter 50mm: the spindle-grille SUV pulls away down the tree tunnel, red taillights and rear KENDRILL plate catching the light.
21–23s — Aerial drone drifting over the Lagos lagoon in morning haze: Ikoyi skyline, the white cable-stayed bridge, small boats.
23–30s — Camera locked at road level in the middle of the wide Eko Atlantic boulevard. The four SUVs roll toward the lens side by side, left to right: square SUV, lead SUV, spindle-grille SUV, boxy SUV. They stop together at 27s, 6 metres away, and hold, engines idling.

SOUND
Native audio only: ambience and engines, no music, no voices. Birds and breeze in Ikoyi, tyres on asphalt growing loud, deep idle as they stop; close engine rumble on the details; wind over water on the aerial; open wind between towers and four engines settling at the end. Each cut changes the ambience.

KEEP CONSISTENT
Opens on the road-level wide with the convoy already in view. Each car matches its reference; only these four cars. Plates read KENDRILL. Ends holding on the four cars side by side.
```

---

## Part 2 (0:30–1:00) — Afternoon: The City

Settings: Seedance 2.5 · 30s · 9:16 · 1080p · audio ON · `omni_reference` (car sheets, `@loc_hotel_driveway`, `@loc_link_bridge`).

```
30-second vertical 9:16 luxury chauffeur-fleet commercial in Lagos, Nigeria, on a bright afternoon turning golden: a Rolls-Royce Cullinan, Rolls-Royce Ghost and Mercedes saloon roll along a Victoria Island street, the Ghost arrives at a hotel entrance, the Cullinan stops filling the frame on a city avenue, a black sports coupe roars over the Lekki–Ikoyi Link Bridge, ending on a rising aerial over Eko Atlantic as the light turns gold. Real-camera realism, clean frame with no on-screen text.

REFERENCES
@car_cullinan @car_ghost @car_s580 @car_corvette — each car's exact body, grille, lights, wheels and plates.
@loc_hotel_driveway @loc_link_bridge — the places.

LOOK
Natural real-camera footage. True-to-life colour, bright clear afternoon light warming toward gold by the end, glossy deep blacks on the paint, gentle contrast. Street shots feel like a phone held low on the pavement, almost still; details 85mm with shallow depth of field.

PLATES
Every car wears a black licence plate with white uppercase KENDRILL lettering, front and rear.

CARS — gloss black, cabins empty
@car_cullinan: tall luxury SUV, chrome temple grille, bonnet ornament.
@car_ghost: long saloon, rear-hinged coach doors, cream leather, starlight headliner.
@car_s580: sleek saloon, slim digital headlights.
@car_corvette: low mid-engine coupe, red brake calipers, quad centre exhausts.

SHOTS
0–4s — FIRST FRAME: phone-style camera low on the pavement of a busy Victoria Island street, 24mm, almost still. The Cullinan, the Ghost and the saloon roll along the far lane from right to left across the frame, one after another, glass office towers behind.
4–9s — Low on the paving of the hotel driveway, 24mm. The Ghost rolls in under the entrance canopy toward the camera and stops close, its side filling the right half of frame; the doorman stands still by the doors.
9–11s — Door height 50mm: the Ghost's rear coach door swings open slowly onto the cream leather seat and starlight headliner. The seat is empty.
11–17s — Camera low and centred on a city avenue lined with tall buildings, 24mm. The Cullinan drives straight toward the lens, headlights on, and stops at 16s so close it fills the frame, its chrome grille and KENDRILL plate sharp.
17–19s — 85mm, slight tilt, slow orbit around the Cullinan's bonnet ornament.
19–26s — Camera low at the edge of the Link Bridge deck, the white cable-stayed pylon behind. The coupe accelerates past the lens right to left at 21s; the camera whip-pans to follow it across the bridge.
26–30s — Aerial drone rising over Eko Atlantic as the light turns golden: glass towers, the sea wall, the ocean, the waterfront plaza below.

SOUND
Native audio only, no music, no voices. Street ambience (traffic, distant horns, footsteps); hotel driveway (a fountain, tyres on paving, the soft click of the coach door); the Cullinan's near-silent arrival; the coupe's V8 rising to a roar and fading across the bridge; high wind and distant ocean on the aerial. Each cut changes the ambience.

KEEP CONSISTENT
Opens on the pavement-level street with the three cars crossing frame. Each car matches its reference; no other cars in close view except ordinary traffic in the far background. Plates read KENDRILL. Light warms through the clip. The doorman stays still in the background. Ends on the rising aerial.
```

---

## Part 3 (1:00–1:30) — Golden Hour: The Arrival

Same as v2 Part 3, with these changes:

- **Add to LOOK:** "Natural real-camera footage, true-to-life colour, golden-hour light." Remove "gentle flares".
- **Add a PLATES line:** "Every car wears a black licence plate with white uppercase KENDRILL lettering, front and rear."
- **Change shot 0–6s to:** "FIRST FRAME: camera locked on the paving 20 cm above the ground, 24mm, a tall planter with tropical leaves at the left edge of frame, the V of parked black cars across the frame with the gap in the centre, ocean and orange sky behind. The black Ghost glides in through the gap toward the lens, its KENDRILL plate catching the light, and stops 5 metres away at 5s, centred in the gap, filling the middle of the frame."
- **Host lines are unchanged:** "Lagos moves fast. Your ride should too." · "From Escalades to Rolls-Royces — chauffeur-driven, on time, every time." · "This is Kendrill Luxury. WhatsApp us to book your ride."

---

## Edit

Unchanged from v2: one music track across all three parts, beat drops on the cuts, the hook caption at 0:00–0:03, the brand lower-third at 0:03–0:06, captions on the host lines, the end card inside the safe zone, and the 15s and 30s cut-downs. The 15s cut-down should include Part 1's plate close-up (10–12s), because it's the clearest brand moment in the fleet section.
