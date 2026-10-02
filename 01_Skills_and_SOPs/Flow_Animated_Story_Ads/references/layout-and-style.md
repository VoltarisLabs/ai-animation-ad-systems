# Layout, fonts, colours and caption styles

Canvas 1080x1920, 24 fps.

## Safe zones (Reels / TikTok / Shorts)

- Top 13% (y < 250): app chrome. Keep text out.
- Bottom 20% (y > 1536): caption, handle, CTA button. Keep key text out.
- Right rail (x > 885 for y about 1000-1700): like / comment / share buttons. Keep text left of it; long one-line subtitles need wide side margins (MarginL/R 200 → about 680 px wrap).

## Where things sit (GTA HUD builder)

| Element | Position | Style |
|---|---|---|
| Faces in the clips | about 35-50% of height (prompt: "face centered, eyes just above mid-frame; top eighth and bottom third clear"); banners at y 1000 sit just below | |
| Minimap | top-left, 250 px disc at (34, 262) | PIL PNG, dark fill, white ring, amber house icon |
| STRESS label + 5 stars | top-right, stars at x 721-1005, y 345; label right-aligned at 1038, 268 | Anton 50 amber; stars R=34 |
| Toasts (+ REPAIR QUOTES, star-pop terms) | right-aligned at 1045, y 420 / 505 | Bebas Neue 56 (50 on two lines for long ones), dark box |
| Subtitles | centred, y 1185 (61%) | Montserrat 60 bold, white, 4.5 black outline |
| Objective line | centred, y 1305 | Bebas Neue 62 amber |
| Titles / banners | centred, y 1000 on a dark band; the hook title sits low (1200/1330) so the face stays clear | Anton 118-150; MISSION COMPLETE in amber |
| Cost list | centred, header on the subtitle line, items from y 1292 every 70 px | Bebas Neue 74, hot red, struck grey when cancelled |
| Name card (freeze) | left, RAY at (70, 760), HOMEOWNER below | Anton 140 white / Bebas 58 amber |
| End card | band 870-1290: NEW OBJECTIVE (amber kicker), ASK FOR A / CASH OFFER, "No obligation." | |

Colours (ASS is &HBBGGRR): amber `&H0000B4FF`, red `&H002E2EE8`, list red `&H003C3CFF`, white, black. Never a game's own logo font (no Pricedown); draw your own HUD rather than copying a game layout.

Checks that caught real problems: the objective line covered a cap (moved to the bottom); the minimap sat on his head during a push-in (hidden for that shot); long toasts crossed his cap (two lines); the empty star meter vanished on the end card (darker plate, light slot outlines); the meter crossed the freeze panel's border (moved 14 px left).

## Card reel builder (claymation)

Card 936x1248 at (72, 592) inside a white 10 px frame with a soft shadow, rounded corners r=36; cream background (238, 221, 199) or black with a faint 108 px grid. Lead words Montserrat 88 at y 300, red keyword Archivo Black up to 190 at y 445, small line Montserrat 56 at y 548. Stamps (NO REPAIRS, NO COMMISSION...) Anton 132 white in a red box, slammed in with a pop sound. Orange progress bar across the top. Lead words show the instant a shot starts; the keyword pops on its word.

## Caption styles the person reacted to

- Rejected: plain captions in the middle of the frame; a single word popping at the top.
- Liked: "tape" captions (words on torn tape strips) with zoom/shake, offer stamps and a progress bar (One Little Leak); the ClayReel card style; GTA subtitles + HUD.
- Always: no dead space. Tighten pauses, put lead text up the moment a shot starts, make the card and type big.

## Static ads (same brand)

Liked: black-and-white poster, before/after split (headache of listing vs. handing over keys), claymation, clay comic (favourite). Rejected: realistic "native" formats (fridge note, marker on a photo, polaroids, checklist), orange template, colour-way swaps, anything that looks AI-fake. No company name on the image. Give full Nano Banana Pro prompts (3:4, x4).
