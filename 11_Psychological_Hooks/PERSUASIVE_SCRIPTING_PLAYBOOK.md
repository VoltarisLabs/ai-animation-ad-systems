# Persuasive Scripting Playbook: Angle, Strategy, Data, Next Script

Written 2026-10-01. One loop for every ad: **research → angle → strategy → script → review → launch → read the data → next test.**

This file adds four things the folder did not have:
1. **The angle engine** (§2-§4): turn research into a "villain" angle. The viewer's self-blame moves onto a real outside cause, the cause is explained, and the offer lands as the fix. It is decoded from the Lem ad below.
2. **The strategy and test plan** (§5): which angles to run, in what order, and which number decides.
3. **The data loop** (§6-§7): which number judges which line of the script, and what to test next.
4. **The next-script review** (§8): a fixed block at the end of every script that says what to improve in the next one. Real results replace the predictions once the ad runs.

Plus what the Ad Creators Lab course and its Ad Games entries show about making the video and the voice look and sound real (§9), and what the feedback on Ads 15 to 20 has taught so far (§10).

**What stays in force, unchanged:**
- `claims-registry.md` wins over every file here. It is on `origin/main` (added 2026-09-29); pull before use.
- `OFFER_FIRST_PROCESS.md` (locked).
- `AD_COPY_CHECKLIST.md`.
- The loop order (Open A → payload → Open B → payload → Open C → payload → Close C → payload → Close B → payload → Close A → payload → CTA).
- The labelled script with a `SHOW →` line under every line.
- Company voice only: an AI avatar never plays a seller or a customer.
- Cost summary and a typed go before any paid generation.

**Where it sits in the README order:** between step 2 (Offer) and step 3 (Write), and again at step 4 (Test).

---

## 0. The loop

```
RESEARCH ........ research-cards.md, Buyer_Avatar/, comments on our live ads
   ↓
ANGLE ........... §2  false belief → villain → mechanism → fix
   ↓
STRATEGY ........ §5  which angles, which test, which number decides
   ↓
SCRIPT .......... §4 beat map + AD_COPY_CHECKLIST + OFFER_FIRST + loop order
   ↓
NEXT-SCRIPT REVIEW  §8  score, 3 fixes, prediction    ← after EVERY script
   ↓
OWNER / J FEEDBACK  logged in §10
   ↓
LAUNCH → READ THE DATA  §6
   ↓
DIAGNOSE → NEXT TEST    §7  → back to ANGLE (concept lost) or SCRIPT (one beat lost)
```

**Today's state (measured 2026-10-01):** no Property Abundance ad has run, so there is no performance data. `swipe-file.md`'s "Proven winners (our own ads)" table is empty. Until the first test runs, the review in §8 works on predictions and owner feedback only. The first test's job is to give us our own baseline (§5).

**Blocker before any test:** `propertyabundanceusa.com` failed on 2026-09-27 (http 403, https certificate error). No ad can send traffic there. Either fix the site or run Meta Instant Forms, which keep the lead on Meta (§6 says which click metric to read then).

---

## 1. The model ad, decoded: Lem (Ad Games #2)

**Source.** An entry in Ad Creators Lab's "Ad Games #2" (theme: AI podcast ads, September 2026). The judging criteria were the hook, the realism of the conversation, the realism of the AI creative (voice and visuals), and persuasion. The creator's own write-up, as pasted by the user on 2026-10-01:

> "Two friends, one couch, one confession most women never say out loud. The angle: we make vibration the villain / it was never you (research showed most women think they're the problem). Shame → relief, building tension, explaining the alternative mechanism then revealing the product (Lem lands as the fix)"

The product is most likely Hello Nancy's Lem (inferred from the name and the angle, not confirmed). Its page says it uses "air pulse technology" instead of "motor-driven vibration" (hellonancy.com/pages/lemon-massager).

### The ad, measured (downloaded and transcribed locally, 2026-10-01)
79.67 s, 1074 × 1920, 273 words at 207.3 words per minute. 27 cuts (3.39 per 10 s); the first cut is at 2.87 s. Measured with ffprobe, ffmpeg scene detection (> 0.3) and whisper.cpp large-v3-turbo.

**The set:** a warm, low-lit podcast studio (a neon "podcast" sign, bookshelves, acoustic panels, mugs). Two women with broadcast mics and headphones: the **confessor** and the **guide**. The edit cuts between single shots of each. White lowercase captions of 1 to 4 words sit mid-frame.

**The cutaways are metaphors, not stock:** warm, tactile 3D shots. On "rubs you raw", the old method is a soft object grinding a cracked red surface. The product glows on soft fabric. On "climb from there", dots rise around it. A woman lies awake in bed on "you spend years".

| Time | Beat | What happens (paraphrased; short quotes) | Job |
|---|---|---|---|
| 0.00 | Hook | The confessor asks to tell a secret: "you're not allowed to make a face" | Opens a loop: what secret? |
| 2.76 | Reaction | The guide is "already making a face" | Humour, realism |
| 4.22 | Confession | She has never finished; she starts to say the product category and stops herself ("vi-… Nothing.") | Shame. The self-censored word is funny and keeps the ad platform-safe |
| 8.02 | Shame peak | She has faked it every time and is tired of pretending | The unspoken sentence, out loud |
| 12.48 | Validation | The guide thanks her, then: "same" | Not alone |
| 18.80 | **Self-blame + absolution** | The guide "thought I was just built wrong"; it turns out she was using "the wrong thing the whole time" | Blame moves to the old method |
| 24.12 | Skeptic asks | "Really? Tell me more." | The viewer's question, asked for them |
| 25.98-39.68 | **Mechanism of the problem** | The old device "only does one thing. Friction." It only works if the body is already there, so it "rubs you raw", "and you spend years thinking you're the problem" | The villain, explained in plain cause and effect |
| 39.68 | Skeptic asks | What does the new way "actually do differently?" | Pulls the next beat; never a pitch |
| 43.16-55.26 | **Mechanism of the fix** | Soft air pulses instead of grinding; "works with your body"; starts gentle, "you climb from there" | The new way, before the product |
| 55.26 | Personal proof | Her first try: doubt, then it worked | A story, not a claim |
| 59.06 | Desire | "I need the name." | The viewer asks for the product |
| **62.72** | **Product named** (78.7% of the ad) | Price, a 30-day guarantee, "send it back" | Risk reversal |
| 69.50 | Commitment | The confessor will order it before she leaves; "Text me" | Social proof inside the scene |
| 75.42 | CTA | Straight to the viewer: click the link below | Breaks the overheard frame once, at the end |

**What makes it work, in one line each:**
- The skeptic asks every question the viewer would ask, so each beat is pulled, not pushed.
- The shame is said by one friend and answered by "same", so it's safe to keep watching.
- The villain is explained before the product exists in the ad. When the name lands, it's the answer to "I need the name".
- The metaphor shots carry the mechanism in pictures, so it works with the sound off.

### The seven moves, and the rule we take from each

| # | Move | In the Lem ad | Why it works (evidence) | Our rule |
|---|---|---|---|---|
| 1 | **Research finds the self-blame** | "research showed most women think they're the problem" | The angle comes from a belief the audience holds, not the writer's taste. | Every angle starts from a self-blame belief that is sourced on a research card. |
| 2 | **An outside villain** | "we make vibration the villain" | Blair Warren (2005): people follow those who "justify their failures… and help them throw rocks at their enemies." StoryBrand: one villain, and it must be real. | Name an outside cause: a system, a rule, an old method. Never a person or a group of people. |
| 3 | **Absolution** | "it was never you" | Albuquerque (*The 16-Word Sales Letter*): take "the blame of their failures off their shoulders and put it onto the old opportunities they tried." Agrawal & Duhachek (2010): an ad that adds to the shame a viewer already feels works less well, because viewers discount it. | One plain line that lifts the blame. Never add blame ("you should have…"). |
| 4 | **A format that makes the secret sayable** | "Two friends, one couch, one confession" | Overheard talk persuades more than a pitch (Walster & Festinger 1962, via a secondary summary). Dramas invite less counter-arguing than arguments (Deighton, Romer & McQueen 1989). A second voice helps only if the argument is strong and the two voices hold different views (Harkins & Petty 1987). | Pick the format for the emotion. In a two-voice format, one voice is the skeptic and asks the viewer's questions. |
| 5 | **Shame → relief, with tension** | "Shame → relief, building tension" | Overall judgments of an ad are driven by the peak moment and the end, and viewers prefer "delayed peaks and high ends" (Baumgartner, Sujan & Padgett 1997). Rising joy holds viewers (Teixeira, Wedel & Pieters 2012). Ads with a full five-act story were rated higher (Quesenberry & Coolsen 2014, 108 Super Bowl ads) and got more shares and views (2019, 155 viral ads). | Write the emotion line first: start feeling → end feeling. Build tension; put the relief late and end high. |
| 6 | **The mechanism before the product** | "explaining the alternative mechanism then revealing the product" | Schwartz, stage 3 markets: "A NEW MECHANISM, a new way to making the old promise work." Georgi: the mechanism of the problem says why they failed before; the mechanism of the solution says why this works. Jeremy Haynes: Meta pushes buyers to stage 4, so show the mechanism and the process. | One cause-and-effect sentence for the problem, one for the new way. Then the offer. |
| 7 | **The product lands as the fix** | "Lem lands as the fix" | The viewer already believes the new way, so the product answers a question they are now asking. | The full terms land on the last close (Close A), as the answer. |

**The contest backs move 2 up:** in Ad Games #1, all 5 of the top 5 had an explicit "it's not X, it's Y" villain or blame reframe, against 2 of the other 11 (§9a).

### Two cautions from checking the Lem angle
- **The villain must be true.** A survey of 2,056 women found "Most women (71.5%) reported having never experienced genital symptoms associated with vibrator use" (Herbenick et al. 2009). The brand's own support is narrower: a doctor quoted on its page says air pulse helps women who become "less responsive to vibration after menopause or cancer." An over-broad villain is a claim we could not make. **Our villain line is a factual claim: it needs a public source and a line in `claims-registry.md` before it runs.**
- **"Most" needs a measurement.** No study was found showing "most women think they're the problem." The closest study links blaming yourself to more distress (J Sex Med 2020). Never write "most sellers…" without a measured number.

### What does not carry over as-is
- **Two friends confessing = two customers.** Our AI avatars never play a seller or a customer (no AI labels, FTC 16 CFR 465.2 and 255). A fictional "independent podcast host" praising us would be a fake endorsement too. Compliant versions: §4, formats.
- **The late product reveal.** Our locked offer-first process needs "cash", "offer", "buy" or "sell" heard by 4.5 s, and the user's rule is a reward word first. **So in our ads the offer word is early, and the *reason it works* is what lands late.** The viewer knows by 4.5 s that we buy houses. They learn why their house was never the problem only after the tension.

---

## 2. The angle engine (do this before any hook)

Fill one card per angle. One card = one angle = one ad concept.

```
Avatar:                  [card name from research-cards.md]
False belief (self-blame): "[what they blame themselves for, in their words]"
                         Source: [card field + R/I/D tag]
Villain (real cause):    [an outside system, rule or old method]
                         Source: [public source]   Registry line: [yes / needs adding]
Absolution line:         "[It was never ___. It was ___.]"
Mechanism of the problem: [one sentence: because X, Y happens, so you feel Z]
Mechanism of our fix:    [one sentence: our way removes X because ___]
The fix (offer):         [confirmed registry terms only]
Emotion line:            [start feeling] → [end feeling]
Format:                  [presenter confession / two-voice company podcast / test or game / montage]
Signature image:         [the one picture people will remember]
Reward word for the hook: [Cash / Offer / Bonus, or J's task-removal exception]
```

**The five tests (all must pass before writing hooks):**
1. **Recognition:** the avatar nods within 1 second. It is their unspoken sentence from the card.
2. **Relief:** the absolution line takes weight off. It never adds blame.
3. **Truth:** the villain is a true, sourced cause, and it is in the registry. If it isn't, the angle waits.
4. **Bridge:** a confirmed term removes the villain. If no confirmed term touches the cause, the angle is a different ad or a false one.
5. **Ownable:** the reference ads (R1-R6) don't already say it. Check their transcripts. If a competitor says it, it isn't ours.

---

## 3. Five Property Abundance angles (from research-cards.md)

Status uses `claims-registry.md` as of origin/main `93796af`. **Verbs:** the registry froze "we buy" / "we buy as-is" and every verb that makes Property Abundance the buyer (2026-09-29). Write the confirmed condition with a neutral verb: "the sale is as-is", "the house sells as-is", "bought as-is". The approved offer name is "The Walk-Away Offer" (branding only). "Seed" hooks are starting points, not tested lines, and each follows the reward-word-first rule.

| Avatar | False belief (card) | Villain (mechanism of the problem) | Absolution | Our fix (confirmed) | Emotion line | Claim status | Seed hook |
|---|---|---|---|---|---|---|---|
| **Fran, house needs everything** | "The house got away from me, and I can't afford to catch it up." [D] | The "fix it first" rule of a retail sale: buyers who borrow need the house to pass the lender's checks, so agents say fix it first [R: card 4 lever 4] | "It was never the house you let go. It was the loan your buyer would need." | The sale is as-is. No commission, no fees, no closing costs. No obligation. | embarrassment → dignity | **Villain line needs a public source** (lender property requirements) and a registry line. The fix is confirmed. | "Cash offer for the house you stopped inviting people into." |
| **Emily, the heir** | "I want this house gone, and I feel guilty for wanting that." [I] | The clean-out-then-list routine: a listing expects an emptied, fixed, show-ready house, which turns grief into a months-long project [R: card 1 tried-and-failed] | "Wanting it done isn't giving up on them." | Belongings can stay. You pick the closing date. As-is. | guilt → permission | Fix confirmed. The villain line is general and needs wording that makes no number or speed claim. | "Cash for an inherited house, with everything still inside it." (J prefers task removal for heirs: "Don't sort it. Don't pack it. Just go.") |
| **Maya, needs out** | "I can't hold this life together through another ninety days of showings." [D] | The showing-and-waiting cycle: showings, good feedback, no offer, another price cut, while her move date stays fixed [R: card 5] | "Your house isn't the problem. The waiting is." | You pick the closing date. As-is. Belongings can stay. | dread → control | Fix confirmed. **Any speed or "can't fall through" line is not confirmed.** | "Offer on your house, and YOU pick the closing date." |
| **Jason, burned-out landlord** | "Tell me I'm not stupid, and that the loss stops being mine the day I sign." [I] | The eviction-and-attorney cycle that bills him every month while hearings get continued [R: card 3] | "You didn't fail at this. You got stuck in a process that bills you monthly." | As-is. No commission. | shame → finality | **Blocked:** buying with a tenant in place is TBD in the registry. Wait for the owner. | none until confirmed |
| **Marcus, behind on payments** | "I don't want anyone to know how bad it's gotten." [I] | Waiting: "The longer you wait the less options you have" [R], plus buyers who prey on people in trouble | Third person only: "Falling behind after a job loss happens. Hiding it is what costs people." | No obligation. As-is. | fear → calm | **High risk:** Meta's personal-attribute rule, and no foreclosure facts are confirmed. Write last. | none until reviewed |

**Order to run them:** Fran first. It is the closest match to Lem: a real outside mechanism, with "as-is" as the confirmed fix. Then Emily (J already rates task removal for heirs), then Maya. Jason and Marcus wait.

**Open conflict, ask J:** on 2026-09-29 the user allowed "bonus = the middleman fee" and "Closing in 30 days or less". J's registry blocks both: §2 freezes every "no middleman" claim, and §3 blocks "any closing timeline". Until J rules, neither goes in a script.

---

## 4. From angle to script: the beat map

The Lem arc, placed into the required nested structure. Each open plants one plain question a stranger gets on first hearing (`loop-order-rule`), and each close starts with its open's own words.

| Label | Lem move | Job | The question it plants or answers |
|---|---|---|---|
| **OPEN A** | Reward word + the confession scene | Stop the scroll. Name the offer by 4.5 s. Show the thing they're ashamed of. | "Cash for MY house? Like this?" |
| payload | The scene, dimensionalized | Make the pain a place, an object, a moment | |
| **OPEN B** | The self-blame, said out loud | Tension: "is it me?" | "Is this my fault?" |
| payload | What they tried, and why it failed | The villain at work, not yet named | |
| **OPEN C** | The villain, teased | "There's one reason ___" | "What reason?" |
| payload | Mechanism of the problem | Cause → effect, one or two sentences | |
| **CLOSE C** | The villain, named in C's words | Answer C | |
| payload | Mechanism of our fix | How our way removes the cause | |
| **CLOSE B** | Absolution, in B's words: "It was never you." | Relief: the peak | |
| payload | The catch first, then confirmed terms | Trust, then relief stacked | |
| **CLOSE A** | Pay off the hook in A's words | The fix lands | |
| payload | Risk reversal | "No obligation." | |
| **CTA** | The smallest step | "Tap the button. Answer a few questions." | |

**Rules for this map:**
- **The emotion line steers the edit.** The villain half and the relief half should feel different: tighter frames and room tone in the first half; more space, warmer light, a lift in the sound at the absolution. This is craft advice, not a measured rule; test it.
- **Mechanism lines: two sentences at most.** No lecture (Georgi). Don't explain so much that they don't need to click (Sabri).
- **The catch keeps its close.** "Truth? Cash offers usually come in lower than listing. Ours too." always comes with "That's why lower isn't everything." (registry §1).
- **CTA 1 at 30-60%.** `OFFER_FIRST_PROCESS.md` asks for a first CTA at 30-60% of the ad. The loop rule puts the CTA last. They have never been tested against each other. So one can ride in the payload after Close C as a soft ask ("Tap below. But first, here's why."), and §5 round 3 tests the two structures.

### Formats that keep the Lem effect and stay compliant

| Format | How it carries the confession | Compliance |
|---|---|---|
| **Presenter confession** | Ava or JMSN says the unspoken sentence as a question to the viewer: "Ever look at that roof and think, I let this happen?" | Company voice. Name the situation, never "you are / you have" + a trait. |
| **Two-voice company podcast** | Two Property Abundance presenters at one table, Lem's roles: one says the thing sellers won't say out loud and asks every question the viewer would ask ("Wait, they'd buy it like THAT?"); the other answers with the villain and the fix. Realism kit (§9a-9d): alternating single shots, reaction-only clips, one interruption, one object handed across the table, a fixed audio block per voice. | Both speak as the company, and any show name on the set is our own. No "independent host", no seller, no customer. |
| **Test or game** | A visual test with a scoreboard. The course's wine ad runs a 5-glass blind test with number tags (§9). Ours could tally what a retail sale asks of the seller, item by item, against what we ask. | Every item on the board must be a confirmed term or a sourced fact. |
| **Voice-over montage** | The confession and the villain carried by pictures, R2-style, one picture per phrase | People in b-roll only where the user's current rule allows them. |

---

## 5. Strategy: from angles to a test plan

### The creative does the targeting
Housing is a Special Ad Category on Meta. Age is fixed at 18-65+, all genders are included, there is no ZIP targeting, a city or pin includes a 15-mile radius, and lookalikes and detailed-targeting exclusions are unavailable (Meta Help, "About audiences for housing…"). Geography is the only hard control left. **So the first line chooses the audience:** each angle calls out its avatar's situation in the hook.

Also check the federal Fair Housing Act, 42 U.S.C. §3604(c): no housing ad may indicate a preference based on race, color, religion, sex, handicap, familial status or national origin. How it applies to a buyer's ad was not researched; ask counsel before an angle names a family situation.

### What Meta rewards now
Meta's own guidance on its newer ad system (Andromeda, 2025) is to diversify creative. "When creative is too similar, our system may not recognise it as different… creative limited or creative fatigue." "Don't: Rely on subtle shifts that maintain the same visual concept." (Meta, creative-differentiation page.) Meta has not published that hook-only variants get merged; that claim is second-hand. **So round 1 tests different concepts (angle × format), not word swaps.** Hook tests come later, and each hook variant changes the first frame and the line, not just the text.

### Test order for Property Abundance
| Round | What changes | What stays the same | Decision number |
|---|---|---|---|
| 1. **Angle** | 3 concepts: Fran, Emily, Maya, each its own angle and signature image | Format, length, CTA, offer terms | Hook rate, then hold rate, then link CTR, then cost per lead |
| 2. **Hook** | 3 openings on the winning angle: MAIN (benefit-led), CONTROL (pain-led), WILDCARD (`prompts/one-shot-script.md`) | The body | Hook rate |
| 3. **Structure** | Nested loops vs. a flat offer stack (Ref_Ads_Research §9 point 5) | Angle, hook, length | Hold rate, then link CTR |
| 4. **Format** | Presenter walk-and-talk vs. two-voice podcast vs. montage | Script | Hold rate, then cost per lead |
| 5. **CTA and offer framing** | CTA placement and wording; catch-first vs. no catch | Everything else | Link CTR, then cost per qualified lead |

One variable per round.

**Naming** (adapted from the Creative Testing Playbook in `04_Audience_Research/`): `YYMMDD_Avatar_Angle_Format_H#`, e.g. `261005_Fran_LoanVillain_Presenter_H1`.

### Hypothesis card (write it before launch, in the script file)
```
Test:        [what changes] vs [control]
We believe:  [avatar] will [stop / watch / click] because [the angle's reason]
Decides it:  [one number]          Threshold: [beat control by ___ %]
Read after:  [impressions / days / leads]  (see "How much data" below)
If it wins:  [next test]           If it loses: [next test]
```

### How much data before judging
- **Meta:** an ad set usually leaves learning after about 50 results in a week. Changing the creative or adding an ad counts as a significant edit and restarts it. A/B tests run 7 days at minimum.
- **What 50 leads a week costs** (arithmetic on third-party medians): $687 at WordStream's 2026 real-estate cost per lead ($13.74), and $6,600 at Brandon Bateman's 2021 Facebook median for investor seller leads ($132). A small budget will not exit learning, so judge creatives on hook, hold and CTR first, and on cost per lead only when there is volume.
- **Practitioner read points (opinion):**
  - Read hook rate after 2,000 impressions; it settles at 5,000-10,000 (Chris Bristow, SparkUGC, 2026).
  - Spend 2-3× the target cost per lead per creative (Bristow).
  - Kill at 0 leads after 3× the target CPL, at 1 or fewer after about 4.7×, and at 2 or fewer after about 6.3×. No decision on data under 48-72 hours old (Cedric Yarish, AdManage.ai, 2026).
- **Randomness is large.** Three identical ad sets got 100, 86 and 80 conversions (Jon Loomer, 2024). At small volume, a gap under about 25% is not a winner.

---

## 6. Reading the data: which number judges which line

Definitions are Meta's own (Meta Business Help Center, fetched 2026-10-01) unless marked.

| Number | Formula | What it judges in the script | Notes |
|---|---|---|---|
| **Hook rate** (practitioner) | 3-second video plays ÷ impressions | First frame, OPEN A, hook text | A 3-second play excludes replays |
| **Hold rate** (practitioner) | ThruPlays ÷ 3-second plays | The body: payloads, Opens B and C, tension | A ThruPlay is 15 s or the full video. On an ad under 15 s it is a completion, so don't compare it with a 30-s ad |
| **Drop-off points** | Video plays at 25 / 50 / 75 / 95 / 100% | Which beat lost them | Map these against the script's beat times (below) |
| **Average play time** | Includes replays | The body overall | |
| **Link CTR** | Link clicks ÷ impressions | The offer: Close A and the CTA | For Instant Forms, read link CTR, not outbound CTR (the form opens on Meta) |
| **Form or page conversion** | Leads ÷ link clicks | The form or page, and message match | Not a script problem unless the promise doesn't match the page |
| **Cost per lead** | Spend ÷ leads | The whole chain | |
| **Lead quality** | Qualified ÷ leads; appointments; contracts | Whether the angle attracts the right seller; follow-up speed | Meta: faster follow-up improves lead quality |
| **CPM** | Spend ÷ impressions × 1,000 | The auction and audience, not the script | |
| **Frequency** | Impressions ÷ reach | Fatigue | Meta flags "Creative fatigue" when cost per result reaches 2× past ads |
| **Comments** | read them | Emotion, objections and new customer words | Copy commenters' words into the research card as internal raw material, never as testimonials |
| **Relevance diagnostics** | quality, engagement and conversion rankings (after 500 impressions) | See §7 | |

**Benchmarks (all practitioner opinion; our own median replaces them after round 1):**

| Number | Range | Source |
|---|---|---|
| Hook rate | "20-40% is generally solid" | Motion glossary, 2026 |
| Hook rate | 30-40% baseline; under 25% needs rework | Motion blog (Wes Arai) |
| Hook rate, cold audiences | 18-28%, median about 22%; Reels 24-36%, median about 30% | AdSights glossary, DTC brands, no dataset size given |
| Hook rate | 20-30% good, 30-40%+ exceptional | Sabri Suby |
| Hold rate | 40-50% average, over 60% strong | Motion blog (Arai) |
| Hook / hold / CTR (all) | over 30% / over 20% (average watch time ÷ length) / over 1.5%; pause under 0.75% CTR | Creative Testing Playbook (Epic Ads Lab, e-commerce) |
| Real-estate lead campaigns | CTR 4.17%, CPC $1.27, conversion 9.95%, CPL $13.74 | WordStream 2026, 452 US campaigns, medians, whole real-estate industry (not cash buyers) |
| Investor seller leads | Facebook CPL median $132; 20-30 leads per deal | Brandon Bateman's 2021 client data, via Carrot |
| Investor seller leads | about 20 leads per deal; cost per deal about $3,000-3,500 | SilverStreet Marketing, Carrot podcast 2023 |

No hook-rate or hold-rate benchmark for real estate or lead gen was found.

**Map the drop-offs to the beats.** Put the script's beat start times next to the 25 / 50 / 75 / 95% play points. The beat just before the steepest drop is the line to fix. For a 30-s ad: 25% = 7.5 s, 50% = 15 s, 75% = 22.5 s.

---

## 7. Diagnose → fix → next test

Fix only the first broken step, in this order (Sabri's triage, expanded).

| What the data shows | Where the problem is | Fix in the next script | Next test |
|---|---|---|---|
| Low hook rate; the rest fine | First frame, OPEN A, hook text | New opening with a different first frame + line, same body. Check: reward word first? Situation named in under 1 s? A plain question planted? | 3 hooks (MAIN / CONTROL / WILDCARD) |
| Good hook, low hold | The body | Find the drop beat (§6). Usual causes: a payload over two sentences, a mechanism lecture, an open that plants no question, the relief arriving too early | The same hook with a tightened body |
| Good hold, low link CTR | The offer and the CTA | First CTA at 30-60%, a smaller first step, the catch said first, more confirmed terms as relief | CTA placement or wording |
| Good CTR, low form or page conversion | The page or form | Message match: the same promise and emotional temperature. Check the site works. A shorter form | Page or form, not script |
| Good CPL, poor lead quality | The angle draws the wrong sellers | A sharper situation call-out; Meta's "higher intent" form; faster follow-up | Call-out wording |
| Good, then fading | Fatigue | Practitioner rule: frequency over 2.2, or CTR down over 25% → swap the hook, presenter or format. A new concept beats a re-skin (Andromeda) | New concept from §3 |
| Negative comments | Trust | Check every claim against the registry; check the tone (sympathy theatre, hype) | Tone variant |

**Meta's relevance-diagnostics matrix** (Meta Help, "How to use ad relevance diagnostics"):
- Quality below average → the creative looks low quality: fix the production.
- Only engagement below average → "isn't spurring interest": fix the hook and body.
- Only conversion below average → "Improve the call to action… or post-click experience": fix the offer, CTA, form or page.
- Quality and conversion below average with engagement fine → "click-baity": the hook promises more than the ad delivers.

**One caution:** a practitioner (Dara Denney) treats spend, results and cost per result as the proof of a winner, and calls CTR and hold rate "storytelling KPIs". Use hook, hold and CTR to find *where* to fix. Use cost per qualified lead to decide *what wins*.

---

## 8. After every script: the next-script review (required)

Every script file ends with this block. The writer fills it in straight after the script; `ugc-reviewer` re-scores it with fresh eyes. **Every criticism quotes the line it's about.** Generic advice ("make it more engaging") doesn't count.

```
## Next-script review: [Ad N, version]

### Scorecard (1-5; quote the weakest line under each score below 4)
| # | Dimension | What a 5 looks like | Score |
|---|---|---|---|
| 1 | Stop power | Reward word first, the situation recognised in under 1 s, a plain question planted | |
| 2 | Offer clarity | "cash/offer/buy/sell" heard by 4.5 s; the whole deal clear by about 13 s | |
| 3 | Angle | False belief → villain → absolution all present, in plain words | |
| 4 | Mechanism | One cause → effect sentence for the problem and one for the fix, both sourced | |
| 5 | Tension curve | Every open plants a question; the peak is late; the end is high | |
| 6 | Trust | Catch first, every claim in the registry, no fake proof | |
| 7 | Audience fit | Their words, their situation, about 80% "you" | |
| 8 | CTA | Smallest step; CTA 1 at 30-60% and CTA 2 at the end | |
| 9 | Creativity | One signature image a viewer could describe to a friend; the format serves the emotion | |
| 10 | Realism | One fixed audio block per voice; about 180 words per minute or slower; room tone matches the place; every line passed a listening check; phone look; no AI tells (§9b-9d) | |
| 11 | Compliance | Registry, Meta personal attributes, Fair Housing, no seller or customer avatar | |

### 3 fixes for the next script
1. "[quoted line]" → [what to change, and why]
2. ...
3. ...

### Prediction (checked against data later)
Weakest number expected: [hook / hold / CTR / CPL], because [reason].
This script tests: [the hypothesis card from §5].

### Questions for the owner
- [claims to confirm before this can run]

### After launch (fill in when data arrives)
| Number | Predicted | Actual | Gap |
|---|---|---|---|
Lesson: [one line] → add it to §10's log.
```

**Why predictions:** writing down which number will be weakest, then checking it, is how the team learns whether its judgment is any good. A prediction that keeps missing means the review is scoring the wrong things.

---

## 9. Making it look and sound real: what the course and the Ad Games show

**Material (2026-10-01):** the Ad Creators Lab "AI UGC" course (19 lessons) and all 40 videos in its Arena (Ad Games #1, August 2026, animated ads; Ad Games #2, September 2026, AI podcast ads). Everything was downloaded and transcribed locally and nothing was played aloud. The files are in `07_Assets/Reference_Ads/adcreatorslab_course/` and `…/adcreatorslab_arena/` (gitignored). The full reports are `adcreatorslab_arena/ARENA_REPORT.md` and `adcreatorslab_course/COURSE_REPORT.md`, with prompts and timestamps.

Tags: [said] in the lesson audio, [screen] read on screen, [measured] by us with ffprobe, ffmpeg or Whisper.

### 9a. What separated the winners
Ad Games #1 had 16 entries; the host picked a top 5 and members voted. **This is a judged contest, not ad performance, and 16 is a small sample.**

| | Top 5 (median) | Other 11 (median) |
|---|---|---|
| Length | 56.82 s | 64.11 s |
| Cuts per 10 s | 3.61 | 3.29 |
| Words per minute | 188.8 | 172.7 |
| **An explicit "it's not X, it's Y" villain or blame reframe** | **5 of 5** | **2 of 11** |

All [measured]. The top 5's reframe lines: "she blamed it on a pea"; "drinking more plain water won't hydrate your muscle cells"; "The problem isn't your ads. It's that you keep running the same formats."; "he's not more handsome than you. He just has fuller… hair"; and a "whatever it was, it wasn't this" reveal.

What else the top 5 share:
- **The villain is a physical object on screen:** a burning laptop, mattresses with exposed springs, a melting can.
- **The old way gets a black-and-white or frozen beat.**
- **The voice starts at 0.00 s.**
- **The world fits the product:** a fairy tale that is literally about a mattress.

Two crowd favourites outside the top 5 had a story but no villain and no mechanism. One commenter told one of them: "pick one villain… close the loop".

**Round 2 (podcast ads, no winner yet):**
- **What the most-liked entries share:** two clearly different characters (a skeptic and an insider, a mentor and a mentee); the product as the answer to the other person's question; and one realism gesture beyond talking heads (pauses with hand gestures, a reaction clip, a product handed across the table).
- **The host praised exactly that:** "The product handoff is such a cool detail and makes the ad feel more natural."
- **Criticised:** "the voices are too monotonous", "a bit too nano bananay", "bad sync on the lips", position jumps between shots, music too loud.
- **11 of 16 put hook text on the first frame** (counted on the contact sheets in the Arena analysis).

Posters' own performance claims, not verified: a mattress ad "$686" spend → "$16,626" ("24× ROAS"); a podcast ad, "30 qualified leads" in "5 days"; a pet ad, "68% hook rate".

### 9b. The voice: why theirs sounds better
Three causes, then the tools.

1. **A fixed audio block per character, pasted unchanged into every clip.** Theirs, read on screen in the podcast lesson (paraphrased; the course is members-only): the accent and region, that she speaks fairly fast, that it sounds like a podcast mic with "very little echo", that the volume drops when her mouth moves away from the mic, and that she speaks assertively. It names the accent, speed, attitude, mic, room and mic distance. **Ours** (Ad 20): "a warm, bright, confident American woman around 30, natural and clear… at a natural brisk pace with no pauses".
2. **Loose, human delivery.** Their lines carry fillers ("Okay so", "Wait wait wait"), "a small laugh at the start", natural pauses, and reaction-only clips ("I seeee", "mhhhhhhhmmmm") [screen]. Our prompts ask for "no pauses" because the jump cuts remove them. **Keep** our rule of no sound after the last word: it stops the model adding words. **Test** a looser start on hooks and reactions; keep strict wording on claim lines.
3. **Pace.** Their finished ads run 168.8, 180.5 and 194.9 words per minute [measured, first word to last]. Our Ad 19 voice track ran 209.9, after capping pauses at 0.26 s and speeding it up ×1.06. **Stop speeding voices up; budget about 180 words per minute.**

**Their voice routes (all paid tools; free tiers not checked):**
- **ElevenLabs Voice Design:** describe the character *and the room* ("…in a gun store with some echo. He is an ex military male"), generate 3, and A/B them against the video's own voice [said].
- **ElevenLabs Instant Voice Clone:** from at least 10 s of the clip's own audio, with the music removed [said].
- **Eleven v3 emotion tags:** [thoughtful] [annoyed] [surprised] [excited] [fast] [screen].
- **Lip-sync:** the audio plus a still in RIZZ (on MaxFusion), under 60 s per take, starting with the mouth closed [said]. Our `kie_seedance.py` already takes `--audio` as a voice reference (it can't be combined with a first-frame image).
- **A listening pass on every line:** "I don't want it to be any second where the voice doesn't sound good" [said]. Regenerate only the bad lines.

**The room must match the place:** bathroom reverb, a car's close muffle, wind on the mic for the street ("the mic is too perfect" was the problem they fixed) [said/screen].

### 9c. The picture
- **The reference is a real phone photo** (Pinterest), edited in Nano Banana Pro by changing each face feature to "the opposite". They chose NBP over GPT Image 2 to keep the phone-lens texture [screen]. They edit in small steps ("too much in one go it looked weird"). **That conflicts with our one-shot rule; keep ours unless the user wants it tested.**
- **Consistency:**
  - the same @Image1 in every prompt;
  - "same person, same outfit, same kitchen as Segment 1";
  - the next segment starts from a frame of the approved clip (we already do this).
- **Talking video:**
  - Seedance 2.0 in 15 s, 720p segments, one action per prompt, written as 5-second blocks that say what is in frame *and what is not*.
  - "We don't want it to look too high definition." [said]
  - Kling 3.0 Pro for podcast lines.
  - Sora 2 Pro for 12 s hooks whose prompt names the format (FaceTime, "get ready with me", unboxing).
- **B-roll:** NBP stills of the same character, animated for 5 s (Kling 2.6), plus real phone footage matched on skin tone [said/screen].

### 9d. The edit
- **Build the audio timeline first, then lay the picture on it** [said].
- **Long hook, then fast cuts.** Their podcast ad: 32 cuts in 48.81 s. The wine ad: 34 cuts in 32.28 s, counted on a crop of the ad panel because the lesson is a screen recording [measured].
- **When the AI face is weak, put the talking head in a corner overlay** over b-roll or screens [said].
- **Look like a creator made it:**
  - shake added in post;
  - small plain captions (white Anton or Open Sans, 1-3 words);
  - a TikTok-style comment-reply sticker;
  - sound effects tied to actions;
  - no transitions.
  - "most creators are not gonna add these effects." [said]
- **Grade:** black-and-white for the reveal or the old way; saturation +7 [screen].
- **No music bed in the podcast ad.** Loudness: −19.7 LUFS (podcast) and −17.3 LUFS (wine) [measured]. Ours master to −14.

### 9e. What changes in our pipeline
| # | Change | Rule or test | Cost |
|---|---|---|---|
| 1 | One audio block per character (accent, age, speed, attitude, mic, room, mic distance), pasted unchanged into every clip | **Rule** | Free |
| 2 | Pace budget about 180 words per minute; no speed-ups | **Rule** | Free |
| 3 | Room tone matched to each place | **Rule** | Free |
| 4 | A listening pass per line; regenerate only bad lines | **Rule** | Kie credits for regenerations |
| 5 | Looser delivery on hooks and reactions (a filler, a laugh, a pause); strict on claim lines | Test | Free to write |
| 6 | A designed ElevenLabs voice per character, fed to Seedance with `--audio` | Test | ElevenLabs is paid; Kie credits |
| 7 | Two-voice company podcast (§4 formats) with reaction-only clips and one handoff | Test | Kie credits |
| 8 | A corner overlay of the talking head, a comment-reply sticker, plain small captions | Test in the edit | Free |
| 9 | A villain shown as a physical object, and a black-and-white beat for the old way | **Rule for angle ads** | Free in the edit; image credits if generated |
| 10 | Character b-roll (the presenter acting out a line) instead of object-only stock | Test, needs the user's OK (b-roll rule) | NBP 18 credits per image + video credits |

Every paid run still needs the cost summary and a typed go.

---

## 10. What the feedback has taught so far (Ads 15-20)

Gathered from the session files, script files and memory on 2026-10-01: 30 feedback items from the user and J, 2026-09-25 to 2026-10-01. No live ad data exists yet.

| Pattern | What happened | Rule for the next script |
|---|---|---|
| **No reward up front** | Ad 18 v1-v5 opened with a negative, a pain question, a pitch or a scene: "I don't think you have given any real psychological attention hook here." "start the hook with something positive." | First word Cash, Offer or Bonus; money, "you" and the house within 8 words; no name or company. Exception: J chose a task-removal hook for heirs ("Don't sort it. Don't pack it. Just go."), so offer one of each. |
| **Too close to the reference, or too far** | v4/v5 weakened R1's strong lines ("You are making it worse"); v7 copied R5 ("a cheap copy") | Keep the best reference's beats and psychology; write every line fresh (0 shared 4-word phrases); never weaken its power lines. When asked for better, rework the whole script. |
| **Unconfirmed promises** | v6 kept R1's mortgage, moving and speed promises: "don't make any promises that I didn't mention" | Registry terms only. Conflicts (bonus, 30 days) go to J. |
| **Wrong loop structure** | v9 had one loop: "How many times do I have to tell you?"; Ad 20 opens that meant nothing to a stranger | Three nested loops, payload after every open and close; every open a plain question; every close starts with its open's words. |
| **Instructions changed** | 7 clips instead of 3; only the changed lines shown; J's wording altered | Exact clip count and length; always the whole labelled script; J's lines are locked. |
| **Not interesting or emotional enough** | "Still not interesting enough"; "there's no human emotion" | Concrete, sensory, present-tense scenes; a feeling of "this is the only option"; legitimacy and benefits. The angle engine (§2) is the fix for this one. |
| **Hook and pictures planned apart** | J's pick for Ad 20 (2026-09-29): the hook opens on a picture with a physical action (an overstuffed drawer that won't shut, hip-checked), the line is three short beats ("Don't sort it. Don't pack it. Just go."), and Close A calls back to the same object. He kept "Cash offer…" only as the control, calling it the category's most-flagged phrase. On 2026-10-02 the user called Ad 21 v1's hooks and visuals weak: a host reading an offer line at a table, and filler b-roll (a folder, an empty counter). | Write the hook's first frame and the line together: one object that IS the problem, one physical action, a line of 3 short beats, and the same object paid off in Close A. Every b-roll shot shows the mechanism or the named thing; if a term has no picture, stay on the face with a gesture and a text pop. |
| **Looks AI-made** | "looks like it was generated with AI"; a female voice on a male character | Company voice only; hooks on the face, payload lines as pictures; one consistent voice and face; §9's methods. |

**Approved so far:** Ad 15 v2 (the honest admission), Ad 17 v11 (b-roll matched to the words), Ad 18 v8's hook line ("Hold up. Cash for your house, plus a bonus nobody told you about."), and J's Ad 20 v2.

### Log (append one row per review or result)
| Date | Ad / version | From (user / J / data) | Feedback or result (exact words or numbers) | What it means | Rule for the next script |
|---|---|---|---|---|---|
| | | | | | |

---

## 11. Sources

**Persuasion and story**
- Blair Warren, *The One-Sentence Persuasion Course* (2005), breakthroughmarketingsecrets.com PDF.
- Evaldo Albuquerque, *The 16-Word Sales Letter*, via macksbooknotes.com notes.
- Eugene Schwartz, *Breakthrough Advertising*, stage quotes via valchanova.me review (secondary).
- Stefan Georgi, "Here's how unique mechanisms work", stefanpaulgeorgi.com. Todd Brown's definition: LifterLMS podcast (UMP/UMS is not his term in any primary source found).
- Russell Brunson, *Expert Secrets*: summaries and Goodreads highlights (secondary).
- Donald Miller, *Building a StoryBrand*, via nateliason.com notes.
- Agrawal & Duhachek 2010, JMR 47(2); Duhachek, Agrawal & Han 2012, JMR 49(6).
- Baumgartner, Sujan & Padgett 1997, JMR 34(2); Teixeira, Wedel & Pieters 2012, JMR 49(2).
- Quesenberry & Coolsen 2014, JMTP 22(4); 2019, J Interactive Marketing 48.
- Walster & Festinger 1962 (secondary summary); Harkins & Petty 1987, JPSP 52(2); Deighton, Romer & McQueen 1989, JCR 16(3).
- Herbenick et al. 2009, J Sex Med 6(7); J Sex Med 2020, 17:1144-1155. Hello Nancy product pages.

**Meta, data and testing**
- Meta Business Help Center: video ad metrics, CTR, CPM, CPC, cost per result, frequency, learning phase, significant edits, A/B tests, ad relevance diagnostics, creative fatigue, housing audiences, creative differentiation (fetched 2026-10-01).
- Meta engineering blog on Andromeda (2024-12-02); Meta for Business news (2025-03-27); Marketing Brew, 2026-09-28.
- Motion (glossary and blog), Vaizle, AdSights, Foreplay, SparkUGC (Bristow), AdManage.ai (Yarish), Jon Loomer.
- WordStream Facebook ads benchmarks 2025 and 2026; Carrot (Bateman, SilverStreet).
- `04_Audience_Research/The_Creative_Testing_Playbook.webarchive` (Epic Ads Lab).
- 42 U.S.C. §3604 (Cornell LII).

**Our own files**
- `research-cards.md`, `claims-registry.md`, `prompts/one-shot-script.md` (origin/main), `OFFER_FIRST_PROCESS.md`, `04_Audience_Research/Ref_Ads_Research.md`, `offer-and-mechanism.md`, `testing-and-iteration.md`, `03-modern-creators/jeremy-haynes.md`.
- Ad Creators Lab course lessons and Ad Games entries: downloaded and transcribed locally in `07_Assets/Reference_Ads/adcreatorslab_course/` and `…/adcreatorslab_arena/` (gitignored; members-only content, so no transcripts in the repo).
