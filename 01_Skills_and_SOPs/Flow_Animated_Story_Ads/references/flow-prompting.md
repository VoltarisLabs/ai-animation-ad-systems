# Reference images and Flow prompts

Tools the person uses in Google Flow:
- **Nano Banana Pro** (images): character sheets, settings, stills, end cards. 9:16 for anything that goes in the edit, 16:9 is fine for a reference sheet. Ask for x4 and let them pick. Download at 2K when offered (a 768x1376 still gets soft after a push-in).
- **Veo 3.1 Ingredients to Video** (9:16, 8 s; Flow sometimes returns 10 s): attach 1-3 reference images.
- **Veo 3.1 Frames to Video**: first frame = an exact image (for callbacks, e.g. the kitchen still that later gets swept clean). Takes no ingredients, so the likeness comes from that frame.

## 1. References first

Make the character and the setting before any clip, get a yes, save them in `refs/`, and attach them to every clip. Without them the character drifts (in the claymation ad one clip came back with a different man and could not be used).

A new ad in a look that already exists reuses that ad's approved refs (ask the person to attach their copies; the images are not in this skill) unless the story needs a different person. Any new made-up character needs its own owner review before launch.

Game look, character sheet. The first version, described as a tired dad in a flat cartoon style, was rejected as "not a game character"; the approved look was semi-realistic painted poster art with a rugged, confident character:

```
Open-world video game loading-screen poster art style. Semi-realistic digital painting with bold black ink outlines, cel-shaded color blocks, dramatic high-contrast lighting, saturated colors. An original character: RAY, a rugged American man in his early 50s, short salt-and-pepper beard, strong jaw, confident half-smirk, aviator sunglasses hooked on his shirt collar, worn navy ball cap with no logo, faded red flannel shirt with sleeves rolled up over a grey t-shirt, blue jeans, brown work boots. Full body, standing with arms crossed, slight low-angle hero shot. Plain light background so he is easy to reuse. No text, no letters, no numbers, no logos.
```

Game look, the house:

```
Open-world video game loading-screen poster art style. Semi-realistic digital painting with bold black ink outlines, cel-shaded color blocks, dramatic sunset lighting, saturated orange, magenta and teal sky, palm trees and leafy trees along a quiet suburban street. A tired single-story ranch house: small front porch with three steps, sagging gutter, peeling paint, blue tarp over part of the roof, overgrown lawn, concrete driveway. Slight low-angle wide shot. No people, no cars. No text, no house numbers, no signs, no logos.
```

Describe the look; don't name a game (see SKILL.md, "Styles, not brands").

Claymation look: make a clean reference of the clay man from the best frame of an approved clip (face crop + full body side by side) and attach it to every later clip.

Reuse frames as references too: a frame of the glowing beam from one clip kept the beam identical in the next; a frame of the truck and box from the walk-away clip made the end-card poster match.

## 2. Veo clip prompt

Either order works. The approved game-look clips opened with "Vertical 9:16, single shot, no cuts.", then the scene, the timed beats and the framing, then the style words, then the negatives and the sound. A template:

```
Vertical 9:16, single shot, no cuts. <Where, light, time of day>. <Character> from the character reference (<3-4 visible traits: cap, shirt, beard>) <starting state, already mid-action>.
0-1 s: <first beat>.
1-3 s: <the one main action>.
3-8 s: <settle / hold / small reaction>.
<Framing: his face centered, eyes just above the middle of the frame; keep the top eighth and bottom third clear.>
<STYLE WORDS>. 2D animated illustration, not 3D, not photoreal.
No text, letters, numbers, logos, signs or game HUD. No other people, police, weapons, money or crime. <Scene-specific: no calendars, clocks, screens, stickers, plates.>
Mouth closed; he does not speak. No dialogue, no voice, no music. Sound: <2-3 real sounds>.
```

Why each part matters:
- **One action, starting mid-action.** Veo garbles two actions. Start him already on the ladder, already seated, already inside the light, door already shut.
- **"Single shot, no cuts."** Veo otherwise adds a cut mid-clip.
- **Timed beats** land the key action early (the splash at 1 s) so the hook can start on it.
- **Framing** keeps faces out of the caption and HUD bands (see `layout-and-style.md`).
- **"Does not speak / no dialogue"**: Veo invents speech and music; once it even changed a voice line. Clip audio is muted or ducked in the edit, but speech in the clip can still leak.
- **No text or numbers**: generated paperwork, trucks, ladders and signs come back with garbled text or numbers, which the ad cannot show.

The approved hook clip (game look, Ray reference attached; the style words are written generically here):

```
Vertical 9:16, single shot, no cuts. A worn living room at sunset, warm orange light through the window. Low-angle close-up from below: Ray, the man from the reference image (navy cap, red flannel shirt, salt-and-pepper beard), looks straight up at a sagging brown water stain on the ceiling, holding a plastic bucket to his chest. His face is in the middle of the frame, the stain above him.
0-1 s: a fat drip splashes on his cheek.
At 1 s: a dinner-plate-sized stained patch bursts and a heavy splash of water pours down right onto his face. The ceiling stays up: no hole, no collapse. He flinches toward the camera, eyes squeezed shut, soaked. Quick camera shake.
Then he stands dripping, staring up at the ceiling, completely fed up.
Open-world video game loading-screen poster art style animation: semi-realistic digital painting look, bold black ink outlines, cel-shaded color blocks, dramatic high-contrast lighting, saturated colors.
No text, letters, numbers, logos or signs anywhere. No calendars, clocks, screens or phones. No other people.
Sound: drip, a wet crack, a big water splash. He does not speak. No dialogue, no voice, no music.
```

## 3. Known Veo / Nano Banana hazards

| Hazard | What to write instead |
|---|---|
| Climbing onto a ladder from the ground (feet through rungs) | "already stands three rungs up a plain unmarked aluminium ladder" |
| Taking a cap off (the cap morphs) | "pushes his cap back and wipes his forehead" |
| Opening a door, camera inside the house | start on the porch, door already shut |
| Ceiling "gives way" (caves in, implies major damage, drifts toward the unconfirmed "any condition") | "a dinner-plate-sized stained patch bursts... the ceiling stays up, no hole, no collapse" |
| Paperwork or contracts | "blank white papers seen edge-on, a paint roller on top; no pens, signature lines, dollar signs, receipts" |
| Person leaning on a truck (legs vanished behind the tailgate) | "SITS on the edge of the lowered tailgate, legs hanging down, whole body visible from cap to boots" |
| Truck badges and plates | "no emblem or plate" (check the plate is blank in a zoomed frame) |
| A mission-marker light gaining arrows or icons | "a tall cylinder of soft golden-yellow light... a plain glow, no symbols" |
| Handshakes (merged hands; also a claims problem) | avoid; see the claims rules |
| Death or grief words ("late mother", funeral, urn, casket) get the prompt blocked | imply it: an inherited house, a keepsake box, old photos seen from the back, dated furniture; never name a death |

## 4. Stills (Nano Banana Pro)

Use stills for a held beat (Ray at the kitchen table behind a stack of repair papers) and for the end-card poster. Say where things sit so text has room: "the stack on the left side of the table, never blocking his face", "a plain blue bin on the floor at the left". A still that later becomes a Frames-to-Video first frame must be kept exactly (same file).

## 5. The smash-hook prompt (claymation example)

```
Claymation stop-motion, vertical 9:16. The clay man from the reference image (same face, hair and clothes) stands in front of a cracked living-room wall, gripping a big sledgehammer.
0-1s: He winds up and swings as hard as he can.
1-2s: The hammer SMASHES the wall. The whole wall bursts open in a huge explosion of clay plaster chunks and dust, and a massive blast of green cash shoots out of the hole toward the camera. Strong camera shake, slow motion on the burst.
2-5s: Cash keeps gushing out like a waterfall, hundreds of bills swirling around him. He stumbles back, eyes huge, jaw dropped.
5-8s: Bills rain down all over the room. Still in shock, he slowly lowers the hammer to the floor.
Style: handmade clay, visible fingerprints, choppy stop-motion movement, warm lamp light, dramatic and exciting.
Audio: huge crash, crumbling plaster, loud whoosh of paper, bills fluttering. No music. He does not speak. No dialogue, no voice.
```

The edit cut it into two shots: swing and blast (punch-in, shake and a 2-frame flash on impact) under "Bonus cash!", and the hammer hitting the floor exactly on "down". Money on screen belongs only to an offer the owner has confirmed.

## 6. Checking a clip

For each new clip: `bash scripts/contact_sheet.sh src/c1_splash.mp4 4` (a timestamped sheet, 4 frames a second), a zoomed strip around the key moment if needed, and `python scripts/words.py src/c1_splash.mp4` (it reads the clip's audio itself) to catch speech. Whisper also hallucinates "Thank you for watching!" on breeze noise; that is not speech. Note the source second of each beat (impact, head drop, nod, sweep, glance back): the builder anchors those to voice words.
