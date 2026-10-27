# Ad 36 "The Photo": script v1 (game look)

**Status (2026-10-27):** current. The user picked this one out of three versions ("Too Much House", "The Photo", "The Hum") and picked the game look for it. Waiting on J's OK on the topic. Nothing generated.

**Situation:** Bev's insurer drops her after a satellite photo of her old maple leaning on the roof. Every insurer she calls asks about the roof; a new roof plus a tree crew is more than her savings. She asks for a cash offer; the house sells as-is; her next chapter is a small house with open sky over the roof and a maple that fits in a pot.

**Process:** the `/gta-style` skill (`01_Skills_and_SOPs/Flow_Animated_Story_Ads/slash_commands/gta-style/SKILL.md`), Ad 32 v3's graphics (the same lock Ad 35 uses: `10_Video_Builds/Ad35_GTA_Dez_StuckInPark/plan/02_GRAPHICS_LOCK_from_Ad32v3.md`), and the global rule that no shot is longer than 1.0 s.

## Landscape fact (sell-fear part 1)

- Spoken: "Insurers check roofs from the sky."
- Source, read live 2026-10-27: Insurance Journal, 2026-05-04, "Another State, Tennessee, Warns Insurers About the Proper Use of Drone Images". Tennessee "has joined a few other states in urging insurers to be careful" about aerial imagery used in "claims and nonrenewal decisions"; the article names Alabama's and West Virginia's bulletins too. Also Kentucky Bulletin 2026-01 (2026-03-11, read in the AAIS compliance alert, not on the Kentucky site): satellite and aerial images in cancellations, nonrenewals and claim denials.
- Source line on screen (plain text, no masthead, no figure): `INSURERS USE AERIAL PHOTOS IN NON-RENEWALS · INSURANCE JOURNAL, MAY 4, 2026`
- **No Ohio source yet.** A search found Ohio House Bill 652 (Jan 2026: nonrenewal notice from 30 to 60 days), but ohiohouse.gov and legislature.ohio.gov refused the connection twice on 2026-10-27, so it is unread and not used.

## Script

```text
[OPEN A]   PAIN   Bev's insurance dropped her. A satellite photo caught her maple.
[payload]  PAIN   Insurers check roofs from the sky.
[payload]  PAIN   The maple hugs her roof, rent-free.
[OPEN B]   PAIN   Every insurer she calls asks about the roof.
[payload]  PAIN   New roof? Tree crew? Her savings said no.
[OPEN C]   PAIN   Every storm, Bev watches the maple, not the TV.
[payload]  PAIN   The maple watches back.
[CLOSE C]  PATH   Bev asked for a cash offer. The house sells as-is. The maple stays.
[payload]  PATH   Took what mattered. Left the rest.
[CLOSE B]  DEST   Now Bev only calls her garden club.
[payload]  DEST   Storm night? Bev watched the whole movie.
[CLOSE A]  DEST   Another satellite photo. Bev's in this one, waving.
[payload]  DEST   Her new maple fits in a pot.
[CTA]      PATH   Seen your roof from the sky? Ask for a cash offer. No obligation.
```

Measured by script (`count_tags.py`; as-is = 1 word, rent-free = 2): 113 words. PAIN 52 (46.0%), PLANE 0 (0.0%), PATH 32 (28.3%), DEST 29 (25.7%). Inside the cold budget in `11_Psychological_Hooks/sell-fear.md` (PAIN 40-50, PLANE 10 or less, PATH 20+, DEST 25+). The fees and the closing date are on the end card only.
Voice length, estimated from words per minute: 41.91 s at Ad 32 v3's 162.2 wpm (first word at 0.11 s), plus a 1.50 s end-card tail = 43.41 s. The line times below come from that estimate; re-time everything from the real voice file's word times.

Loops: Open A (satellite photo) closes in Close A ("Another satellite photo"); Open B (calls) closes in Close B ("only calls her garden club"); Open C (the maple in the storm) closes in Close C ("The maple stays") and its payload ("Storm night? ... the whole movie").

**The hook:** frame 0 is the problem object plus one physical action with no words: from above, the maple's big branch sweeps across the shingles and a red target box snaps onto it. The narrator names Bev and her loss by word 4 (about 1.3 s, estimate), the way the account's lead ads do ("Ray's losing a piece of his house every month.").

| Test | Line 1 | Close A |
|---|---|---|
| MAIN | Bev's insurance dropped her. A satellite photo caught her maple. | Another satellite photo. Bev's in this one, waving. |
| CHALLENGER (strategist) | Bev's maple hugged her roof. A satellite saw. Insurance said goodbye. | Same |

Test: one ad per ad set, equal budget; read the 3-second view rate after 1,531 impressions per arm or more (enough to tell 24.2% from 20.0% at 80% power), then link CTR against 3.7%.

## Claim check (claims registry read 2026-10-27, Section 1 only)

| Line | Status |
|---|---|
| "The house sells as-is." | Section 1 wording (neutral verb, no actor) |
| "Took what mattered. Left the rest." | Section 1 ("Take what matters. Leave the rest."), past tense, same promise |
| "Ask for a cash offer. No obligation." | Section 1 |
| End card: SELLS AS-IS · NO COMMISSION · NO CLOSING COSTS · YOU PICK THE CLOSING DATE | Section 1 |
| "Bev's insurance dropped her." / "Every insurer she calls asks about the roof." | Story events, no claim about the business. Reworded after the J-rules review so nothing says no insurer will cover the house (that would turn as-is into the unconfirmed "any situation") and nothing says one photo is enough to drop a home (the source says images should not be the only information) |
| "Insurers check roofs from the sky." | Landscape fact, sourced above, no figure |

Not in the ad: "we buy", any company name, numbers, prices, speed, "any condition", guarantees, competitor names, urgency. The letter in shot 2 is plain white with no insurer name or logo; NON-RENEWAL is stamped on in the edit.

## Duplicate check (2026-10-27)

Grep of the made ads' Meta text, Ads 2x-3x scripts, lyrics, the Flow examples and the team's Rosa, Ray and Irene transcripts:
- Insurance appears only as a carrying cost (Ad 20, Rosa); no ad is about a non-renewal.
- "maple" appears only in an unused Ad 25 draft (`old/OLD_Ad25_SCRIPT_v2_RoofShookLoose.md`); "satellite" only in Ad 31's camera plan; the name Bev nowhere.
- Changed after the reviews: "as-is, X and all" (Ad 25 "ceiling and all", Ad 32 "cracks and all") and "X included" (Ad 35) are not used; pie (Ad 25), "slept right through" (Ad 27 v5) and a knot that looks like an eye (Ad 35's porch-light eye) are out.
- The roof is a common condition (Ads 25, 27, 32 and Rosa's appraiser), so here the thing the photo flags is the maple, and the roof never leaks.
- 4-gram check against 49 files: only registry wording and its joins.

## HUD (edit only; from the Ad 32 v3 lock; text inside y 285-1248, never over a face; narrator only, no music bed)

| Element | Ad 36 version |
|---|---|
| Target box (this ad's own device) | A red square that snaps onto the maple from above in shot 1 with a camera-shutter sound; it comes back on "Insurers check roofs" (green boxes on the neighbours' roofs, Bev's red) and at Close A on the new house, red to green as she waves |
| Minimap | Bev's house icon with a small red tree on it; red on the pain beats, green on "sells as-is", gold at MISSION COMPLETE |
| Meter | "PEACE" label + 10 segments. Drains on "dropped", "roof", "said no", "watches back"; refills on "cash offer", "as-is", "rest", "garden club"; gold when full. (Not "COVERAGE": refilling it would read as the business giving insurance) |
| Mission pill | "MISSION: STAY INSURED" → "MISSION FAILED" (red, on "said no") → "NEW MISSION: CASH OFFER" (amber, on "cash offer") → "MISSION COMPLETE" (gold, on "pot") |
| Name-card freeze | Shot 5, 0.76 s: BEV / DROPPED BY INSURANCE |
| Toasts | "+ NON-RENEWAL" · "+ OLD MAPLE" · "+ ROOF" · "+ NEW ROOF" · "+ TREE CREW" · "+ STORM WATCH" (red) · "MAPLE: STAYS" (green) |
| Band | "NEW MISSION / CASH OFFER" (amber, Close C) · "MAPLE / STAYS" (green) |
| Ticks panel | SELLS AS-IS · NO COMMISSION · NO CLOSING COSTS · YOU PICK THE CLOSING DATE |
| Captions | ALL CAPS, Ad 32 v3 style. Red: DROPPED, ROOF, NO, STORM, BACK. Green: CASH, OFFER, AS-IS, STAYS, MATTERED, REST, WAVING, POT, OBLIGATION. Gold: MAPLE |
| End card | Map still M with an amber pin + "YOUR HOUSE" and an amber target box pulsing on it (never green: the viewer has not done anything yet). Panel: "NEW OBJECTIVE" / "ASK FOR A CASH OFFER" / "No obligation." |

## Shot plan: every shot 1.0 s or less

Sources:
- S: painted orbit view over the Great Lakes, a small satellite glinting (one Nano Banana still; push-ins in the edit)
- M: painted top-down view of Bev's street, her small house under a huge maple in the centre (one Nano Banana still; also the end-card map)
- C1 Bev's house, day: high aerial and the mailbox
- C2 the maple and the roof, day, close
- C3 the kitchen table, day
- C4 storm night, the living room
- C5 the morning after, then leaving
- C6a the new small one-storey house, day
- C6b the new house, storm night
- C7 the new porch: aerial descent, the wave, the potted maple

Each C is one 8 s Flow clip (first-frame still, then Frames to Video) with 8-10 numbered shots. Only adults on screen. No readable text, numbers, logos or phone screens facing the camera; all words, stamps and HUD come from the edit. The edit trims or splits anything that comes back over 1.0 s, and the final is checked with the cut detector (pass = longest shot 1.0 s or less).

| Time (est.) | Line | Shots (source, length) |
|---|---|---|
| 0.00-3.81 | Bev's insurance dropped her. A satellite photo caught her maple. | 1 C1 top-down: the maple's big branch sweeps across the shingles; the red target box snaps on (0.85) · 2 C1 Bev at her mailbox, a plain white letter open, jaw dropping; NON-RENEWAL stamped red in the edit (0.8) · 3 S the orbit view, a satellite glints (0.7) · 4 M fast push-in down to her street, a shutter flash (0.7) · 5 freeze of shot 1 with a comic border, BEV / DROPPED BY INSURANCE (0.76) |
| 3.81-6.03 | Insurers check roofs from the sky. | 6 M wide street, a scan line sweeps roof after roof, source line on (0.8) · 7 M closer: small boxes blink green on the neighbours' roofs, Bev's stays red (0.7) · 8 C2 worn shingles, moss in the gaps (0.72) |
| 6.03-8.62 | The maple hugs her roof, rent-free. | 9 C2 the long branch lies across the roof and curls round the chimney like an arm round a buddy (0.9) · 10 C2 the branch pats the chimney in the wind (0.85) · 11 C2 wide: the huge maple leaning over the small house, + OLD MAPLE (0.84) |
| 8.62-11.58 | Every insurer she calls asks about the roof. | 12 C3 Bev at the kitchen table, phone to her ear (screen away), pen over a blank notepad (0.75) · 13 C3 her pen strikes a line through a blank row, + ROOF (0.7) · 14 C3 she looks up at the ceiling and sighs (0.75) · 15 C3 another strike, then another, the pad nearly all strikes (0.76) |
| 11.58-14.54 | New roof? Tree crew? Her savings said no. | 16 C2 the old roof, a red outline traced over it in the edit, + NEW ROOF (0.7) · 17 C2 the maple's trunk, + TREE CREW (0.7) · 18 C3 Bev lifts the lid of a small glass jar on the counter (0.8) · 19 C3 one moth flutters out of the empty jar; MISSION FAILED (0.76) |
| 14.54-17.87 | Every storm, Bev watches the maple, not the TV. | 20 C4 lightning over the house, the maple whipping in the wind, red vignette (0.85) · 21 C4 the living room: her armchair turned away from the TV toward the window, TV glow only (0.85) · 22 C4 Bev's wide eyes over her mug, lit by lightning, + STORM WATCH (0.8) · 23 C4 through the window, the maple thrashing over the roof (0.83) |
| 17.87-19.35 | The maple watches back. | 24 C4 a branch slaps flat against the window, leaves pressed like a nose, thunder (0.75) · 25 C4 Bev jolts back in the chair, mug sloshing (0.73) |
| 19.35-24.15 | Bev asked for a cash offer. The house sells as-is. The maple stays. | 26 C5 calm morning, Bev at the kitchen table, phone face-down beside her coffee (0.8) · 27 C5 her thumb taps the phone, screen turned away, glow on her fingers; band NEW MISSION / CASH OFFER (0.8) · 28 C5 her face, the first small smile (0.8) · 29 C5 the house in morning sun, a green sweep across it, tick SELLS AS-IS (0.8) · 30 C5 the maple still hugging the roof, leaves dripping (0.8) · 31 C5 Bev gives the maple a little salute from the porch; band MAPLE / STAYS (0.81) |
| 24.15-26.37 | Took what mattered. Left the rest. | 32 C5 Bev slides one photo album into a box (0.75) · 33 C5 she sets the box by the door, the full room behind her untouched (0.75) · 34 C5 she drives off, the old house and its maple shrinking behind (0.72) |
| 26.37-28.96 | Now Bev only calls her garden club. | 35 C6a the new small one-storey house, open sky over the roof (0.85) · 36 C6a Bev on the porch laughing into the phone, screen away (0.87) · 37 C6a three friends from the garden club come up the path with flowerpots and trowels (0.87) |
| 28.96-31.55 | Storm night? Bev watched the whole movie. | 38 C6b storm night at the new house, rain on the window, no tree over the roof (0.85) · 39 C6b Bev on the couch facing the TV (screen away from the camera, glow on her face), a popcorn bowl (0.87) · 40 C6b she laughs at the movie, feet up (0.87) |
| 31.55-34.51 | Another satellite photo. Bev's in this one, waving. | 41 S the orbit view again, the satellite glints (0.7) · 42 C7 high aerial descending onto the new house, the target box snaps on red and turns green (0.75) · 43 C7 top-down: Bev on the porch looks straight up (0.75) · 44 C7 she waves at the sky, grinning, shutter flash (0.76) |
| 34.51-37.10 | Her new maple fits in a pot. | 45 C7 Bev lifts a small potted maple sapling toward the sky like a trophy (0.85) · 46 C7 the garden club at the porch table cheers (0.87) · 47 C7 the sapling's leaves flutter in the breeze; MISSION COMPLETE (0.87) |
| 37.10-43.41 | Seen your roof from the sky? Ask for a cash offer. No obligation. | End card band stays the whole time: NEW OBJECTIVE: ASK FOR A CASH OFFER · No obligation., ticks panel. Under it: 48 S the satellite glints (0.8) · 49 M the street map, amber pin + YOUR HOUSE, amber box blinking (0.9) · 50 M closer on the pin, the box pulses (0.8) · 51 C5 recap: Bev salutes the old maple (0.75) · 52 C7 recap: Bev waving (0.8) · 53 C7 recap: the potted maple (0.75) · 54 M the pin pulses amber, gold sparkle round it (0.8) · 55 M wide map, YOUR HOUSE glowing (0.71) |

55 shots. Longest planned shot: 0.9 s. Each row's shot lengths add up to its line's estimated time.

To make (Flow): stills S and M, then clips C1, C2, C3, C4, C5, C6a, C6b, C7 (8 s each, 8-10 numbered shots each; the plan uses the best ones).

## Reviews (2026-10-27, one round of five, on the 128-word draft; simulated personas are not data)

- J-rules: FIX → applied (payload added between Open B and Open C, the truth-gate and "any situation" wording, the Ask question).
- Strategist: ranked it first of the three for a cold test; loss moved to word 4; "X and all" close replaced.
- Storyteller: new close, Close B and payoff lines; the eye knot, the recipe card and the list of names replaced (Veo text risk); the space zoom is built in the edit.
- Personas (simulated): the target viewer (Akron, non-renewal over an old roof and a tree) stop 9 / tap 6; Fran 8 / 6; Emily, Marcus and Fran picked it over the other two. Objection answered by "Her savings said no" (why not just fix it).
- Editing coach: cut to 113 words for this account's length (done); the first cut lands at 0.85 s.

## Open

- J's typed OK on the topic.
- An Ohio source for the landscape fact (HB 652 page unread, see above).
- The look and cast lock: Bev, her old house under the maple, the new house (gta-style stage 2), then the R prompts.
- Narrator voice (ElevenLabs, original voice or written consent) and `PERMISSIONS.md`.
- `propertyabundanceusa.com` returns 403, which blocks launch.
- The other two versions offered on 2026-10-27 ("Too Much House", "The Hum") are in `session-chat/2026-10-26_ad36-too-much-house-script.session.md` (local only).
