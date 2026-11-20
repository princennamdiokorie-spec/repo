# Kendrill Luxury — Lagos Fleet Film (1:30) · Script v2

Revision of the Nov 11, 2026 script by @MOE. Same structure (3 Seedance 2.5 parts of 30s, 9:16, 1080p, native audio on, music and end card in the edit). What changed and why comes first; the full prompts follow.

---

## What changed and why

| # | Change | Why |
|---|---|---|
| 1 | **The host now steps out of the back of the Rolls-Royce Ghost, opened by a chauffeur, instead of driving the Ferrari SF90 herself.** The SF90 becomes an optional variant. | The ad promises "chauffeur-driven", but she was driving herself, so the picture contradicted the line. The SF90 is also not on the price list, so the hero car was one nobody can book. The Ghost is bookable, its coach doors are iconic, and Part 2 already opens its door with "nobody gets out". Part 3 now pays that off. |
| 2 | **A real hook in the first 3 seconds.** The convoy is already close and moving at the lens from the first frame (it used to start as a dot and take 9s to arrive), plus a caption over the opening, added in the edit. | On Reels and TikTok, people decide in about 1–2 seconds. A car far away rolling slowly for 9s is a scroll-past. A hook has three slots (visual, spoken line, caption). The spoken slot stays empty until 1:15, so the caption has to carry the claim. |
| 3 | **The brand shows up early.** A small "Kendrill Luxury" lower-third at 0:03–0:06, added in the edit. | In v1 the name was first heard at 1:23, and most viewers of a 1:30 ad never get there. |
| 4 | **The call to action matches the end card.** "Book your ride today" → **"WhatsApp us to book your ride."** | The end card shows a WhatsApp number. The spoken line should tell people what to do with it. |
| 5 | **Give each car a reference sheet, generated from its written description, before any video** (one image per car, attached in `omni_reference`). | v1 described the cars in text only, separately in each part, so the Part 3 fleet would not match Parts 1–2. Generating one approved image per car first and attaching it everywhere keeps every car identical across all 3 parts. It is the same idea as a character sheet, applied to the cars. |
| 6 | **Brand names in the prompts are a rejection risk.** Higgsfield's own guide says prompts with trademarks can be stopped by its IP filter (`ip_detected`). v2 leads each car description with its reference tag and a plain description; model names stay as secondary detail. A fallback wording for the spoken line is included. | Without this, a whole 30s generation could be rejected, or the badges come out garbled. |
| 7 | **Tighter prompts, and timings rounded to whole seconds.** I removed repeated rules (the KEEP CONSISTENT lists restated the LOOK and CARS sections) and replaced "no X" with positive wording ("blank plates" rather than "no letters or numbers"). | Higgsfield's and the video skill's prompting guides both say long prompts make models lose focus, and that models follow positive wording better. Exact 0.1s timings are rarely hit anyway, and pretending otherwise makes review harder. |
| 8 | **The host gets a full character sheet**, not one image on grey: a face, an outfit flat-lay, then a 3-panel front / back / portrait sheet (the Higgsfield character-sheet workflow, Realism style). | One front-facing photo gives the model nothing for her walk, her profile or her back when she steps out of the car. The sheet is what keeps her identical across every shot. |
| 9 | **Sound-off and safe zones.** Burn in captions for the host's lines. Place the end card inside the safe band (see Edit). | Most feed viewers watch muted. In v1 the end card sat in the "open sky at the top", which is exactly where the TikTok and Reels interface covers the frame. |
| 10 | **15s and 30s cut-downs from the same footage**, at no extra generation cost. | 1:30 is long for paid social. Run the short cuts as ads and use the full film organically and on the website. |

Kept from v1, because they were already right: ground-level camera and close passes, macro details, no on-screen text in the generations, logo and contact details added in the edit, one music track across all parts, cuts timed to the music.

**Two things to check before release:**
- **"On time, every time" is an absolute claim.** Only keep it if Kendrill can stand behind it. A softer option is "always on time".
- **Nigeria may require approval before the ad runs.** Paid ads there generally need pre-approval from ARCON (the advertising regulator). Worth confirming with whoever places the media.

---

## Assets to prepare

**Fleet reference sheets (generated from the descriptions).** Every car is **gloss black with dark tinted windows and blank plates**. For each car, generate one 16:9 sheet showing front three-quarter, side profile and rear three-quarter on a neutral grey studio background, from the car's description in the parts below. Approve each sheet before any video. Names:
`@car_escalade` `@car_lx600` `@car_landcruiser` `@car_g63` `@car_cullinan` `@car_ghost` `@car_s580` `@car_corvette` (and `@car_sf90`, in red, only if you use the SF90 variant).

**Characters**
- `@char_host`: a 3-panel character sheet built with the Higgsfield **character-sheet** workflow, **Realism** style. Casting entry:
  - Name: Host. Role: brand presenter, poised corporate lead.
  - Age: 28. Ethnicity/origin: Nigerian (Yoruba or Igbo, your call); Skin tone: natural dark brown; Eye colour: dark brown.
  - Hair colour: black; Hair length: long; Hair texture: relaxed; Hair styling: sleek low bun.
  - Build: slim, tall. Base outfit: tailored ivory pantsuit, black silk shell top, gold stud earrings, slim black heels.
  - Steps: face (approve) → outfit flat-lay (approve) → 3-panel sheet (approve). Attach the approved sheet in Part 3.
- `@char_chauffeur` (Part 3): Nigerian man, about 40, close-cropped hair, clean-shaven, black two-piece suit, white shirt, black tie, white gloves. He is background talent, so one approved face plus a sheet is enough. It keeps him consistent through the door-opening shot.

**Optional:** `@ref_convoy` (reference video 1), used only for camera position and how the convoy moves (Part 1, as in v1).

The Kendrill logo is still never given to Seedance; it goes on in the edit.

---

## Part 1 (0:00–0:30) — The Fleet Arrives

Settings: Seedance 2.5 · 30s · 9:16 · 1080p · audio ON · `omni_reference` (car references, plus `@ref_convoy` if used).

```
30-second vertical 9:16 luxury car commercial in Lagos, Nigeria. Four gloss-black luxury SUVs charge toward a road-level camera on a tree-lined Ikoyi road and fan into a V, then macro details, a lagoon aerial, and the four arriving side by side on an Eko Atlantic boulevard. Real-world filmmaking, clean frame with no on-screen text.

REFERENCES
@car_escalade @car_lx600 @car_landcruiser @car_g63 — each car's exact body, grille, lights and wheels. Ignore their backgrounds.
@ref_convoy (if attached) — only the camera position (lens on the road surface, on the centre line, locked off) and how the convoy fans into a V. Ignore its location and any text.

LOOK
Clean modern digital cinema. Deep blacks, punchy contrast, rich saturated colour, crisp and clear. Bright overcast morning in Ikoyi with glossy reflections on black paint; hard clear sunlight at Eko Atlantic. Wides 24mm at road level; details 85–100mm macro, shallow depth of field.

CARS — all gloss black, dark tinted windows, blank black plates
@car_escalade (lead): tall full-size SUV, vertical LED light bars, large crest grille.
@car_lx600: spindle grille, triple-beam headlights.
@car_landcruiser: boxy modern SUV, horizontal LED light bar.
@car_g63: square body, round headlights, vertical-slat grille.

SHOTS
0–5s — FIRST FRAME: camera locked on the asphalt, lens 15 cm above the road on the centre line, 24mm. Ikoyi road under arching almond and palm trees, cream estate walls with pink bougainvillea. The lead SUV is already 25 metres away and closing fast, headlights on, three SUVs tight behind it. At 3s it brakes and stops 4 metres from the lens, filling the lower frame, while the other three swing out into a V behind it.
5–7s — Macro 100mm: the lead SUV's grille, camera sliding left to right, tree reflections moving across the chrome.
7–9s — Road level 35mm: the square SUV's front wheel rolls past the lens left to right, brake caliper visible.
9–11s — 85mm slow push-in: the spindle-grille SUV's headlights switch on from dark to full.
11–14s — Door height 50mm: the boxy SUV glides past right to left at walking pace, palm reflections sliding across its doors.
14–17s — Low rear three-quarter 50mm: the lead SUV pulls away, tall red taillights glowing down the tree tunnel.
17–20s — Aerial drone drifting forward over the Lagos lagoon at morning: Ikoyi skyline, the white cable-stayed Lekki–Ikoyi Link Bridge, small boats.
20–30s — Camera locked at road level, 24mm, centre of a wide empty Eko Atlantic boulevard: glass towers, palm median, blue sky. The four SUVs roll toward the lens side by side, left to right: square SUV, lead SUV, spindle-grille SUV, boxy SUV. They stop together at 27s, 6 metres away, and the frame holds on them, engines idling.

SOUND
Native audio only: ambience and engines, no music, no voices. Birds and breeze in Ikoyi, tyres on asphalt growing loud, deep engine idle as they stop; close engine rumble on the macros, a soft click as the headlights switch on; wind over water on the aerial; open wind between towers and four engines settling into idle at the end. Each cut changes the ambience.

KEEP CONSISTENT
Opens on the road-level wide with the convoy already close. Each car matches its reference in every shot; only these four cars. Ikoyi = trees, walls, bougainvillea; Eko Atlantic = glass towers, wide boulevard, palms. Ends holding on the four cars side by side.
```

---

## Part 2 (0:30–1:00) — The Exotics

Settings: Seedance 2.5 · 30s · 9:16 · 1080p · audio ON · `omni_reference` (car references). In v1 this part used `t2v` with no references.

```
30-second vertical 9:16 luxury car commercial in Lagos, Nigeria at golden hour: a black Rolls-Royce Cullinan glides over the Lekki–Ikoyi Link Bridge, a Rolls-Royce Ghost and a Mercedes sedan arrive at the Eko Hotel driveway, a black sports coupe roars down an Eko Atlantic boulevard, ending on a rising aerial over Eko Atlantic at sunset. Real-world filmmaking, clean frame with no on-screen text.

REFERENCES
@car_cullinan @car_ghost @car_s580 @car_corvette — each car's exact body, grille, lights and wheels. Ignore their backgrounds.

LOOK
Clean modern digital cinema. Warm low golden-hour sun, long shadows, gentle flares, deep blacks, rich saturated colour, crisp and clear. Wides 24mm at ground level; details 85mm, shallow depth of field.

CARS — gloss black, blank plates, cabins empty except where stated
@car_cullinan: tall luxury SUV, chrome temple grille, bonnet ornament.
@car_ghost: long saloon, rear-hinged coach doors, cream leather, starlight headliner.
@car_s580: sleek saloon, slim digital headlights.
@car_corvette: low mid-engine coupe, red brake calipers, quad centre exhausts.

SHOTS
0–7s — FIRST FRAME: camera locked low at the edge of the Link Bridge deck, 24mm, the white cable-stayed pylon and fanned cables rising behind, sun low on the horizon. The Cullinan glides toward the lens and passes close on the right at 5s, sunset sliding across its paint.
7–9s — Macro 85mm, slow 45° orbit around the bonnet ornament, sun flaring behind it.
9–16s — Phone-style camera low on the paving of the Eko Hotel & Suites driveway, 24mm, almost still. Under the entrance canopy the Ghost rolls in from the far end, the saloon behind it. The Ghost stops close to the lens at 15s, its side filling the right half of frame. A doorman in dark uniform stands still by the doors.
16–18s — Door height 50mm: the Ghost's rear coach door swings open slowly onto the cream leather seat and starlight headliner. The seat is empty.
18–20s — 85mm: the saloon's front wheel turns as it creeps forward; its headlight glows brighter.
20–28s — Camera low at the side of a wide Eko Atlantic boulevard, 24mm, sun low behind the towers. The coupe accelerates hard past the lens right to left at 23s; the camera whip-pans to follow it down the boulevard, calipers and exhausts catching the light.
28–30s — Aerial drone rising slowly over Eko Atlantic at sunset: glass towers, the sea wall, the ocean glowing orange, the waterfront plaza below.

SOUND
Native audio only, no music, no voices. Wind across the bridge, faint water, the Cullinan's near-silent hum and soft tyres; hotel driveway ambience (distant traffic, a fountain, tyres on paving, the soft click of the coach door, a quiet engine); the coupe's V8 rising to a loud roar and fading; high wind and distant ocean on the aerial. Each cut changes the ambience.

KEEP CONSISTENT
Opens on the bridge wide with the Cullinan approaching. Each car matches its reference; no other cars in close view. Light grows warmer toward the sunset aerial. The doorman stays in the background, still. Ends on the rising aerial.
```

---

## Part 3 (1:00–1:30) — The Ghost and the Host

Settings: Seedance 2.5 · 30s · 9:16 · 1080p · audio ON · `omni_reference` with `@char_host`, `@char_chauffeur`, `@car_ghost` and the other fleet references.

Host lines (about 10 seconds, Nigerian English, "Kendrill" pronounced KEN-drill):
- "Lagos moves fast. Your ride should too."
- "From Escalades to Rolls-Royces — chauffeur-driven, on time, every time."
  - Fallback if the IP filter rejects brand names: "From city SUVs to the finest saloons — chauffeur-driven, on time, every time."
- "This is Kendrill Luxury. WhatsApp us to book your ride."

```
30-second vertical 9:16 luxury car commercial in Lagos, Nigeria at golden hour: on the Eko Atlantic waterfront plaza a black Rolls-Royce Ghost glides into the centre of a parked black fleet, a uniformed chauffeur opens its rear coach door, a poised Nigerian businesswoman steps out, walks to camera and delivers a short call to action, then the camera rises to a wide of the plaza. Real-world filmmaking, clean frame with no on-screen text.

REFERENCES
@char_host — the host: face, skin tone, hair and outfit exactly as the sheet. Ignore its background.
@char_chauffeur — the chauffeur: face and uniform exactly as the sheet.
@car_ghost and the fleet references — each car exactly as its reference.

LOOK
Clean modern digital cinema. Warm low golden-hour sun from screen left, soft rim light on her hair and shoulders, gentle flares, deep blacks, rich saturated colour. Wides 24mm at ground level; her shots 35–50mm, shallow depth of field.

THE HOST
Nigerian woman, 28, natural dark-brown skin, sleek low bun, tailored ivory pantsuit over a black silk shell top, gold studs, slim black heels. Poised, warm, deliberate. Polished Nigerian English accent, mid-pace, a small confident smile between lines, eyes on the lens whenever she speaks.

THE PLAZA — fixed for the whole clip
Wide light-stone paving, the sea wall and the Atlantic behind, glass towers at the far edges. Six gloss-black cars parked in a wide V facing camera with an open gap in the centre, left to right: G63, LX600, Cullinan, [gap], S580, Escalade, Land Cruiser. Parked cars stay still. Blank plates.

SHOTS
0–6s — FIRST FRAME: camera locked on the paving, lens 20 cm above the ground, 24mm, the V spread across the frame, ocean and orange sky behind. The black Ghost enters through the gap and glides toward the lens, stopping 6 metres away, centred in the gap, at 5s.
6–9s — Low 35mm beside the Ghost's rear door: the chauffeur in a black suit and white gloves steps into frame and swings the rear coach door open; a slim black heel steps down onto the stone.
9–12s — Medium 35mm, slightly low: the host rises from the rear seat and stands tall; the chauffeur closes the door behind her and stands back. She buttons her blazer at 11s.
12–15s — She walks toward camera at a confident pace, the camera dollying back at her speed, the Ghost and fleet softly out of focus behind. At 14.5s she stops waist-up, centred, eyes on the lens.
15–26s — Same shot, no cut, a very slow push-in from waist-up to chest-up that keeps moving through the lines. 15–17.5s, calm, a slight smile: "Lagos moves fast. Your ride should too." 18–22s, warm, an open-hand gesture toward the fleet: "From Escalades to Rolls-Royces — chauffeur-driven, on time, every time." 22.5–26s, direct, the smile widening: "This is Kendrill Luxury. WhatsApp us to book your ride."
26–30s — Same shot: a small nod, she steps out of frame to her left at 26.5s; the camera cranes up and back to a high wide of the plaza (the Ghost in the centre of the black V, the chauffeur beside it, ocean and sunset behind) and holds still from 28.5s.

SOUND
Native audio, no music. Waves on the sea wall, open wind, the Ghost's near-silent arrival; the soft click and sweep of the coach door, a heel on stone; her heels on paving. Her voice: clean, close, dry studio-quality dialogue, microphone out of frame. Each line spoken exactly once, nothing added. 26–30s: waves and wind only.

KEEP CONSISTENT
Host and chauffeur match their sheets in every shot. Eyes on the lens for every line. The camera keeps moving through 15–26s. Parked cars stay still in the same V order; the Ghost sits in the centre gap. Ends on the still high wide with calm sky in the upper third.
```

**SF90 variant (only if the SF90 is added to the price list):** use v1's Part 3, but have the host step out of the **passenger** side with a chauffeur at the wheel, so the "chauffeur-driven" line stays true. Attach `@car_sf90`.

---

## Edit, sound and delivery

**Edit**
- **Stitching:** stitch the parts with hard cuts at 0:30 and 1:00.
- **Music:** one instrumental across all three parts, as in v1: cinematic Afro-house with a light amapiano log drum, 118–122 BPM, with a beat drop on each cut. Bake it in for paid ads. For organic posts, consider attaching a trending sound in the app instead. Duck the music under the host (1:15–1:26) and fade out over the final 0.8s.

**Text added in the edit** (all inside the safe band, 180px in from each side, y = 220–1420 on 1080×1920; never in the bottom 500px)
- **Hook caption, 0:00–0:03.** Pick one; it complements the picture rather than describing it:
  - "Your driver is already outside."
  - "Lagos's black-car fleet, on call."
  - "Chauffeur-driven. Anywhere in Lagos."
- **Brand lower-third, 0:03–0:06:** a small "KENDRILL LUXURY" wordmark.
- **Captions** for the three host lines (1:15–1:26).
- **End card, 1:28.5–1:30:** the exact Kendrill logo, "WhatsApp 08108742714" and "@kendrillluxury", placed in the upper-middle of the safe band (around y = 300–800), over the calm sky.

**Cut-downs (same footage, no extra credits)**
- **15s:** Part 1 0–5s (the convoy fanning into a V) → Part 2 16–18s (coach door opens) → Part 3 6–9s (door, heel) → Part 3 22.5–26s (call-to-action line) → end card.
- **30s:** Part 1 0–5s → Part 1 20–27s (four abreast) → Part 2 0–7s (bridge) → Part 3 0–9s (Ghost arrival, door) → Part 3 15–26s (all lines) → end card.

**Generation order and cost** (prices from v1's table; I'll confirm live prices before anything is generated)
1. Character sheets: host, then chauffeur (and car sheets if there are no photos). Image credits only.
2. A 480p draft of each part: 90 credits per part, 270 for all three.
3. Review the drafts. Finalise only the approved takes at 1080p: 480 credits per part, 1,440 for all three.

**Optional, for more control:** split Parts 1 and 2 into two 15s clips each (no more than 4 shots per clip). Fewer shots per generation means the model hits the shot list more reliably. The total running time stays the same.
