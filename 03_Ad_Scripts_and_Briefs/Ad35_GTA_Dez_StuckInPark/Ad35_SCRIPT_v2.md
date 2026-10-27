# Ad 35 "Stuck in Park": script v2 (game look)

**Status (2026-10-26):** current. v1 (`Ad35_SCRIPT_v1.md`) is superseded. Waiting on J's OK on the topic, on "Termites included." and on the character. Nothing generated.

**What changed from v1 (user, 2026-10-26):**
1. "The first hook should be the attention grabber." The open is now the literal twist on the chain picture: "Dez's house won't let him leave. Literally." The dream job moves to line 2.
2. The global 1-second rule ("you cannot stack to one frame more than one second… 10 frames in an 8-second video, or 8"): every shot below is 1.0 s or less, the end card included. Key moments come back as a new angle instead of being held. v1's 22-shot plan with 1.5-2.5 s holds is replaced.
3. To fit the hook without dropping DEST below 25%: "a little" and "Turns out" were cut.

**Graphics (user, 2026-10-26): like `successful_video/Ad32_final_v3.mp4`.** The full lock is `10_Video_Builds/Ad35_GTA_Dez_StuckInPark/plan/02_GRAPHICS_LOCK_from_Ad32v3.md`, and it replaces v1's HUD list (no chain-link icon, no LEVEL CLEARED). It adds a DREAM JOB meter, the mission pill, toasts, ALL CAPS keyword-coloured captions, bands, the ticks panel and the YOUR HOUSE map end card. The wording on screen in the shot plan below follows that lock.

Everything else (source card, claims check, duplicate check, look) stands as in v1. Look and reference prompts: `10_Video_Builds/Ad35_GTA_Dez_StuckInPark/plan/01_LOOK_CAST_AND_REFERENCES.md`.

## Script

```text
[OPEN A]   PAIN   Dez's house won't let him leave. Literally.
[payload]  PAIN   He just got the dream job in another city.
[payload]  PAIN   People turn down job moves over the house they'd leave behind.
[OPEN B]   PAIN   Every pull on that chain cracked the house more.
[payload]  PAIN   The house already had other tenants. Termites.
[OPEN C]   PAIN   So Dez tried something the house never saw coming.
[payload]  PATH   Engine off.
[CLOSE C]  PATH   Never saw it coming: he asked for a cash offer.
[payload]  PLANE  The house sells as-is. Termites included.
[CLOSE B]  PATH   The chain? He took what mattered. Left the rest.
[payload]  PATH   He picked the closing date.
[CLOSE A]  DEST   The house that wouldn't let him leave? Shrinking in his rearview.
[payload]  DEST   Monday, new city. Dez pulls up to the dream job, nothing on his bumper. Walks in like he owns the place.
[CTA]      PATH   Is your house the chain? Ask for a cash offer. No obligation.
```

Measured by script (as-is counted as one word): 128 words. PAIN 52 (40.6%), PLANE 6 (4.7%), PATH 38 (29.7%), DEST 32 (25.0%). Every tag is at or inside its budget; DEST is exactly at its floor.
Voice length, estimated from words per minute: 47.3 s at Ad 32 v3's 162.2 wpm, plus an end-card tail of about 1.5 s. The line times below come from the same estimate. Re-time everything from the real voice file's word times.

**The hook:** frame 0 shows the problem with no words (a house dragging a car backward by a tow chain). The line names Dez, plants a plain question (how can a house stop him leaving?), and ends on the punch word that the picture proves. Alternates for a test, same frame 0: "Dez floored it. His house pulled him back." / "Dez is leaving town. His house said, 'Not without me.'"

## Shot plan: every shot 1.0 s or less

Sources:
- C1 driveway at dusk
- M top-down map (one Nano Banana still, push-ins in the edit)
- C2 the house with no people
- C3a and C3b driveway at night
- C4 the inside of the house at dawn
- C5 the drive at sunrise
- C6 the new city, golden morning

Each C is one 8 s Veo clip with 8-10 numbered shots. All text and HUD come from the edit. The edit trims or splits anything that comes back over 1.0 s, and the final is checked with the cut detector (pass = longest shot 1.0 s or less).

| Time (est.) | Line | Shots (source, length) |
|---|---|---|
| 0.0-2.6 | Dez's house won't let him leave. Literally. | 1 C1 wide low, mid-pull: tires smoking, the tow chain from the porch post to his rear bumper taut, the car sliding BACKWARD toward the porch, wheels spinning forward (0.9) · 2 freeze of shot 1 with a comic border, DEZ / MOVING FOR WORK (0.7) · 3 C1 tow hook, the links straining (0.5) · 4 C1 rear tire spinning in smoke, on "Literally" (0.5) |
| 2.6-5.9 | He just got the dream job in another city. | 5 C1 phone on the dash lights up, glow only, toast INCOMING: DREAM JOB (0.8) · 6 C1 Dez grins at it through his aviators (0.8) · 7 C1 the porch post bends toward the car, nails popping (0.9) · 8 C1 Dez glares back at the house over his sunglasses (0.8) |
| 5.9-10.0 | People turn down job moves over the house they'd leave behind. | 9 M painted street map, every house chained to the car in its driveway (0.9) · 10 M closer, two neighbors' cars straining on their chains (0.8) · 11 M back on Dez's pin, source card (0.8) · 12 C1 his car jerks backward again (0.8) · 13 C1 Dez drums the wheel, jaw set (0.8) |
| 10.0-13.3 | Every pull on that chain cracked the house more. | 14 C2 a crack zips up the brick from the foundation, + FOUNDATION CRACKS (0.8) · 15 C2 tilted: the porch corner sinks with a bounce (0.8) · 16 C2 the gutter sags and swings (0.8) · 17 C2 the whole house shudders, dust puffing from the siding (0.9) |
| 13.3-15.9 | The house already had other tenants. Termites. | 18 C2 sawdust trickles from small holes in a porch beam, + TERMITES (0.8) · 19 C2 one tiny cartoon termite peeks out and ducks back in (0.9) · 20 C2 a line of sawdust runs along another beam like a lit fuse (0.9) |
| 15.9-19.2 | So Dez tried something the house never saw coming. | 21 C3a night on the driveway, the porch light flicks on like an eye (0.9) · 22 C3a the porch light flickers, staring him down (0.8) · 23 C3a Dez, sunglasses off, eyes narrowing at the house (0.8) · 24 C3a his hand on the key (0.8) |
| 19.2-20.0 | Engine off. | 25 C3a the key turns (0.4) · 26 C3a the dash goes dark and the chain drops slack onto the driveway (0.4) |
| 20.0-23.7 | Never saw it coming: he asked for a cash offer. | 27 C3b the porch light flickers in confusion (0.9) · 28 C3b Dez slides onto the hood and sits (0.9) · 29 C3b his thumb taps the phone, screen turned away, glow on his fingers; link 1 green CASH OFFER ASKED (0.9) · 30 C3b his face in the glow, one-sided grin (0.9) |
| 23.7-25.9 | The house sells as-is. Termites included. | 31 C3b the house drops a shingle in surprise (0.8) · 32 C3b the whole house at night, cracks and all; link 2 green SELLS AS-IS; NO COMMISSION · NO CLOSING COSTS pill (0.8) · 33 C3b the tiny termite waves from its hole (0.6) |
| 25.9-29.2 | The chain? He took what mattered. Left the rest. | 34 C3b Dez lifts the chain off the tow hook (0.8) · 35 C3b he drops it on the driveway (0.8) · 36 C4 attic at dawn: he lifts one small box off a big pile (0.8) · 37 C4 he clicks the attic light off on the rest; link 3 green LEAVE THE REST (0.8) |
| 29.2-31.1 | He picked the closing date. | 38 C4 a marker circles a date on a plain kitchen calendar with blank squares (0.9) · 39 C4 Dez caps the marker and nods; link 4 green CLOSING DATE PICKED, CHAIN OFF (0.9) |
| 31.1-35.1 | The house that wouldn't let him leave? Shrinking in his rearview. | 40 C5 the car rolls out of the driveway, the chain left on the porch steps (0.8) · 41 C5 the box on the passenger seat (0.8) · 42 C5 rearview mirror: the old house shrinking behind him (0.8) · 43 C5 rearview, closer: the porch light blinks goodbye (0.8) · 44 C5 Dez slides his aviators back on, grinning (0.8) |
| 35.1-42.9 | Monday, new city. Dez pulls up to the dream job, nothing on his bumper. Walks in like he owns the place. | 45 C5 sunrise highway toward a skyline, minimap route drawing on (0.9) · 46 C5 the skyline in golden light (0.9) · 47 C6 the car pulls up to a glass office tower on a plaza (0.9) · 48 C6 the clean rear bumper, empty tow hook (0.8) · 49 C6 the car door shuts (0.8) · 50 C6 white sneakers step onto the plaza (0.8) · 51 C6 he walks toward the glass doors, box under his arm (0.9) · 52 C6 his reflection in the doors, grinning (0.9) · 53 C6 the doors slide open into golden light, LEVEL CLEARED (0.9) |
| 42.9-48.8 | Is your house the chain? Ask for a cash offer. No obligation. | End card band stays the whole time: NEW OBJECTIVE: ASK FOR A CASH OFFER · NO OBLIGATION. Under it, recap shots from the clips above, each 1.0 s or less: 54 the viewer's own house pin on the minimap with a red chain (0.9) · 55 the chain lifting off the hook (0.8) · 56 the rearview house shrinking (0.8) · 57 Dez walking in (0.8) · 58 the house pin's chain turning green (0.9) · 59 the pin glowing gold (0.8) · 60 Dez's one-sided grin in the doorway (0.9) |

60 shots. Longest planned shot: 0.9 s. Each row's shot lengths add up to its line's estimated time, within 0.1 s.

Clips to make (Flow, first-frame still then video, 8 s each): C1, C2, C3a, C3b, C4, C5, C6, plus the map still M. The end card reuses clips.

## Unchanged from v1

The source card (Atlas Van Lines, 2026-04-16), the claims check (registry Section 1 only), the duplicate check, the HUD list and the open items: see `Ad35_SCRIPT_v1.md`.
