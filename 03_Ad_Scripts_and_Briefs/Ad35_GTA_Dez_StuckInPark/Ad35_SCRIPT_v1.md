# Ad 35 "Stuck in Park": script v1 (game look)

**Status (2026-10-26):** picked by the user (option A of 3). Waiting on J's OK on the topic and on "Termites included." Nothing generated.

**Where it came from:** the user's pasted draft "The Getaway" (a fast guy, a decaying inherited estate, foundation cracks, termites). Refined in five reviewer passes (J-rules, strategist, storyteller, seller personas, editing coach), then turned into three options; the user picked A.

What changed from the pasted draft, and why:
- Inherited estate became a dream job in another city. Inheritance is already in Ads 15, 18 and 20, and J rejected it ("Forget the inheritance").
- Cut lines that imply a fast sale (registry Section 3): "Fast", "months of waiting", "inspections, appraisals", "fastest guy in town", "fast lane".
- Cut "the traditional market is a trap" and the agent slamming a FOR SALE sign: disparaging, and text from the generator.
- Cut the cash stack over the car hood, plus "crew" and "the pros": they read as a money handoff and a heist. The game-look skill bans crime.
- Cut the logo and website end card (no company name; the site still returns 403) and the button animation (Meta's non-existent-functionality rule).
- The four metaphors (sinking, anchor, fast lane, one move) became one: a tow chain from the porch post to his bumper.
- Lines that other made ads already use were rewritten: "Fix it to list it", "cracks and all", the lake, windows down, "the only thing...".

**Look and process:** Ad 32's (painted open-world loading-screen poster art; Flow first frame, then video; ElevenLabs narrator; local HUD edit). Media go to `Game_Style/`. Plan: `10_Video_Builds/Ad35_GTA_Dez_StuckInPark/plan/01_LOOK_CAST_AND_REFERENCES.md`.

## Landscape fact (sell-fear part 1)

| Spoken | Source card (plain text, no masthead, no figure) | Source |
|---|---|---|
| "People turn down job moves over the house they'd leave behind." | ATLAS VAN LINES CORPORATE RELOCATION SURVEY · APR 2026 | [Atlas Van Lines press release, 2026-04-16](https://www.atlasvanlines.com/company-news/atlas-van-lines-59th-annual-corporate-relocation-survey-family-flexibility-and-the-economy-are-driving-relocation-decisions): "In 2025, most companies (59%) had an employee decline to relocate." Top reasons include "Concerns of selling/leaving the home at origin (21% in 2025)." Also reported by [Ohio REALTORS, 2026-06-29](https://www.ohiorealtors.org/blog/2364/moving-for-a-job-why-housing-may-be-the-make-or-break-factor/). Checked live 2026-10-24. |

It is an employer survey: the companies report why their employees said no. It is added to the fact bank in `11_Psychological_Hooks/sell-fear.md`.

## Script

```text
[OPEN A]   PAIN   Dez got the dream job. His house won't let him leave.
[payload]  PAIN   People turn down job moves over the house they'd leave behind.
[OPEN B]   PAIN   Every pull on that chain cracked the house a little more.
[payload]  PAIN   Turns out the house already had other tenants. Termites.
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

Measured by script (as-is counted as one word): 127 words. PAIN 51 (40.2%), PLANE 6 (4.7%), PATH 38 (29.9%), DEST 32 (25.2%). DEST is at its floor: cut no DEST words.
Voice length, estimated from words per minute: 47.0 s at Ad 32 v3's 162.2 wpm, 50.0 s at 152.3 wpm (team winners). Add about 1.5 s of end card.

**The question each open plants:** A: how can a house stop him leaving? B: what's breaking? C: what didn't the house see coming? Each close opens with its own words ("Never saw it coming", "The chain?", "The house that wouldn't let him leave"). The order is the required A-B-C nest with a payload after every open and close.

## Claim check (registry Section 1 only)

| Line | Registry row |
|---|---|
| The house sells as-is. Termites included. | As-is (confirmed). The J-rules review ruled "Termites included" a story detail, like Ad 25's "ceiling and all", not an "any condition" claim. J's OK requested. Keep termites cartoon-small on screen (Meta sensational content). |
| He took what mattered. Left the rest. | Belongings can stay (confirmed wording) |
| He picked the closing date. | Seller picks the closing date (confirmed). Never "around his start day": that implies the sale meets a deadline (J-rules ruling). |
| Ask for a cash offer. No obligation. | No obligation (confirmed) |
| On screen only: NO COMMISSION · NO CLOSING COSTS | No commission, no closing costs (confirmed) |

Not in the ad: speed of any kind, "no showings", "we buy", the company name, numbers or $.

## Duplicate check (2026-10-24)

No made ad or team ad uses job relocation, termites, a chain or tow chain, respawn, two keys, a boss text, or the name Dez. Checked: successful_video/*_META.txt, scripts, plans, the CLAUDE.md ad list, and the team's Ray, Irene, Rosa and Stress Meter ads. Ad 32 also has foundation cracks, but as one of six houses' problems.

## HUD (edit only; text inside y 285-1248 on 1080x1920; never over a face)

Minimap (house pinned, red chain icon) · pill MISSION: START THE DREAM JOB · name card DEZ / MOVING FOR WORK (about 2 s) · CHAINED (about 3.5 s) · source card (after the toast is gone) · + FOUNDATION CRACKS · + TERMITES · a chain icon with four red links that turn green one at a time: CASH OFFER ASKED, SELLS AS-IS, LEAVE THE REST, CLOSING DATE PICKED · NO COMMISSION · NO CLOSING COSTS pill · CHAIN OFF · LEVEL CLEARED · end card NEW OBJECTIVE: ASK FOR A CASH OFFER · NO OBLIGATION, with the viewer's own house pin and its chain turning green. No logo, website, buttons, digits or stars. About 17 text events, about 2.7 s apart (editing coach).

## Shot plan (22 shots; light: red dusk, then night, then golden morning; narrator only, no music bed)

The user's pasted draft asked for 50 cuts of 1 s or less. That is 10.9 cuts per 10 s; the rejected Ad 31 v3 ran 11.41 and the account's winners 1.82-3.89. So 22 shots, with bursts of 1 s or less on the pain lines and holds of 1.5-2.5 s on the hook, the ask, the rearview and the walk-in. The user can ask for the 50-cut version.

| # | Line | Shot |
|---|---|---|
| 1 | Open A | (2 s) Dusk driveway, mid-pull: tires smoking, the tow chain from the porch post to his rear bumper already taut, the car sliding BACKWARD toward the porch with its wheels spinning forward, the porch corner dipping |
| 2 | Open A | Bumper close-up: chain links straining |
| 3 | Open A | His jaw through the windshield, aviators on |
| 4 | Fact | (1.5 s) Top-down painted street map: every house chained to the car in its driveway (still, push-in in the edit) |
| 5 | Open B | A crack zips up the brick from the foundation |
| 6 | Open B | The porch corner sinks with a bounce (game physics) |
| 7 | Tenants | A porch beam, sawdust trickling from small holes; one tiny cartoon termite peeks out |
| 8 | Open C | He glances back at the house over his sunglasses |
| 9 | Open C | (1.5 s) Night: the porch light flickers like an eye, staring him down |
| 10 | Engine off | Key turns, dash goes dark, the chain drops slack onto the driveway |
| 11 | Close C | (1.5 s) He sits on the hood tapping his phone, the screen's glow on his face (screen never visible, phone never at his ear) |
| 12 | Close C | The house drops a shingle in surprise |
| 13 | As-is | Wide of the house, cracks and all, porch light dimming |
| 14 | Close B | Close on the bumper hook: Dez unhooks the chain and drops it on the driveway |
| 15 | Close B | Attic: he lifts one small box off a big pile and clicks the light off on the rest |
| 16 | Date | He circles a date on a plain kitchen calendar with blank squares |
| 17 | Close A | He pulls out of the driveway; the chain lies on the porch steps |
| 18 | Close A | (2 s) Rearview mirror: the old house shrinking behind him, porch light blinking goodbye |
| 19 | Dest | Sunrise highway toward a city skyline |
| 20 | Dest | He parks at a glass office tower; close-up of a clean bumper |
| 21 | Dest | (2 s) He walks in like he owns the place |
| 22 | CTA | End card |

## Hook test (strategist)

Use the same frame 0 for both, change only the first line. MAIN: "Dez got the dream job. His house won't let him leave." CHALLENGER: "Dez is moving for work. His house won't let go." The metric is the 3-s view rate against the account's 24.2%. The strategist estimates 1,531 impressions per arm to tell 24.2% from 20.0% at 80% power (the strategist's figure, not re-computed).

## Reviews (simulated personas, not data)

Final persona run: Maya (life transition) stop 8/10, tap 6/10. Fran 5/5. Emily, Marcus and Jason 2-3 (not their situation). This ad is aimed at Maya's card.

## Open

- J's OK on the topic, on "Termites included." and on the character before anything is generated.
- Voice: an original ElevenLabs narrator, or a clone only with written consent (`PERMISSIONS.md` beside the build).
- `propertyabundanceusa.com` still returns 403: nothing launches until it is fixed.
