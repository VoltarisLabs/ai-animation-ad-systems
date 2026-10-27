# Ad 24 · "X-Ray" · production plan v1 (what to generate, in what order)

Written 2026-10-08. Steps 2-4 of the 9-step `ugc.mp4` clone workflow. Script: `Ad24_SCRIPT_v1.md` (selected, 12 spoken lines, about 40 s of voice + end card; estimate from the reference's measured pace, not measured audio).

## The look (decided)

| Part | Source | File |
|---|---|---|
| Character | The semi-real homeowner woman (mid-50s, chestnut bob, coral top, navy trousers, white sneakers), 7.36 heads tall | `13_Generated/images/ZackD_3D/ZackD_Woman_reallook_character_sheet_v1_gemini.jpeg` (04:15 sheet) |
| Set | `ugc.mp4`'s studio: flat sky-blue wall + light-blue floor with a cyan grid | `13_Generated/images/ZackD_3D/REF_set_skyblue_gridfloor_empty.png` |
| House, props, backyard | New, in the SAME semi-real render as the woman (not clay) | to generate (below) |
| Animation | `ugc.mp4`'s: drop-ins, walls opening, pill labels, sparkle puffs, grass growing over the grid, slow push-ins, one fast pull-back, end card | measured 2026-10-07 |

`ugc.mp4` frames are a composition guide only. Don't upload them to the image model: they pull the clay look back in.

## What `ugc.mp4` shows, and our version of each shot

| `ugc.mp4` (s) | What it shows | Ad 24 version |
|---|---|---|
| 0-4.7 | Small cottage alone on the grid; the front wall folds open into a dollhouse | Our cottage; an x-ray scan turns the walls see-through |
| 4.7-6.3 | Roof close-up, tiles + hammer drop in | Gutter close-up, a ladder drops in |
| 6.3-8.0 | Porch close-up, peeling paint | Fence close-up, a stack of boards drops in |
| 8.0-13.7 | The man on the grid; tools land on him; the house again; SELLS AS-IS | Her on the grid, loaded; the x-ray house; she faces the house; walls go solid; SELLS AS-IS |
| 13.7-16.0 | Sofa, wardrobe, lamp, box on the grid; frame and plant hop into the box (TAKE) | Same idea with our furniture (TAKE / STAYS) |
| 16.0-17.8 | Calendar, a hand circles a date | Same, her hand, red marker |
| 17.8-26.0 | Loaded again; items vanish in puffs; grass grows from his feet | Same |
| 26.0-35.0 | Backyard: fence, round trees, hammock; end card | Sunny back patio with strawberry pots; she tastes one; end card |

## The house (one house in this ad)

One small **single-storey cottage**, the same type as `ugc.mp4`'s house but our own design and in the semi-real look:
- pale sage-green clapboard walls, white trim, charcoal-grey shingle roof, a red-brick chimney on the right, a white front door in the middle, one window each side, a small front porch with two steps and white posts;
- standing alone on the sky-blue grid set, seen straight from the front, centred, nothing around it (no street, no lawn), like `ugc.mp4`;
- the four problems the script names, each easy to see: the front **gutter** sagging at one end and overflowing with dead leaves; a short white picket **fence** beside the house with one broken board and a gap; an outdoor brass **faucet** on the front wall dripping into a small puddle; **peeling paint** on the porch posts and window trim.

It appears 4 ways: solid (F01), x-ray (F02), gutter close-up (F03-F04), fence close-up (F05-F06). Rooms are only seen through the x-ray: a simple living room (sofa) and kitchen (sink). No full interior rooms are needed. The living-room pieces in line 8 stand on the grid, like `ugc.mp4`.

## Images to generate (9:16, 2K)

**Style kit first (step 4).** Each one is the master for what comes after it.

| # | Image | References to upload | Note |
|---|---|---|---|
| K1 | Woman crops: front, 3/4, side, back, calm face, hand | none (I cut them locally, free) | from the 04:15 sheet |
| K2 | Props sheet on the grid: wooden ladder, stack of new fence boards, red toolbox, paint can, bucket, hammer, cardboard box, framed photo, potted plant, red marker | set plate | all in the woman's render style |
| K3 | Backyard patio, empty: lawn, low wooden fence, two round trees, terracotta pots of strawberry plants with red berries, a small wooden bench, blue sky with soft clouds | none | the reward place, like `ugc.mp4`'s backyard |
| F01 | The house, solid, on the grid | set plate | doubles as the house master |

**Scene frames (step 5).** Every end frame is made from its start frame, so the clip flows.

| Frame | What it shows | Upload (max 3) |
|---|---|---|
| F02 | Same house, same camera: walls and roof see-through, glowing cyan like an x-ray, simple rooms inside; the 4 problems glow orange | F01 |
| F03 | Gutter close-up: sagging gutter full of leaves at the roof edge | F01 |
| F04 | F03 + the ladder leaning on the gutter | F03, K2 |
| F05 | Fence close-up: the broken board and the gap, on the grid floor | F01 |
| F06 | F05 + the stack of new boards beside it | F05, K2 |
| F07 | Her full body on the grid, front, hands empty, slightly worried | K1 front, set plate |
| F08 | Same framing: ladder on her shoulder, boards in her arms, toolbox in her hand | F07, K2 |
| F09 | Closer (push-in): paint can and bucket on top of the boards, knees bent, peeking over the pile, worried brows | F08, K2 |
| F10 | From behind her right shoulder: she stands on the grid, hammer in hand, looking at the solid house a few steps away | K1 back, F01 |
| F11 | Same, her head and shoulders sag | F10 |
| F12 | Living-room pieces on the grid: grey-blue sofa, floor lamp, side table with the framed photo and the plant, open box on the floor | set plate, K2 |
| F13 | Same, the photo and the plant are now in the box | F12 |
| F14 | Wall calendar close-up, blank day squares (no numbers), her hand with the red marker, coral sleeve cuff showing | K1 hand, K2 |
| F15 | Same, one square circled in red | F14 |
| F16 | Same framing as F09, hands empty, arms down, shoulders relaxed, soft closed-mouth smile | F09, K1 front |
| F17 | Same framing, but she stands on grass in the backyard patio (grid and wall gone) | F16, K3 |
| F18 | Wider: she holds a strawberry at her lips, closed-mouth smile, pots around her | F17, K1 3/4 |

That's 20 images: K2, K3, F01-F18.

## Clips (step 6): Kling 3.0, first + last frame, 9:16, sound off, one camera move each

Times are estimates from the script's pace.

| Clip | Voice (s) | Frames | Motion | Length |
|---|---|---|---|---|
| C01 | L1, 0.0-5.0 | F01 → F02 | a glowing scan band sweeps top to bottom and the walls turn see-through; slow push-in | 5 s |
| C02 | "The gutters call for a ladder," 5.0-7.0 | F03 → F04 | the ladder drops in from above and lands leaning; camera still | 3 s |
| C03 | "the fence calls for boards," 7.0-8.8 | F05 → F06 | the boards drop in and stack; camera still | 3 s |
| C04 | "and she answers every call." 8.8-10.6 | F07 → F08 | ladder, boards, toolbox drop onto her one at a time and she catches them | 3 s |
| C05 | L3 + L4, 10.6-14.4 | F08 → F09 | paint can, then bucket land on the pile; knees bend; slow push-in | 4 s |
| C06 | L5, 14.4-16.8 | F02 only | x-ray glow pulses; slow push-in | 3 s |
| C07 | L6, 16.8-19.2 | F10 → F11 | her head and shoulders sag; camera still | 3 s |
| C08 | L7, 19.2-22.4 | C01 played backwards | walls go solid again | free (edit) |
| C09 | "She keeps what she loves, the rest stays," 22.4-25.3 | F12 → F13 | the photo, then the plant, hop into the box | 3 s |
| C10 | "and she circles her closing date." 25.3-27.5 | F14 → F15 | her hand draws the red circle | 3 s |
| C11 | L9, 27.5-30.9 | F09 → F16 | items vanish one by one, arms drop, she exhales and smiles; slight punch-in | 4 s |
| C12 | L10, 30.9-32.7 | F16 → F17 | grass grows out from her feet and the backyard fades in | 3 s |
| C13 | L11, 32.7-37.0 | F17 → F18 | fast pull-back; she picks a strawberry and tastes it | 5 s |
| C14 | L12 + end card, 37.0-42 | F18 only | gentle idle: she chews and smiles, leaves sway | 5 s |

13 paid clips, 47 s in total. Only the part each line needs is used. Every character shot stays at 1x speed, with no cloned frames.

Rules for every clip prompt: her mouth stays closed except for smiles (narrator only), one camera move, nothing appears that isn't in the frames, no text.

## Voice and edit (steps 7-8)

- **Voice:** one ElevenLabs take of the 12 lines. ElevenLabs' policy bans cloning someone's voice without consent (SOP rule), so use a stock voice or a voice we own.
- **Edit (me, free):**
  - headline bar "SHE QUIT FIXING THIS HOUSE" (0-2.5 s);
  - captions in `ugc.mp4`'s style;
  - pill labels: GUTTERS, FENCE, FAUCET, PAINT, SELLS AS-IS, TAKE, STAYS;
  - sparkle puffs, SFX hits, a music bed, the end card (CASH OFFER plus the 4 confirmed terms), "Zero obligation." in yellow;
  - master to -14 LUFS.

The stills are 2K and the clips 1080p (or 720p), so the final is 1080×1920.

## Cost (before any run)

| Item | How many | Each | Total |
|---|---|---|---|
| Images, Kie `nano-banana-pro` 9:16 2K | 20 | 18 credits (measured) | 360 credits ($1.80) |
| Images in your Gemini app | 20 | 0 Kie credits | 0 |
| Clips, Kling 3.0 1080p (pro) | 47 s | 18 credits/s (list price, not measured) | 846 credits ($4.23) |
| Clips, Kling 3.0 720p (std) | 47 s | 14 credits/s (measured on Ad 23) | 658 credits ($3.29) |

All on Kie: 1,206 credits ($6.03) at 1080p, or 1,018 credits ($5.09) at 720p. This excludes redos. Every image and clip needs its own cost line and your typed "go" first. Zack D work stays local; it doesn't go on Airtable.

## Order of work

1. K1 crops (me, free) → K2 props → K3 backyard → F01 house. Check each one before the next.
2. F02-F18, in order, each checked against its prompt and its references.
3. C01-C14, in order; the last frame of each approved clip is checked against the next clip's start frame.
4. Voice → edit → side by side with `ugc.mp4` (name the 3 biggest gaps).
