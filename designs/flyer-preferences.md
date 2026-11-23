# Flyer preferences: what this client likes

Read this before designing any flyer, poster or event graphic. It is built from
real choices and corrections, each tagged with where it came from, so a new
concept can be built right the first time with little direction. Update it
whenever a choice or correction teaches something new; keep the evidence tag.

Evidence key: **[picked]** chosen from options · **[fixed]** a correction they
gave · **[made]** an edit they made themselves · **[asked]** an explicit request.

## Overall look

- **Bold, glowing, saturated scenes, not dark and moody.** When the scene was
  darkened to match a reference post, the answer was "way darker… I don't want
  it darker like this." Keep strong neon glow and visible light. [fixed]
- **Chrome/silver 3D metal with electric-blue neon** is the house style for
  hero titles (a riveted, angular 3D plaque with a nameplate, like the Space Benin
  "GRAND OPENING" title). [asked] [picked]
- **Of four directions** (chrome gate with white contact bar, velvet-curtain
  arch, spotlight stage, neon octagon portal), **the portal won**: a glowing
  tunnel of neon rings converging behind the title. [picked]
- **One blue across the whole flyer.** The background glow must match the
  title's own neon blue; sample the title's neon and reuse it. [fixed]
- **Match the brand's own posts** for detail fonts and accent colours when the
  client shares them, but keep the glow and brightness of our design. [asked] [fixed]

## Layout (portrait 4:5, 1080×1350 base)

- Logo top centre, **with breathing room above it** (they moved it about 46 px
  lower than my first placement). [made]
- Title plaque dominant in the upper middle, full width. [picked]
- Date block split by a thin neon vertical line: huge chrome range on the left
  ("10–12" + spaced "DECEMBER" under it), day list + time on the right. [picked]
- Day names (THU/FRI/SAT) on a **dark navy panel with thin silver dividers**
  between rows. [made]
- **Venue line (pin + club name + address) centred exactly halfway** between
  the date block and the contact line, measured, not eyeballed. [fixed]
- **Contact info is minimal:** one slim line at the very bottom (phone ·
  email · Instagram/Snapchat handle) under a hairline rule. Never a big bar or
  big block. "Too bulky… needs to be minimal." [fixed]
- Secondary rows stay **small and in proportion**. Making a row big "blew it
  out of proportion." [fixed]

## Type

- Detail text: **wide geometric sans, all caps, generously tracked, soft silver**
  (#c5c5c6). Montserrat 500–600 matched their brand's post. [asked]
- Separators: **thin blue vertical bars "|"**, not dots. [asked]
- Big numbers and time: condensed heavy display (Anton) in chrome gradient. [picked]

## Accuracy and wording

- **Brand names exactly as the client writes them**: "KOVA NIGHT CLUB" is two
  words. Check the client's own posts for spelling. [fixed]
- Don't invent extras (DJ names, taglines, city); ask. Small functional labels
  like "DOORS" and "RESERVATIONS" were accepted. [asked]

## Process they expect

- **Default: give them the prompt to run themselves in Higgsfield** (they have
  free credits there that this connection can't use): "next time give me the
  prompt." Only generate through the connection when they ask. [asked]
- **Show the credit cost and get approval before any paid generation**, with
  options for 1 or 2 variations. [asked]
- When they say "use code", build backgrounds and layout in HTML/CSS, not AI. [asked]
- **Text inside rendered 3D art: edit it with an AI image editor (Nano Banana),
  not code-drawn lettering.** The code version "didn't work." Paste the edited
  region back onto the clean transparent asset. [fixed]
- Generate cut-out assets on a transparent (or flat grey) background, with clean
  edges and no fringe. [asked]
- A pick means "refine this", **not final**. They say when it's final. Don't
  build extras (like a story version) until asked. [fixed]
- Final deliverables: PNG, **4K** render, **layered PSD** (named layers),
  Canva-editable version on request. [asked]

## Concept 2: copy a reference layout in our colours

- They bring a third-party flyer and ask to **copy its layout and 3D type
  effect, re-coloured to Kova's chrome + electric blue**, keeping elements they
  name (here: the product bottles and the round light-bulb marquee behind the
  title). [asked]
- Badge ring text chosen: **"GRAND OPENING. 3 NIGHTS."** (event-focused) over
  the brand slogan. [picked]
- Product shots from other brands go in **unbranded** (no logos or labels) unless
  they say otherwise. [asked]

## Concept 3: recolour a scene and swap the people

- When editing a reference scene, **clear the area where the title will go**:
  remove objects there and leave only background effects (glow, haze,
  sparkles), not new elements. [fixed]
- People in their scenes: **beautiful Black women**, same poses as the reference. [asked]
- People must look **super realistic, like a real photograph**: real skin texture, pores, real hair and hands. Painted or airbrushed "AI look" is rejected ("it looks too AI and I don't like it"). Put photographic cues in every people prompt. [fixed]
- Recolour gold scenes to Kova chrome silver + electric blue, with no gold left. [asked]
- Models wear **the flyer's palette** (chrome silver, electric blue), lit with electric-blue rim light, not teal. Poses: **sultry and confident**, e.g. fingertip touching the lip, preferred over a reaching hand. [fixed]
- 3D titles: **depth yes, sideways turn no.** A title rotated about 15° was "too sideways… we can't use it." Keep titles front-facing (a slight low angle is fine) and get depth from extrusion and layering. When they ask for options, give several distinct prompts. [fixed] [asked]
- **"Make it better" means a NEW design**, not a polished copy. Don't attach the old image as a reference or say "keep the format" unless they ask; that reproduced the same design and frustrated them. [fixed]
- **Titles need a flat, level top edge** with clear space above them for the logo. Tall script loops or ascenders (the G and d of "Grand") crashing into the logo must be fixed in the title prompt itself. On the flyer, measure the title's real top edge and keep a fixed gap below the logo. [fixed]
- Write the image prompt tightly and show it before spending credits:
  "I wouldn't want to waste my Higgsfield credits." [asked]

## Concept 4: replicate a reference flyer in Kova branding

- Approach that worked: GPT Image 2.6 with the reference flyer attached and a
  "same layout, recolour and rebrand" prompt. All text, small print included,
  rendered correctly. [picked]
- Background: **subtle blurred club-party scene** (crowd, haze, lights, bokeh in
  navy/blue). **No repeating logo-pattern wallpaper**: "irrelevant." [fixed]
- Use the **real Kova logo** (its symbol can stand in for the A in GRAND as a
  crest). Never an invented emblem. [asked]

## Club name

- **The club's name is "Kova Lifestyle"** (it replaces "Kova Night Club" on flyers). [fixed]
- **Before editing, confirm which file is meant.** Pick the version most recently delivered to them (usually the latest 4K in `kova-upscales/`). If a name like "the portal one" could mean two files, ask in one line. I once edited the wrong, older flyer: "This is the version you are working on." [fixed]
- **When reopening any older flyer, update it to the current wording first.** Every "Kova Night Club" becomes "Kova Lifestyle" (use `kova-flyer/title/grand-opening-title-B.png`, not the `-night-club` plaque), without being asked. Reusing an old version with the old name was corrected: "Are you forgetting that we made the change?" [fixed]
- A logo symbol used inside a title must match the neighbouring letters: same
  chrome palette (sampled from the letters), cap height and baseline. Done in code. [asked]

## Self-check before sending (always)

- **Inspect every render for alignment and spacing before sending**: even gaps
  between stacked text blocks, the title block grouped tightly under the top
  line, everything centred, and no overlaps with sparklers or other elements.
  When a request says to move blocks (e.g. "the title goes up"), verify that it
  actually happened. "You're supposed to be looking at them… does it align?" [fixed]
- When a model fails a precise layout edit, do it in code on the clean version. [asked]
- **Standing command: assess every flyer thoroughly before sending.** Zoom in on
  every logo and compare it side by side with the source file. AI refinement
  passes redraw logos (the Kova symbol came back with doubled loops), so always
  restore the exact logo in code. Check label colours and paper, any visible patch
  edges, every line of text, and alignment. [fixed]

## Concept 5: simple luxury (client's new direction)

- After all the busy concepts, the client asked for **something simpler but
  luxurious**: dark navy, one glowing hero object in the centre, an elegant serif
  title, and small widely-spaced details (reference: a gold sunburst-and-diamond
  "opening celebration" flyer). Recoloured to Kova chrome + electric blue. [asked]
- Built in code with the real Kova symbol as the hero; three hero treatments
  offered (radiance rays, art-deco arch, spotlight on a reflective floor). [asked]

## Past work

- Kova Night Club grand opening, Dec 10–12: final = `kova-flyer/flyer4-portal*`
  (see `kova-flyer/README.md`).
