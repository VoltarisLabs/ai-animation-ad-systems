# Script, hook and claims

## 1. Re-read the claims registry, every time

`11_Psychological_Hooks/claims-registry.md` in this repo is the source of truth and it changes (on 2026-09-29 the "we buy it ourselves" family was frozen). Fetch it fresh before writing a line. From outside a checkout:

```bash
gh api repos/VoltarisLabs/ai-animation-ad-systems/contents/11_Psychological_Hooks/claims-registry.md \
  -H "Accept: application/vnd.github.raw" > claims-registry.md
```

As of 2026-10-01:

| Usable (Section 1) | Wording |
|---|---|
| As-is | "The house sells as-is." / "No repairs." (neutral verb, no actor) |
| Belongings can stay | "Take what matters. Leave the rest." / "Don't clean it out." |
| No commission / fees / closing costs | "No commission. No closing costs." |
| Seller picks the date | "You pick the closing date." |
| No obligation | "No obligation." |
| Admission (optional) | "Truth? Cash offers usually come in lower than listing. Ours too." Always followed by its close "That's why lower isn't everything." Keep "usually". |
| Listing costs in general terms | "Listing means repairs, cleanup, commission and closing costs." (no numbers) |
| Offer name | "The Walk-Away Offer" (owner-approved; the team found it unclear, so the GTA ad dropped it) |

Blocked or banned: any "we buy / we're the buyer / no middleman / no wholesaling" line; speed or timelines; "any condition"; "we show you the math"; an offer for every submission ("Get your offer" → use "Ask for a cash offer"); numbers of any kind; "best deal", "best price", "top dollar"; fake urgency; competitor names; testimonials; "you inherited / you're behind" (write "Inherited a house?"; keep death words out of Flow prompts too, they get blocked). A "bonus cash" offer is not in the registry: it can be scripted for the team but must not run until the owner confirms amount, qualification and timing and adds it to the registry.

## 2. The nested loop

The team's structure. Each Open raises one concrete question; the Closes pay them off in reverse order, often with "That's why...". Viewers track about two levels, so keep each open simple and visual.

| Part | Job | Stress Meter example |
|---|---|---|
| Open A (hook, 0-3 s) | Face + motion + surprise, one named situation | "The ceiling's leaking, again. Stress meter? Maxed out." |
| Open B | The pile-up everyone knows | "Repair quotes piling up, weekends on a ladder, and everyone says: fix it all, then list it." |
| Open C | The turn | "There's another way out." |
| Main | The mechanism, in approved terms | "Listing means repairs, cleanup, commission and closing costs. This cash offer? None of that." |
| Close C | Pay off the turn | "Take what matters, leave the rest." |
| Close B | Pay off the pile-up | "Fix it all first? No need. The house sells as-is." |
| Close A | Pay off the hook | "You pick the closing date. And that stress meter? Empty." |
| Ask | Soft CTA | "Ask for a cash offer. No obligation." |

Aim for 85-115 spoken words (30-40 s). Plain words a 12-year-old follows.

## 3. Hooks that worked

- Physical comedy with a callback: water crashes onto his face on "again", and the stress meter maxes out.
- A surprise reveal tied to the offer: hammer smashes the wall and cash blasts out ("Bonus cash... if you put the hammer down"), but only if the offer is real.
- Freeze-frame character intro (RAY / HOMEOWNER) right after the hook, like a game cutscene.

Things that fail: a man squinting at a house (no motion), hype words, "you" + a personal attribute, a hook that promises something the ad never pays off.

## 4. Getting options: judge panel

When asked for script options, write several from different angles instead of iterating one. For the GTA ad: four angles (mission objectives, stress star meter, cutscene name cards, loading-screen tips) → each draft checked and fixed by a compliance-and-hook reviewer that re-reads the registry → one judge ranks all and returns the top 3 with a one-line pitch each. In Claude Code this is a Workflow (writer per angle → checker per draft → judge); each agent reads the registry file itself. No such script ships with this skill: write one modelled on `scripts/qa_workflow.js` (args: registry path, brief, angles, team direction), or, without the Workflow tool, draft each angle yourself, run the registry's Section 5 checklist on each, then rank and present the top 3.

Present options as a table the team can read at a glance:

| Part | Narrator says | What we see (style) |
|---|---|---|

Recommend one and say why in one or two lines. Remember the team lead's direction (for example "GTA style", "bonus cash hook"), and say plainly when a direction needs the owner's OK.

## 5. Changing lines later

When a line changes, check what depends on it: the admission line needs its close; removing "catch" language means Open C changes too; a new offer wording changes the end card and the objective text. Re-record the whole voice rather than splicing single lines when the voice settings or reader change.
