# Claims Registry

*Created 2026-09-29. The single canonical source of truth for what Property Abundance ads may and may not say.*

**Precedence rule.** Every other file in this repo defers to this one: `AD_COPY_CHECKLIST.md`, the research document, CLAUDE.md, every script and every brief. When a claim's status changes, update it HERE first, then fix the files that repeat it. If any file disagrees with this registry, this registry wins and the other file is stale. A claim missing from this file is treated as NOT CONFIRMED until it is added.

Why this file exists: scripts kept absorbing placeholder promises from competitor reference ads (offer speed, closing speed, "we show you the math") as if they were Property Abundance facts. An ad that promises what the business does not deliver is a deceptive claim under FTC Act s.5. This registry ends the guessing: a writer checks one file and knows, in one pass, which lines can ship.

---

## 1. CONFIRMED claims

Confirmed by the owner on 2026-09-25 (recorded in CLAUDE.md, Open items) unless noted. These may run in any ad. Use the approved wording or a close paraphrase that does not enlarge the promise.

| Claim | Approved wording variants | Source and date |
|---|---|---|
| We buy the house as-is | "we buy as-is" | Owner confirmation 2026-09-25; runs in Ad 15 v2 clip 3, approved by the owner the same day ("I agree with the script") |
| Belongings can stay; no clean-out needed | "Don't clean it out yet." / "That's why you don't clean it out." / "Take what matters. Leave the rest." | Owner confirmation 2026-09-25; Ad 15 v2 lines 01 and 11 |
| No commission, no fees, no closing costs | "no commission, no closing costs" / "No commissions, no fees, no closing costs." | Owner confirmation 2026-09-25; Ad 15 v2 clip 3 |
| Seller picks the closing date | "You pick the closing date." | Owner confirmation 2026-09-25; Ad 15 v2 line 10 |
| No obligation | "No obligation." / "No obligation. Show your family." | Owner confirmation 2026-09-25; Ad 15 v2 line 09 |
| A cash offer is lower than a fixed-up sale (the approved self-incrimination) | "Truth? Cash offers usually come in lower than listing. Ours too." with its close "That's why lower isn't everything" | Approved by the owner 2026-09-25 for Ad 15 v2 lines 05 and 07 ("I agree with the script") |

Rules that ride along with the confirmed set:

- The self-incrimination line works because it closes with the reframe (as-is, no commission, no closing costs). Never run the admission without its close.
- "Lower than listing" may be described in general terms (repairs, cleanout, commission, closing costs on a listed sale). Never attach numbers or percentages to the comparison; no number about it is confirmed.

## 2. NOT CONFIRMED. Never use until the owner confirms.

These are industry norms copied from competitor reference ads (the PLACEHOLDER status in `04_Audience_Research/Research_Document_Cash_Home_Buying.md`) or open owner decisions (CLAUDE.md, Open questions). They are not facts about Property Abundance. Any script containing one is blocked from production.

| Claim | Status and why it is blocked | Where it lurks today |
|---|---|---|
| Offer speed: "cash offer within 24 hours" or any offer timeline | PLACEHOLDER from refs 1, 3, 6. No owner confirmation. | Research doc Brand Information and FAQ |
| Closing speed: "close in as little as 7 days" or any closing timeline | PLACEHOLDER from refs 1, 2, 6. No owner confirmation. | Research doc Brand Information and FAQ |
| "Any condition" / "any situation" (foreclosure, bankruptcy, back taxes, liens, major work) | PLACEHOLDER from refs 1, 6. No owner confirmation. "As-is" is confirmed; "any condition" is a bigger promise and is not. | Research doc Brand Information |
| "We show you the math" / line-by-line explained offer | PLACEHOLDER from ref 2. No owner confirmation. Ad12, Ad13 and Ad14 cannot run as written because of this line. | Ad12, Ad13, Ad14 scripts; research doc FAQ |
| "We buy the house ourselves" / "no middleman" / "not wholesalers" / "we don't assign your contract" | OPEN. Depends on whether every deal closes on the company's own funds, and that question is unresolved (CLAUDE.md, Open questions). The owner voiced the intent on 2026-09-25 and Ad 15's truth check marked it confirmed, but the funds question reopens it. Ad 15 v2 line 08 ("No wholesaling. We're the buyer.") carries this claim and needs the owner's answer before Ad 15 runs. | Ad 15 v2 line 08; research doc Strategy Implications |

Also unconfirmed (TBD in the research doc, same rule applies): proof of funds on request, no price drop at closing, buying with tenants in place, buying houses in probate, which states and cities we buy in, and which legal entity the ads speak for.

## 3. BANNED. Never use, no confirmation can unlock these.

| Never say | Why |
|---|---|
| Invented numbers of any kind: houses bought, years in business, savings amounts, example offers, percentages, review counts | No number about this business has been measured. Reddit numbers in the research doc are commenter opinions, not facts. FTC Act s.5. |
| Fake urgency or scarcity: countdown timers, "only this week", invented deadlines | No true deadline exists. The checklist rule stands: scarcity only if true. |
| "Top dollar", "best price", "we pay more than anyone" | The ICP calls these lies (research doc, ICP Language Analysis), and a cash buyer cannot honestly claim them. Contradicts the approved self-incrimination angle. |
| Competitor names, in copy or on screen | Comparative claims invite legal and platform trouble and add nothing the angle needs. |
| Testimonials that are not from a real, consenting customer: Reddit quotes as testimonials, AI avatars posing as sellers, invented "I sold my house" stories | FTC 16 CFR 465.2 and 255.1. The owner also refuses AI and dramatization labels (2026-09-25), so an AI avatar may only ever speak as the company's presenter, never as a seller or customer. |
| "You are" / "you have" + a personal attribute: "you're in foreclosure", "you're behind on payments", "you inherited", "you're going through a divorce" | Meta personal-attributes policy, and housing ads are a Meta Special Ad Category. Name the situation, not the person: "Inherited a house?" passes, "You inherited a house" does not. Third-person and story framings pass (checklist Step 8). |

## 4. Before any script ships

1. Every factual claim in the script appears in Section 1 of this file, in approved or narrower wording.
2. Nothing from Section 2 appears anywhere in the script, the captions, the b-roll text or the end card.
3. Nothing from Section 3 appears, and every call-out names a situation, never "you are / you have" + an attribute.
4. The self-incrimination line, if used, keeps its close; no numbers, timelines or guarantees appear in frame or in voice.
5. This file was re-read today, not remembered: statuses change here first, and a claim not listed here is not confirmed.

## 5. Blockers

- **propertyabundanceusa.com returns HTTP 403** ("No application found", seen 2026-09-22, still failing 2026-09-25). Every CTA points there, so **no ad may send traffic until it is fixed**. Finished ads wait; they do not launch to a dead page.

When the owner confirms or rejects a Section 2 claim, or the 403 is fixed, edit this file in the same session and note the date. Then, and only then, update the scripts that were waiting on it.
