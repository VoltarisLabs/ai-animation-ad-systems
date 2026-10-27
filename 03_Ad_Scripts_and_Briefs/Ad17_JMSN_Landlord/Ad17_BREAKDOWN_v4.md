# Ad 17 v4: JMSN in the trashed rental, filmed by a camera operator

**v4 (2026-09-27):** Part C is rebuilt for a second person filming JMSN: wide, over-the-shoulder, close-up and pull-back angles instead of selfies, at the user's request.

**v4 Seedance sync (2026-09-27):**
- The takes are made with **Seedance 2.0 at 720p**: 3 takes of 8 s = 24 s. Each takes 2 cropped reference images of JMSN and no first frame.
- To fit 8 s, **take 3 is cut from 23 to 19 words**: "Our offer's LOWER than a fixed-up sale. No commission, no fees. They left. That's how YOU leave. Tap below." It drops "But you pay" and "too". Status: **proposed; user reply 'yeah', explicit confirmation requested before take 3.** The offer line needs the same explicit yes.
- Words: 19 / 18 / 19 = 56.
- Everything else is v3 unchanged.

v3 reruns Ad 17 through `11_Psychological_Hooks/` in the README's order: Research, Offer, Write, Test and the AI passes. Every step's output is shown below. The deliverable is still the four-part breakdown (Parts A-D), built from these steps.

**Speaker:** JMSN, Property Abundance's buyer, in the company voice. He is never a landlord, seller or customer, so no AI label is needed.
**Fixed:** the 3 locations (L1 front porch and door, L2 wall hole, L3 ceiling leak), 3 takes of 8 / 8 / 8 s (Seedance 2.0, 720p) filmed by a camera operator, two nested loops, about 3 cuts per 10 s at sentence starts, and confirmed claims only.
**Status:** script and storyboard. No video take has been generated.
- **36 credits are already spent:** 2 × 18 on the v3 selfie scene images L1 and L2 (the logs record `creditsConsumed` 18.0 each).
- Those images are superseded and not used, because the takes use reference images, not first frames.

## Result in one table: what v3 changes from v2, and which step drove it

| Change | Driven by |
|---|---|
| **The spoken dialogue is unchanged in v3** (19 / 18 / 23 = 60 words; the v4 Seedance sync cuts take 3 to 19, for 56). Each line was re-derived and backed by the process (Part B "why it stays"). | All steps; the copy chief pass (Appendix §5) found no line worth the swap |
| The main hook stays "The tenant left. Now YOU can too." It is not the top scorer (#6 scored 22 to its 21). It is the hook written from the **root desire** (finality). | Research §4b (write hooks from the root) |
| 20 hooks were written, up from 10, across the 10 hook-generator types, and each was checked against the kill checks and scored | Write step: `prompts/copy-prompts.md` §3, `hook-formulas.md` |
| 3 alternate hooks instead of 2. H3 is new ("Before the contractor, get the AS-IS number.", 22/28) and H4 is new ("Walking away from THIS isn't giving up.", the soft angle of the root desire). v2's H3 ("Not a repair problem. An EXIT problem.", 20) is held in reserve. | `video-scripts.md` Short-form rule 10 and Script QA ("3 alternate hooks"); Research §4b (one bold and one soft angle on the root) |
| **Named template: #5 Us vs. Them**, over #7, #11 and #12 | Write step: `templates/video-scripts.md`, the Step 1 table in `frameworks.md` / the checklist |
| Text pops are now in sentence case with no periods. "They left" + "That's how you leave" became one echo pop, "Your turn to leave". The end card is split into "Ask for my offer" + "No obligation" (each pop is 5 words or fewer). | `video-scripts.md` On-screen text rules |
| A Reels safe zone for every text pop and caption (y 269-1248 px of 1920, 65 px side margins) | Short-form rule 6 |
| A 4-column script sheet was added (Part C) | Script QA ("Written in the 4-column script sheet") |
| **Second click: FAIL, measured live** (see §6). It is added to the blockers. | Research §6 |
| Funnel decision: a direct ask now, a two-step "lower the first ask" as test 3, and a first reply that teaches | Offer §4 |
| 3 follow-up texts drafted | Offer §5 ("Done when") |
| A new source of pasted market words: 11 landlord lines taken verbatim from the raw research file | Research §1-§2 ("paste, don't paraphrase") |
| Test plan and winner log | `testing-and-iteration.md` §3, §4, §10 |
| The Objection Obliterator found 2 objections the ad ignores (wholesaler, price drop at closing) and 1 it can't answer (proof of funds). They go to the page and the first reply, not the ad. | `prompts/copy-prompts.md` §1b |

**Location check:** no playbook step requires a location change. §7 "the pain is shown, not listed" and Short-form rule 2 (the first frame shows the problem object) are both met by L1, L2 and L3. The image prompts stay valid.

---

# STEP 1. RESEARCH (`research-playbook.md`)

## §1 Mine the market's own words
Sources:
- `04_Audience_Research/Research_Document_Cash_Home_Buying.md`: 17 Reddit Answers responses and 170 threads, collected 2026-09-22.
- The Buyer_Avatar files.
- **New in v3:** a mining pass on `Cash_Home_Buying_RAW.txt` (4,511,885 bytes), searching for sentences where tenants, landlords or rentals appear with damage, mortgage, vacant or mess words.

Internal only: these quotes shape lines and are never shown or voiced. One raw line that names a tenant's family status was left out on purpose (Fair Housing guard).

## §2 Worksheet: Burned-Out Landlord, tenant gone, rental trashed
```
Audience + moment:  side investor with a day job; the tenant is finally out, the rental is trashed
                    (holes, junk, a leak), the house is empty and the mortgage keeps coming.
Pains (their words):
  "Bleeding money for months on an attorney is gutting me."                        (research doc, r/Landlord)
  "a ton of damage and multiple months of missed rent"                              (raw file)
  "...put multiple holes in a new-build rental, yanked all the blinds out of the wall, and destroyed the drains"  (raw file)
  "some water damage is visible in the drywall"                                     (raw file)
  "This house has drained my energy, finances, health, and happiness."             (research doc)
Fears (their words):
  "Many 'cash buyers' now are just wholesalers who tie you up in contract..."       (research doc)
  "I filled out their form online, they sent someone out, and then offered me pennies."  (research doc)
  "2 months later they offered 10% less than originally quoted..."                  (research doc; number internal only)
Wants (their words):
  "Get out, tenant and all."                                                        (persona 3 desire)
  "Cut out all the bullshit."  /  "I just wanted it SOLD."                          (research doc)
  "as-os and no showing matter when the house is a mess or tenants wont leave."     (raw file, spelling as posted)
What he tried, and why it let him down:
  re-rent  -> "could just turn into another thing on my plate"                      (research doc)
  fix first -> "No money, time or energy to manage contractors."                    (research doc, table)
  list as-is -> "Buyers still inspect, bring a repair list and renegotiate."        (research doc, table)
  sold after one bad tenant -> "I sold my rental shortly after my first non-payment and dog damage."  (raw file)
Never says out loud:  "I told people this was a good investment, and now I just want it to stop being mine."  [inference, Hook Map]
His words for it:     eviction, cash for keys, bleeding money, attorney fees, non-paying tenant, court date,
                      "cut my losses", "play landlord" ("I do not want to play landlord from another state", raw file)
Awareness level:      Solution-aware (see §3)
```
**Word check:** the Hook Map lists "turn" as his word, but it doesn't appear as a noun in any pasted quote, so the script doesn't use it.

## §3 Awareness gap (Georgi). A rough estimate by inference, not measured.

| Level | Share of this moment | Why |
|---|---|---|
| Unaware | Very small | He is standing in the damage |
| Problem-aware (knows it's trashed, assumes he'll fix and re-rent) | Some | The default landlord move |
| **Solution-aware** (knows the roads: re-rent, fix and list, list as-is, a cash buyer) | **Most** | The research lists every road as tried. Hook Map: "has already considered cash buyers". |
| Product (category) aware (has seen "we buy houses" ads) | Large overlap with the row above | Jeremy Haynes: Meta pushes everyone to Stage 4 |
| Most aware (knows Property Abundance) | About none | The name search finds the UK company (§6) |

**Levels to move:** about one, from solution-aware to a request. By §3, that means a **short ad plus a direct page**. Because selling a property is a big decision, the page has to carry the mechanism and the proof (Offer §4).

## §4 Dimensionalize: 10 scenes (internal; the ad uses the ones marked ▶)
1. ▶ The fist-size hole in the living room drywall at head height (L2, "Patch THAT").
2. ▶ The brown ring on the bedroom ceiling above his head (L3).
3. ▶ The mortgage payment that still clears every month on a house with nobody in it ("Same mortgage, every month").
4. ▶ Trash bags and a broken chair left by the front door (L1, picture only).
5. Blinds yanked out of the window frame.
6. Standing in the doorway with the keys, deciding whether to call a contractor or a realtor.
7. The contractor's quote on the kitchen counter.
8. ▶ The FOR SALE sign he'd have to put up after the work (the scene 5 b-roll).
9. Strangers walking through on a Saturday showing.
10. The text thread with the last tenant, still on his phone.

## §4b Ladder the desire
"Get out" → why? → to stop paying for an empty, trashed house every month → why? → to get his time and weekends back from contractors and tenants → why? → **root: finality, and the dignity of making the adult call** (the Hook Map's hidden desire is that the loss stops being his; its [R] belief is "Cutting my losses fast is the adult move").
- **Bold angle on the root:** "The tenant left. Now YOU can too." (finality). This is **H1, main**.
- **Soft angle on the same root:** "Walking away from THIS isn't giving up." (permission). This is **H4, new**.

## §4c The lever: emotion or curiosity
- **H1 is emotion-led:** the remembered relief of the tenant finally leaving, turned toward himself. It carries a curiosity loop (how can I leave too?).
- The mechanism (sell it as-is, lines 6-8) is the payoff of that itch, and it arrives only after the itch is built. §4c: "build the itch before you reveal it". ✓

## §5 Bullseye desire
**"Get out"** (persona 3), the research doc's "Just be done with it". One bullseye. The other wants (a fair explained price, protected credit) are other ads.

## §6 Second-click pre-check: **FAIL** (measured live, 2026-09-27)

| Check | Measured |
|---|---|
| `http://propertyabundanceusa.com/` | **HTTP 403, body "No application found"** |
| `https://propertyabundanceusa.com/` | curl: "SSL certificate problem: unable to get local issuer certificate". The server presents a **CloudFlare Origin Certificate** (issuer "CloudFlare Origin SSL Certificate Authority"). That kind of certificate is meant for Cloudflare-to-server traffic, not for browsers, so a visitor gets a certificate error. With the check skipped, the page still returns 403. |
| DuckDuckGo, "Property Abundance", top 10 | All 10 are the **UK training company** or unrelated. That covers propertyabundance.info (twice), Trustpilot (twice), Facebook (twice), Instagram @property_abundance, UK Companies House "PROPERTY ABUNDANCE LIMITED" and onecourseaway.co.uk, plus a D&B listing for "Property Abundance Global LLC". **No US cash-buyer result.** |
| Third-party proof (Google Business Profile, reviews, photos) | None found in the search above |

The §6 rule: "If the second click is empty, fix it before you spend more." **This is a blocker for any spend**, not for generating the clips.

## §6b Five angles (Jeremy Haynes)

| View | Status |
|---|---|
| 1. Customers' | Not possible yet: the project has no closed-deal reviews or seller feedback. **User task** once deals close: ask happy and unhappy sellers. |
| 2. AI's | I have no record of a US Property Abundance cash buyer, and the live search above shows only the UK company. **User task:** ask ChatGPT and Gemini "What do you know about Property Abundance?" and "cash home buyers in [city]". The city is TBD in the research doc. |
| 3. The algorithm's | After launch only. **User task:** a burner account, to see whose ads appear next to ours. |
| 4. Secret shopping (from the refs this project measured) | Competitors lead with speed and numbers (housecashin: "24 hours", "seven days"), with "I'm an actual buyer, not a wholesaler" (quick_close), and with "If your house looks like this" (bright_future; s18: "Even if your house looks like this"). Property Abundance can't claim speed. Its honest edges are the admission and the landlord moment. **Proof is the missing differentiator.** |
| 5. Ours (last) | Honest and specific to the moment, but no proof, no working page, and a name that searches to another company. |

## §7 Swipe what is scaling now
- **Limit:** the Meta Ad Library pass has to be done by hand (Meta's terms bar automated collection; see the open items in `07_Assets/Reference_Ads/Reference_Videos_for_House_Buying.md`).
- **Also:** views are not results. No ad in the set has spend or lead data.
- **What the measured refs give Ad 17:**
  - **HomeVestors "What Could Go Wrong"** (r07, 140,739 views; r09, 40,927): "the other ways to sell are bad ideas". That is the **structure** of Ad 17's body: the two roads as questions, then the third road. Steal the structure, never the words: "What could go wrong" and "We Buy Ugly Houses" belong to them.
  - **Part 2, shared pattern:** "The pain is shown, not listed." The damage lives in the L1/L2/L3 pictures, not in a spoken list. Ads that read out "no repairs, no fees, no showings, no commissions" "look like every local TV ad", so Ad 17's terms stop at two: "no commission, no fees".
  - **s18 and bright_future:** "looks like this" is common in this category, so hooks built on it score low on Unique (#7, #8 in v1).
  - **r17** (15,500 views, not an ad): the skeptic's "20 percent less" line is an objection the viewer has already heard. The admission ("Our offer's LOWER than a fixed-up sale") gets there first, with no number.
  - **Pace and cuts:** the vertical refs' median pace is 197.1 wpm. Talking-head ads in the competitor cut analysis run 2.97 cuts per 10 s; Ad 17 plans 3.19 (v4 estimate, 7 cuts in about 21.9 s).

## Research "Done when"
- [x] A worksheet for the audience, full of pasted phrases.
- [x] An awareness level and a bullseye desire.
- [x] Ten dimensionalized scenes.
- [ ] **The second-click check passed. It FAILED** (§6). It is a blocker for spend.

---

# STEP 2. OFFER (`offer-and-mechanism.md`)

## §1 The mechanism in three questions
1. **Why does he have the problem?** Both usual ways out of a trashed rental start with fixing it. Re-renting needs a finished unit for the next tenant, and a retail sale needs a finished house for a buyer's lender and inspector. The mortgage runs the whole time.
2. **What has he tried?** Re-renting, fixing and listing, listing as-is (still inspected and renegotiated), and evicting through the courts. See the worksheet.
3. **Why did that fall short, and how is this different?** Every one of those roads needs someone who wants a finished house. Property Abundance buys it as it stands, so the fix-first step disappears.

**In two sentences:**
- *Problem:* every usual way out of a trashed rental runs through fixing it first, while the mortgage keeps coming.
- *Solution:* sell it as-is to a buyer who takes it as it stands, so there is no fix-first step.

**Plain names:** the problem is **"the fix-first trap"**. The solution is **"the as-is exit"**; the ad says it as "Or sell it AS-IS."

**Held back** (§1: don't give the whole mechanism away): the ad names the what (as-is, our offer, no commission, no fees). The page gives the how.

## §2 Honest offer stack (confirmed terms only)

| Part | Ad 17 | Status |
|---|---|---|
| Rationale (why the offer is what it is) | Not stated in the ad. How Property Abundance prices or profits is not confirmed, and showing the offer math is not confirmed. | Left out on purpose |
| Value (what he no longer does or pays) | No repairs (as-is) · no commission · no fees or closing costs · his own belongings can stay · he picks the closing date | Confirmed (CLAUDE.md 2026-09-25) |
| Price and terms against the real alternative | "Our offer's LOWER than a fixed-up sale", set against fix-and-list (repairs, then commission) and re-rent (another tenant) | **User to confirm:** used in Ad 16 final + Ad 15 v2 approved script; not on the CLAUDE.md confirmed list |
| Bonuses | None confirmed | Left out |
| Risk reversal | No obligation | Confirmed |
| Scarcity | None real | Left out (§2: never invent one) |

**Proof and offer trade off** (Sabri): with no proof yet, the offer and the admission carry the ad. Real proof (a real past purchase, filmed with the seller's consent) is the biggest single upgrade (Appendix §9a).

## §3 The catch, said first
"Our offer's LOWER than a fixed-up sale." It opens clip 3 as its own sentence, right after the answer "Or sell it AS-IS." Its status is user to confirm (above).

## §4 Funnel by awareness gap and price
- **Shape:** solution-aware and a big decision, so the ad goes to a page with the mechanism and proof, then to the action (the §4 table). The one-level gap supports a short ad (Research §3).
- **Lower the first ask** (Sabri's real-estate rewrite): a no-contact guide before the offer request suits cautious sellers.
  - This landlord is "the closest to ready", "wants a number and an exit", and process language kills the hook for him (Hook Map). So the primary CTA stays direct: **Ask for my offer · No obligation**.
  - The two-step becomes **test 3** (Step 5), and only once a no-contact guide exists. Its working name: "Re-rent, fix and list, or sell as-is: a landlord's side-by-side" (no numbers).
- **Sensitive situations:** the ad names the broad moment (tenant gone, house trashed and empty), never a trait of the person. The page explains specifics.
  - **Meta's Housing Special Ad Category** must be set when the campaign is created, and it limits targeting. So the hook itself has to qualify (the word "tenant"), as swipe-file #8 notes.
- **Speed and the gap after the click** (Jeremy Haynes): shorten the time between the request and the conversation, and make the first reply teach (§5, text 1). **No speed claim in the ad.** Reply speed is an operations target, not a promise.
- **Congruence:** the page and the first reply keep the ad's promise ("the tenant left, now you can too"), its blunt, calm temperature, and its admission.

## §5 Follow-up: first three texts, drafted
They are about 80 % value and 20 % ask, with no deadlines. The timings are suggestions, not claims. Sales team only, never in the ad.
1. **Right after the request (teach the process):** "Thanks for the details on the rental. Here's how an as-is sale works with us: you don't fix, clean or list anything, you pay no commission and no fees, and you pick the closing date. Our offer will be lower than a fixed-up sale, and you're under no obligation. When's a good time for a short call?" *(The "lower" line waits on your confirmation.)*
2. **A few days later (a real mini-result: the comparison):** "One way to size up the rental: re-rent it (repairs plus a new tenant), fix and list it (repairs plus commission and showings), or sell it as-is (no repairs, no commission, a lower price). Which of those fits what you want?"
3. **Later (honest admission, no pressure):** "No rush. If fixing and re-renting fits you, that's a real option. If you'd rather be done with it, reply 'offer' anytime."

Sabri says his most valuable buyers converted 90+ days after first contact (his claim). Plan the follow-up to run that long.

## Offer "Done when"
- [x] The mechanism is written in two sentences and has a plain name.
- [x] Every line of the offer stack is true and deliverable. The "lower" line is user to confirm.
- [x] The catch is written down and said first.
- [x] The funnel shape matches the awareness gap.
- [x] The first three follow-ups are drafted.

---

# STEP 3. WRITE

## 3a. 20 hooks (`prompts/copy-prompts.md` §3, 2 per type, 12 words or fewer, benefit-led in 10)
Kill checks are from `testing-and-iteration.md` §2: announce · blind curiosity · solvable without the click · accuse · copyable · body doesn't pay it off · closes in the ad. Scores use the checklist's 7-point score (Useful, Urgent, Unique, Ultra-specific, New, Easy, Safe; 1-4 each), keep at 20/28 or more. All scores are my judgment, not measured.

Every hook's first frame is **L1**: JMSN just inside the open front door, the messy front room behind him. "Twin" gives each pain-led hook's benefit-led partner.

| # | Type (generator) | `hook-formulas` | Lead | Twin | Hook | On-screen text | Kill checks | U | Ur | Un | Sp | N | E | S | Total | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Curiosity + benefit | #47 | Benefit | of 10 | "The tenant left. Now YOU can too." | Tenant left, you can too | Copyable: borderline | 3 | 2 | 3 | 3 | 4 | 3 | 3 | **21** | **Keep: H1 main** |
| 2 | Curiosity + benefit | #47 | Benefit | of 11 | "One way out of a trashed rental that skips the repairs." | Skip the repairs | Copyable: **fail** | 3 | 1 | 2 | 3 | 2 | 4 | 3 | 18 | Cut |
| 3 | Contrarian | #17, reframe | Pain | 20 | "Not a repair problem. An EXIT problem." | Not a repair problem | Copyable: borderline | 3 | 2 | 3 | 2 | 4 | 3 | 3 | 20 | Reserve (v2's H3) |
| 4 | Contrarian | #19 | Pain | 17 | "Don't fix it for the NEXT tenant." | Don't fix it for them | Pass, but it clashes with body line 4 | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 18 | Cut |
| 5 | Common mistake | #56 | Pain | 6 | "Patching it first is the move-out mistake." | The move-out mistake | Accuse: borderline | 2 | 2 | 3 | 3 | 3 | 2 | 2 | 17 | Cut |
| 6 | Common mistake (don't do X until) | #19, #53 | Benefit | of 5 | "Before the contractor, get the AS-IS number." | Before the contractor | Copyable: borderline | 4 | 3 | 2 | 3 | 3 | 4 | 3 | **22** | **Keep: H3** |
| 7 | Testable self-check | #46 | Pain | 8 | "Look behind me. If yours looks like this, don't re-rent it yet." | If yours looks like this | Copyable: **fail** (bright_future, s18) | 3 | 2 | 1 | 3 | 1 | 3 | 2 | 15 | Cut |
| 8 | Testable self-check | #46, #65 | Benefit | of 7 | "Ask yourself: fix it again, or be done with it?" | Fix it again, or be done? | Pass | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 19 | Cut |
| 9 | Story in motion | #69 | Pain | 18 | "Tenant's out. Keys on the counter. And THIS." | And this | Blind curiosity: **fail** | 1 | 1 | 3 | 4 | 3 | 1 | 1 | 14 | Cut |
| 10 | Story in motion | #51 | Pain | 1 | "Last tenant's gone. The mortgage didn't go with them." | The mortgage stayed | Pass (no benefit) | 2 | 3 | 3 | 3 | 3 | 2 | 2 | 18 | Cut (its idea is body line 2) |
| 11 | Mocking the obvious | #48 | Pain | 2 | "'Just patch it and re-rent.' Sure. Until the NEXT one." | Just patch it? | Pass, but it clashes with body line 4 | 2 | 2 | 3 | 3 | 3 | 2 | 2 | 17 | Cut |
| 12 | Mocking the obvious | #48, #60 | Benefit | of 16 | "Everyone says fix it up first. You don't have to." | You don't have to fix it | Copyable: borderline | 4 | 2 | 2 | 2 | 2 | 4 | 3 | 19 | Cut (New 2: Ad 16 ran "You fix NOTHING") |
| 13 | Binding statement | #49 | Pain | 14 | "Nobody buys a rental hoping to patch THIS." | Nobody signs up for this | Pass | 2 | 1 | 3 | 3 | 3 | 2 | 2 | 16 | Cut |
| 14 | Binding statement (permission) | #49 + Hook Map lever 6 | Benefit | of 13 | "Walking away from THIS isn't giving up." | Walking away isn't quitting | Copyable: borderline | 3 | 2 | 3 | 3 | 4 | 3 | 3 | **21** | **Keep: H4** |
| 15 | Gross reveal | #50 | Pain | 19 | "That's what they left you." (pans to the mess) | Look what they left | Blind curiosity: **fail**; it also points at the tenant's leftovers | 1 | 1 | 3 | 3 | 2 | 1 | 1 | 12 | Cut |
| 16 | Gross reveal → relief | #50, #6 | Pain | 12 | "What the tenant broke? Not YOURS to fix." | Not yours to fix | Copyable: borderline | 4 | 2 | 3 | 3 | 2 | 4 | 3 | **21** | **Keep: H2** (pain-led) |
| 17 | Burning question | #65 | Benefit | of 4 | "Re-rent it or sell it? Only one of those ends it." | Only one ends it | Pass, but it asks Open B's question twice | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 20 | Cut: it clashes with the body |
| 18 | Burning question / call-out | #64, market words | Benefit | of 9 | "Done playing landlord? The tenant left. YOU can too." | Done playing landlord? | Accuse: **borderline**. "Playing" can read as calling him an amateur, which pokes the Hook Map core wound (humiliation). The raw quote came from a remote owner, not a burned-out landlord. Clip 1 would be 21 words, over the 20 limit. | 3 | 2 | 3 | 4 | 4 | 3 | 2 | 21 | Cut: kill check and word limit |
| 19 | Drawback first | #57 | Benefit | of 15 | "It's less than a fixed-up sale. It's also the end of it." | Less, and done | Pass, but it repeats body line 7 | 3 | 1 | 3 | 3 | 3 | 3 | 4 | 20 | Cut: it clashes; saved for an admission-led ad |
| 20 | Drawback first | #57 | Benefit | of 3 | "Less than a fixed-up sale. A lot less work." | Less, but less work | Copyable: borderline | 3 | 1 | 2 | 2 | 3 | 4 | 4 | 19 | Cut |

**The copyable check at one bar:** every hook here names the landlord's moment, but none says anything only Property Abundance could say. So every survivor is **borderline** on the copyable check, not a pass. Hooks that don't even carry the moment (#2, #7) fail it.

## 3b. Kept: main + 3 alternates (the body stays identical; each swap re-makes clip 1 and clip 3)

| # | Hook | Lead | Score | Close A | Clip 1 / clip 3 words (script) | Why it's here |
|---|---|---|---|---|---|---|
| **H1 main** | "The tenant left. Now YOU can too." | Benefit (bold root) | 21 | "They left. That's how YOU leave." (v4: "too" dropped) | 19 / 19 | The root desire (§4b), the bullseye (§5), New 4 |
| H2 | "What the tenant broke? Not YOURS to fix." | Pain | 21 | "So what they broke? Not YOURS." | **20** / 19 | The benefit-vs-pain test against H1 |
| H3 | "Before the contractor, get the AS-IS number." | Benefit (surface want) | **22** | "So get the as-is number FIRST." | 19 / 19 | The top scorer. It speaks to his wish for "a number". It is a challenger, not the main, because it comes from the surface want, not the root (§4b), and the "number" wish is backed only by the README's representative voice. |
| H4 | "Walking away from THIS isn't giving up." | Benefit (soft root) | 21 | "That's walking away, not giving up." | 19 / 19 | §4b: one bold and one soft angle on the same root |

**Top 3 by score:** H3 22, H1 21, H2 21 (H4 is also 21). H1 stays main by the §4b rule, not by the score.
- H2's clip 1 is at the 20-word limit, so word-diff it first. Its last line is Open B.
- H3's "AS-IS number" means the offer amount. It shows no figure and promises no timeline.

## 3c. Fascinations (Georgi): for the primary text, not the video (the spoken budget is full)
Alpha, in the first line of the Meta primary text:
- "Why the 'fix it first' step is optional."
- "What you skip when you sell it as-is: repairs, commission, fees."
- "The honest catch: our offer's lower than a fixed-up sale." (user to confirm)

Omega, near the CTA: "No obligation. You pick the closing date."

Every claim here is on the confirmed list except the flagged one.

## 3d. Hooks by awareness level
The Step 1 table's Solution-aware row says open with the result or the mechanism, using result, how-to or proof hooks.
- H1 is a result hook (you get out).
- H3 is a how-to hook (get the as-is number first).
- There are no proof hooks, because no proof exists yet.

## 3e. Template: **#5 Us vs. Them** (`templates/video-scripts.md`)
- **The Step 1 table** (which `frameworks.md` "Which framework when" points to) gives Solution-aware: AIDA/BAB, video templates #4 demo and #2 UGC testimonial. It gives Product-aware: FAB, #5 Us vs. Them and #7 Objection-buster.
- **Both Solution-aware templates are ruled out:**
  - #2 would put a customer's voice on an AI avatar (the no-AI-label rule).
  - #4 has no confirmed process to demo, because the offer math is not confirmed.
- **The category-aware reading is the right one:** Research §3 says to "read product aware as category aware", and Jeremy Haynes puts everyone at Stage 4. So the Product-aware templates apply, with the BAB spine from the Solution-aware row:
  - Before: the tenant left, the house sits empty, same mortgage.
  - Bridge: the two roads, then "or sell it as-is".
  - After: "That's how you leave".

| Candidate | Fit | Verdict |
|---|---|---|
| **#5 Us vs. Them** (20-30 s) | "Most [alternatives] [flaw]. We [different approach], so you [benefit]. [Proof]. [CTA]." Ad 17 attacks the two alternatives (re-rent, fix and list) as questions, never a named company. Then "we" (our offer, as-is), so you (no commission, no fees, you leave). It matches Jeremy Haynes' "sell against the alternatives" and the HomeVestors structure (§7). | **Picked.** Its [Proof] slot is empty (none exists), and that gap is logged. |
| #7 Objection-buster | It needs "'[a top worry, quoted from a real customer]' That's the #1 thing we hear." There is no customer quote, and "#1 thing we hear" would be an invented claim. It is also built for retargeting. | Rejected. Use it for retargeting once real seller quotes exist. |
| #11 The rival's promise, destroyed | "They told me [promise]..." is a first-person story. JMSN would drift into the seller's role, and its "[time] later" beat pulls toward a timeline. It also needs proof. | Rejected for company voice |
| #12 The honest exposé | 30-45 s, with a "put it to the test" beat. At 56-60 words and about 22-23 s there is no room for the test. | Rejected on length. It's a good fit for a longer Ad 17 cut. |

## 3f. Short-form rules (`video-scripts.md`), applied

| Rule | Result |
|---|---|
| 1. Three-layer hook by 2 s | Visual: L1 doorway mess, from 0 s. Text: "Tenant left, you can too", from 0 s. Spoken: "The tenant left." ends at about 1.1 s, and "Now YOU" is heard by about 1.8 s (estimate at 0.365 s/word). ✓ |
| 2. First frame is the thumbnail | JMSN's face plus the problem objects (bags, broken chair) ✓ |
| 3. Sound off | Burned-in captions plus text pops. See the sound-off test. ✓ |
| 4. Change every 1-3 s | 7 cuts. The text pops keep every gap at 2.555 s or less (Part C). ✓ |
| 5. One idea, one CTA | One idea (get out of the trashed rental), one CTA ✓ |
| 6. Safe zone (Reels) | Keep the top 14 %, bottom 35 % and 6 % of each side clear. On a 1080 × 1920 frame, text and captions sit between y 269 and 1248 px, at least 65 px from each edge. Text pops go in the upper band (about y 290-520), captions in the lower band (about y 1000-1240). Both stay off his face. **New in v3.** |
| 7. Look native | Phone footage shot by a second person (like bright_future and zion_fast), a real-looking room, natural light ✓ |
| 8. Length | About 21.9 s (v4 estimate) ✓. Cut a 6-10 s version of the winner for Stories: hook, then "Or sell it AS-IS.", then "Tap below." Build it from the finished clips; no new generation. |
| 9. End card | The last 2.23 s: spoken "Tap below." plus "Ask for my offer" / "No obligation", with a small logo ✓. The rule's "reason to act now" is left out: no real urgency exists. |
| 10. 3 alternate hooks | H2, H3, H4 ✓ (**new in v3**; v2 had 2) |
| 11. Super Bowl lessons | "Who it's from ... in about 2 seconds with the sound off": **departure.** The brand appears only on the end card, per your Ad 16 call ("no company name in clip 3"). One option for you to decide, not applied: a small logo in a corner from 0 s. The other three lessons are met: the most common real use, one audience, and a CTA in the same tone. |

## 3g. On-screen text rules, applied (the v3 text changes)
- **Sentence case, no periods:** v2 used ALL CAPS with periods. Captions, a separate layer, stay in your dynamic-captions style.
- **3-5 words per pop:** v2's end card had 6 words ("ASK FOR MY OFFER · NO OBLIGATION"). It is now two lines: "Ask for my offer" (4) and "No obligation" (2).
- **Echo, don't transcribe:** "They left" + "That's how you leave" (a transcription) became one echo, **"Your turn to leave"**.
- **The claim pop keeps its exact words:** "Lower than a fixed-up sale". Paraphrasing a claim risks changing it.
- **Minimum time on screen** (1.5 s per 5 words): every pop meets it. The shortest is "Next tenant?" at 1.095 s for 2 words, where the rule needs 0.6 s.

## 3h. Script QA before recording
- [x] Written in the 4-column script sheet (Part C, new).
- [x] Three-layer hook in 0-2 s.
- [x] Hook works with the sound off ("Tenant left, you can too").
- [x] A cut or text change every 1-3 s.
- [x] Text inside the safe zone.
- [x] 3 alternate hooks.
- [x] First frame interesting as a still.
- [x] One idea, one CTA.
- [x] Word count fits the length: 56 words at 2.5 words per second = 22.4 s, against an estimated 21.9 s (v4).
- [x] All words added in the editor, never in an AI prompt.
- [x] Kill checks and beat-by-beat check (Appendix §7, §9).
- [x] `AD_COPY_CHECKLIST.md` (Part D).

---

## Part A. Research card (from Step 1; internal only)

| Field | Content |
|---|---|
| Audience + moment | Persona 3. The tenant is finally out, the rental is trashed and empty, and the mortgage keeps coming. |
| Awareness | Solution-aware, read as category-aware, at Stage 4 (Step 1 §3) |
| Bullseye desire | "Get out" (Step 1 §5). Root: finality and the dignity of the adult call (§4b). |
| Top pain | "Bleeding money for months on an attorney is gutting me." · "a ton of damage and multiple months of missed rent" |
| Top fear / objection | Lowball ("offered me pennies"), wholesaler, a price drop late in the deal (Appendix §1b) |
| What he's weighing | Re-rent, fix and list, list as-is (Step 1 §2) |
| Unspoken sentence | "I told people this was a good investment, and now I just want it to stop being mine." [inference] |
| Scenes | Step 1 §4. The ad uses 1, 2, 3, 4 and 8. The **bucket under the ceiling stain is a research scene, not in frame**: the L3 take opens on a close-up that doesn't show the floor. The v4 pull-back could reveal a bucket if you want one. |
| Mechanism | The fix-first trap → the as-is exit (Step 2 §1) |
| Confirmed claims | Buys as-is · belongings can stay · no commission · no fees or closing costs · seller picks the closing date · no obligation · Property Abundance buys the house itself (not a wholesaler) (CLAUDE.md, 2026-09-25) |
| **Claim to confirm** | "Our offer's lower than a fixed-up sale": **used in Ad 16 final + Ad 15 v2 approved script; not on the CLAUDE.md confirmed list; user to confirm.** Ad 15 v2 said "Cash offers usually come in lower than listing. Ours too." |
| Used in the ad | As-is · our offer is lower than a fixed-up sale (user to confirm) · no commission · no fees · no obligation (end card) |
| Banned | Numbers, price, timeline, speed, scarcity, the offer math, buying with a tenant inside, eviction or legal help, promises about the tenant's leftovers, competitor names, "any condition", "top dollar", personal-attribute lines |
| Discrepancy | "We buy it ourselves": CLAUDE.md says confirmed; the research doc says PLACEHOLDER. Not used in the ad. It goes to the page and the first reply once you reconfirm it. |

## Part B. Script breakdown (H1), with why each line stays

| # | Beat | Spoken line | Job | Source | Why it stays in v3 |
|---|---|---|---|---|---|
| 1 | **Open A** | "The tenant left. Now YOU can too." | Qualify ("tenant"), promise the exit, open "how?" | §4b root, §5 bullseye, Hook Map lever 3 | 21/28. Written from the root (§4b). H3 scored 22 but comes from the surface want. |
| 2 | Payload | "House is sitting empty. Same mortgage, every month." | The bleed as a picture, monthly, no number | §4 scene 3, Hook Map lever 2 | The copy chief kept it: "same" against "empty" is the contrast. The number stays out. |
| 3 | **Open B** | "So what's the move?" | Voice his decision | §3 (solution-aware: he's choosing) | It sets up template #5's "vs." beat |
| 4 | Payload | "Patch THAT and bet on the NEXT tenant?" | Alternative 1 and its cost | Worksheet: "another thing on my plate" | #5 "[alternative] [flaw]". Dimensionalized (THAT = the hole on screen). |
| 5 | Payload | "Fix it, list it, pay commission?" | Alternative 2 and its cost | Worksheet: "No money, time or energy to manage contractors"; commission | #5. The copy chief tested "Contractors, showings, commission?" and kept the verbs (Appendix §5). |
| 6 | **Close B** | "Or sell it AS-IS." | The third road: the as-is exit | Step 2 §1 mechanism | It says the mechanism's plain name |
| 7 | Payload | "Our offer's LOWER than a fixed-up sale." | The catch, said first | Step 2 §3. **User to confirm** (explicit yes requested before take 3). | It meets §3 radical transparency and pre-empts r17's objection (§7) |
| 8 | Payload | "No commission, no fees." (v4: "But you pay" cut to fit 8 s; proposed; user reply 'yeah', explicit confirmation requested before take 3) | Offset: the costs from line 5 | Confirmed terms | §7: terms stop at two, so it doesn't sound like a TV feature list |
| 9 | **Close A** | "They left. That's how YOU leave." (v4: "too" cut; proposed; user reply 'yeah', explicit confirmation requested before take 3) | Pay off the hook through the mechanism | Loop rule | Consistency ("That's how" ties the payoff to the mechanism) |
| 10 | CTA | "Tap below." End card: Ask for my offer / No obligation | The smallest step; says what the tap does | Step 2 §4 (direct ask); copy-banks | A direct ask for the closest-to-ready persona. The two-step is test 3. |

**Loop sequence:** OPEN A (1) → payload (2) → OPEN B (3) → payload (4, 5) → CLOSE B (6) → payload (7, 8) → CLOSE A (9) → CTA (10). Nested, closing in reverse. No open-close back to back. A closes last with the hook's promise.

### Labelled script (H1)

```text
CLIP 1 (8 s, L1 open front door, 19 words)
[OPEN A]   The tenant left. Now YOU can too.
           SHOW → AI UGC, L1: just inside the open front door, thumb over his shoulder at the messy front room. Text: Tenant left, you can too
[payload]  House is sitting empty. Same mortgage, every month.
           SHOW → b-roll house_32116905 (from 3 s in), cut on "House", held through both sentences. Text: House sitting empty → Same mortgage every month
[OPEN B]   So what's the move?
           SHOW → AI UGC, L1 punch-in 131%, small shrug, eyebrows up. Text: What's the move?

CLIP 2 (8 s, L2 living room with the hole in the drywall, 18 words)
[payload]  Patch THAT and bet on the NEXT tenant?
           SHOW → AI UGC, L2 (new setup): half-turned, free hand points at the hole on "THAT". Text: Patch it? → Next tenant?
[payload]  Fix it, list it, pay commission?
           SHOW → cut on "Fix" to b-roll forsale_7578271, held through the question. Under it, his hand drops on "Fix it". Text: Fix it? List it? Commission?
[CLOSE B]  Or sell it AS-IS.
           SHOW → AI UGC, L2, hand already down, still, eyes on the lens. Text: Or sell it as-is

CLIP 3 (8 s, L3 bedroom with the ceiling leak, 19 words; v4 cut, proposed; user reply 'yeah', explicit confirmation requested before take 3)
[payload]  Our offer's LOWER than a fixed-up sale.
           SHOW → AI UGC, L3 (new setup), low angle, still. NO cutaway (trust line). Text: Lower than a fixed-up sale
[payload]  No commission, no fees.
           SHOW → same L3 close-up. Text: No commission, no fees
[CLOSE A]  They left. That's how YOU leave.
           SHOW → same L3 take, the operator steps back 2 paces to medium-wide; one small nod on "YOU leave". Text: Your turn to leave
[CTA]      Tap below.
           SHOW → cut on "Tap" to the end card: small logo, arrow down. Text: Ask for my offer / No obligation
```

Plain lines for the Seedance takes (v4; the dialogue line in each `Ad17_seedance_prompt_take*.txt` matches, checked by script):

```text
Take 1: The tenant left. Now YOU can too. House is sitting empty. Same mortgage, every month. So what's the move?
Take 2: Patch THAT and bet on the NEXT tenant? Fix it, list it, pay commission? Or sell it AS-IS.
Take 3: Our offer's LOWER than a fixed-up sale. No commission, no fees. They left. That's how YOU leave. Tap below.
```

### Word count and length (counted by script)

| Take | Duration | Words | Stress | Speech at 0.351-0.380 s/word (Ad 16 Omni pace; Seedance's pace not measured yet) | Limit |
|---|---|---|---|---|---|
| 1 | 8 s | 19 | YOU | 6.67-7.22 s | ≤ 20 |
| 2 | 8 s | 18 | THAT, NEXT, AS-IS | 6.32-6.84 s | ≤ 20 |
| 3 | 8 s | 19 | LOWER, YOU | 6.67-7.22 s | ≤ 20 |
| **Total** | | **56** | | 19.66-21.28 s | |

- At the 197.1 wpm reference median, 56 words take 17.05 s.
- The edit estimate is about 21.9 s: 20.44 s of speech at 0.365 s/word, plus a 1.5 s end-card hold.
- You vs. we: 2 "you" words, 1 "we" word ("our") = 67 / 33. The v4 cut removed "you pay".
- Seedance's own pace is not measured. Run take 1 alone first, then word-diff it and time it before takes 2 and 3.

---

## Part C. Scene breakdown (v4: filmed by a camera operator, not a selfie)

**What changed (user, 2026-09-27):** "It doesn't need to be a selfie video. There will be another cameraman doing the video ... so that you can show it perfectly with great angles and great frames." JMSN now talks into a camera that a second person holds. That makes wide, over-the-shoulder, low-angle and reveal shots possible. The spoken script is unchanged.

**Reference for this style** (watched 2026-09-27 as 1 fps contact sheets):
- `bright_future_16s` (16.917 s): a buyer filmed by someone else at a junk-filled back porch, full body, hard midday sun, with word-by-word captions and a logo end card.
- `zion_fast_15s` (14.633 s): a buyer filmed by someone else in front of a rundown house, full body, overcast light.
- What we take from them: someone else holds the camera, the rooms are real and messy, the light is hard and natural, and he talks straight into the lens.
- What we do better than them: they use one static wide angle, and we change the angle every take.

**Camera language (every take prompt):** a handheld phone camera held by a second person standing a few steps away, with slight natural shake. **Light: low late-afternoon sun with hard shadows** (decided 2026-09-27): hard shadows outdoors, a hard patch of sun through the door or window indoors, darker corners. Auto exposure. No lamps, no gimbal float, no drone, no dolly track, no colour grade. Never write "cinematic" or "photorealistic": those words gave the plastic look on 2026-09-22 (memory `veo-realism-prompt-rules`). JMSN looks into the lens as if talking to the owner who's watching.

### Locations and opening angles

**Reference, not a first frame:** each Seedance take gets 2 cropped reference images of JMSN and no first frame:
- `13_Generated/images/Ad17_JMSN_ref_face_crop.png` (428 × 886);
- `13_Generated/images/Ad17_JMSN_ref_body_crop.png` (430 × 946).

The rooms and angles come from the take prompts.

| Loc | Where | Damage in frame | Opening angle | Why this angle |
|---|---|---|---|---|
| L1 | Front porch and open front door of a small single-storey rental | Two black trash bags on the porch, a broken chair, torn screen door, stained carpet visible through the doorway | **Wide, low angle** from the front path, about 4 m away, camera at knee height. Full body. He stands in the open doorway **for the whole take**, one hand pointing back into the house. | A full-body wide from below makes him the buyer in charge of the scene, and the trashed house fills the frame. That's the hook's picture in one image. |
| L2 | Living room | A fist-size hole in the drywall at head height, scuffs, bent blinds, bare subfloor, one trash bag | **Over-the-shoulder** from behind his right shoulder, medium. He points at the hole, which sits sharp in the frame's left third. | The viewer sees the hole through his eyes on "Patch THAT". |
| L3 | Back bedroom, empty | A brown water-stain ring and a sagging patch on the ceiling, peeling paint high on the wall, window light from the side | **Close-up, eye level**, steady, his face in the right third, the stain visible above and behind his head | The trust line gets a close, calm face. Then the take pulls back to show the whole room. |

### Shot table (H1). Times are estimates at 0.365 s/word; retime to the real clips.

| Scene | Time (s) | Spoken over it | Shot / framing / camera move | On screen | B-roll (cut at sentence start) | On-screen text | Sound | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.000-2.555 | The tenant left. Now YOU can too. | **WIDE, low angle**, static. He stands in the open doorway (he doesn't step onto the porch). His thumb points back into the house on "left", then at the lens on "YOU". | Trashed porch and house, full body | none (three-layer hook: the house, the line, the text) | Tenant left, you can too | Screen door creak, wind, music in low | Clip 1 / L1 |
| 2 | 2.555-5.475 | House is sitting empty. Same mortgage, every month. | Insert | | `house_32116905` from 3 s in (a car passes at 1.0-2.5 s). **Under this b-roll the operator walks in closer**, hidden. | House sitting empty → Same mortgage every month | Room tone | Stock, no people |
| 3 | 5.475-6.935 | So what's the move? | **MEDIUM**, eye level (the same take, now closer). A small shrug. | Waist-up in the doorway | none | What's the move? | Music dips | Clip 1 / L1 |
| 4 | 6.935-9.855 | Patch THAT and bet on the NEXT tenant? | **OVER-THE-SHOULDER**, medium. He points at the hole on "THAT", then turns his head to the lens on "NEXT". | The hole sharp in the left third | none (the hole is the picture) | Patch it? → Next tenant? | Knuckle knock on drywall on "THAT" | Clip 2 / L2 |
| 5 | 9.855-12.045 | Fix it, list it, pay commission? | Insert | | `forsale_7578271` on "Fix" (upscale 1.5×). **Under it, on "Fix it", he turns to face the lens and the operator takes one step back** (no orbit). | Fix it? List it? Commission? | Wind | Stock, no people |
| 6 | 12.045-13.505 | Or sell it AS-IS. | **MEDIUM, front**, eye level, hand down, facing the lens | The hole visible behind him | none (loop close) | Or sell it as-is | Music lifts slightly | Clip 2 / L2 |
| 7a | 13.505-17.520 | Our offer's LOWER than a fixed-up sale. No commission, no fees. | **CLOSE-UP**, eye level, camera still | Calm face, stain above | **none: trust line** | Lower than a fixed-up sale → No commission, no fees | Music out, faint drip | Clip 3 / L3 |
| 7b | 17.520-19.710 | They left. That's how YOU leave. | **Slow pull-back** from close-up to MEDIUM-WIDE: the operator steps back 2 paces and the whole trashed room comes into frame. One nod on "YOU leave". | Full room reveal | none | Your turn to leave | Music back in | Clip 3 / L3 (same take) |
| 8 | 19.710-21.940 | Tap below. | End card | Small logo, arrow down | none | Ask for my offer / No obligation | Music out | Editor |

- **Cuts:** 7 in about 21.9 s = 3.19 per 10 s (estimate), each at a sentence start (user rule `ugc-edit-merge-then-scenes`: about 3 per 10 s). The angle also changes inside takes 1, 2 and 3 (wide to medium, over-the-shoulder to front, close-up to wide), so no angle holds longer than the 4.0 s close-up (7a).
- **Angles used:** wide low, medium, over-the-shoulder, 3/4 front, close-up and a pull-back reveal. That's 6 framings across 3 takes, against 1 static wide in each of bright_future and zion_fast.
- **Risk:** a camera move inside one AI take (the step-in, the turn with a step back, the pull-back) may not happen. On Ad 16, Omni gave "little actual walking". Hiding the step-in and the turn under b-roll means a take that misses its move still cuts cleanly. Only the 7b pull-back is on screen. If it fails, cut 7b as a hard cut to a second, wider generation of L3: a 4-6 s Seedance take at 41 credits/s = 164-246 credits (list price).
- **Sound-off test:** Tenant left, you can too → House sitting empty → Same mortgage every month → What's the move? → Patch it? → Next tenant? → Fix it? List it? Commission? → Or sell it as-is → Lower than a fixed-up sale → No commission, no fees → Your turn to leave → Ask for my offer / No obligation.

### Stock (checked 2026-09-27)
- Used: `house_32116905`, `forsale_7578271`.
- Spare: `contract_7841865` (blur the text), `leak_4159571`, `leak_6108991`, `ceiling_4882745`.
- Never use (people or hands in frame): `hole_4903222`, `leak_6813965`, all four `keys_*`, `garage_*`, `table_*`, `yard_13126902`.

### Clip plan (3 takes, Seedance 2.0, decided 2026-09-27)

| Take | Scenes | Words | Prompt file | Length | Camera inside the take | Credits (list) |
|---|---|---|---|---|---|---|
| 1 | 1-3 | 19 | `10_Video_Builds/Ad17_JMSN_Landlord/Ad17_seedance_prompt_take1_porch.txt` | 8 s | Static wide, low, with him in the doorway throughout. Then the operator moves in to medium (hidden by b-roll). | 328 |
| 2 | 4-6 | 18 | `..._take2_wall_hole.txt` | 8 s | Over-the-shoulder. On "Fix it" he turns to the lens and the operator takes one step back; no orbit (hidden by b-roll). | 328 |
| 3 | 7-8 | 19 | `..._take3_bedroom.txt` | 8 s | A still close-up, then a slow pull-back to medium-wide on "They left" | 328 |
| | | **56** | | **24 s** | | **984** |

- **Settings:** model `bytedance/seedance-2`, 720p, 9:16, 8 s, `generate_audio` on.
- **Inputs:** the 2 reference images above. No first frame.
- **Cost:** 328 credits a take is 41 credits/s × 8 s at list price (the Kie pricing page, as read in the session file). An audio surcharge is not confirmed. **Total 984 credits = $4.92. Nothing has been run.**
- **Take 3 runs only after the user's explicit yes** on both the 19-word cut and the offer line.
- **Each extra hook variant** re-makes takes 1 and 3: 656 credits = $3.28.
- **Superseded, not used:** the Omni prompts `Ad17_video_prompt_clip1/2/3_*.txt` and the v3 selfie images `Ad17_JMSN_L1_front_door_v1.png` and `Ad17_JMSN_L2_wall_hole_v1.png`, which cost 36 credits.
- **Prompt files:** ugc-video-director owns them. The dialogue in all 3 matches this script (checked by script). The decisions above (doorway only, no orbit, low late-afternoon sun, 2 reference crops) are the plan of record for their next revision.

---

## Part D. Checks

| Check | Result |
|---|---|
| Kill checks (H1) | 6 pass, 1 borderline. Copyable: it names one moment, but nothing in it is specific to Property Abundance. Same bar as all 20 hooks. |
| 7-point score | H3 22 · H1 21 · H2 21 · H4 21. All keep. My judgment. |
| Loop order | Nested A/B, closing in reverse, no back-to-back open-close ✓ |
| Beat-by-beat | Appendix §9: 9 claims in order, no contradiction |
| Claims | As-is ✓ · lower than a fixed-up sale ⚠ (**used in Ad 16 final + Ad 15 v2 approved script; not on the CLAUDE.md confirmed list; user to confirm**) · no commission ✓ · no fees ✓ · no obligation ✓ (end card) |
| Step 5 body | First line 7 words ✓. Opens on his situation ✓. Dimensionalized ✓. Alternatives named ✓. Top worry (lowball) raised ✓. Honest admission ✓ (claim to confirm). You vs. we 75/25. Proof ✗ (none exists; this is #5's empty [Proof] slot). |
| Step 6 CTA | Partial. One action, "Tap below" + "Ask for my offer / No obligation": first person, says what the tap does, free. The button should be Learn More, or Get Quote if the page is a quote form (Meta's button list was not checked live). **Gaps:** no proof before the CTA, and the page is dead (Step 1 §6). |
| Step 8 compliance | It names the situation, never a trait. No AI label is needed (company voice). No words in AI prompts. No hints about who the tenant was. **Meta's Housing Special Ad Category must be set when the campaign is created, and it limits targeting** (project rule: `Property_Abundance_UGC_Set_ReelDirection_v1.md`, "Before any of this runs", item 5; swipe-file #8). Meta's policy page was not loaded this session. |
| Temperature | Blunt and calm, with no sympathy. The page and the first reply (Step 2 §5, text 1) must match. |
| Departures | 1. **The brand name is never spoken** (your Ad 16 call on 2026-09-27, "no company name in clip 3"). This also misses Short-form rule 11's "who it's from in about 2 s"; the logo-bug option is for you to decide. 2. Close A echoes the hook (the template's consistency), where reel_direction_2 wants a different type. 3. No ILLUSTRATE line in 60 words. |
| Language gate | 0 em dashes, 0 banned phrases (grep run) |

### Blockers (spend, not generation)
- **The landing page is dead** (measured: 403 over http, and a Cloudflare Origin certificate error over https).
- **The second click shows only the UK company.**
- **The claim "Our offer's lower than a fixed-up sale" needs your confirmation.**

---

# STEP 5. TEST PLAN (`testing-and-iteration.md` §3, §4, §10)

1. **Hook first** (§3.1). The body stays identical, and each variant swaps the first 2-3 s plus its matching Close A (the only change to the body).
   - Run **H1 against H2 first** (benefit against pain; Sabri says benefit wins about 8 in 10, his claim).
   - Then add H3 and H4. Sabri: 3-5 at a time.
2. **Then the angle:** finality (H1/H4) against "get the number" (H3), if H3 wins round 1.
3. **Then the offer framing and CTA:** a direct "Ask for my offer" against the two-step no-contact guide (Step 2 §4). This runs only when the guide and the page exist.
4. **Then the format:** this AI UGC walkthrough against a static in the swipe-file #8 style.
- **Budget tight?** Test organically first on an unbranded account (Sabri, §3). Paid runs need the Housing Special Ad Category.

**Read the results (§4):**
- Hook rate first: 3-second views ÷ impressions. Sabri calls 20-30 % good (his benchmark).
- Use 7-day rolling data. Keep at least 3 tests running.
- Check frequency (under about 3 is usually not fatigue) before calling an ad tired.
- Judge on cost per qualified lead and closed deals, not cost per click.
- When results drop, run the three-point triage (§8): click rate, then page conversion, then the close step.

**Log what wins (§10), only after results exist, into `swipe-file.md` "Proven winners":** the hook, the numbers (hook rate, cost per qualified lead, deals), the audience (Persona 3, trashed-rental moment), the awareness level (Solution-aware, Stage 4), and one line on why it won. **Nothing is written to `swipe-file.md` now.**

---

# APPENDIX. AI passes (`prompts/copy-prompts.md`), run by me, output shown

*These passes ran on the v3 script (60 words). The v4 Seedance sync later cut "But you pay" and "too" from take 3 (proposed; user reply 'yeah', explicit confirmation requested before take 3). The claims are unchanged.*

## §2 Brief check
**Summary back (5 bullets):**
1. Landlord, tenant gone, rental trashed and empty, mortgage still due. Solution-aware at Stage 4.
2. Bullseye: get out. Root: finality with dignity.
3. Mechanism: the fix-first trap → the as-is exit.
4. Offer: as-is, no commission, no fees or closing costs, he picks the date, no obligation. Admission: lower than a fixed-up sale (to confirm).
5. Banned: numbers, speed, scarcity, the offer math, tenant-occupied, eviction or legal, personal attributes.

**Missing or vague:**
- **Proof we can show: none.**
- Where Property Abundance buys: TBD, so there is no city for the page or the AI check.
- Its price-drop policy: TBD in the research doc.
- The landing page is dead.
- The "lower" claim is unconfirmed.
- The "we buy it ourselves" status conflicts between files.

## §1b Objection Obliterator
The material is the research doc's objection table, the raw file and the Buyer_Avatar objections. There are no sales calls or reviews (none exist).
- **Mentions** are sentences in the raw file that match the topic. They include Reddit Answers summaries and repeats, so they signal how common a topic is, not how many people raised it.
- **Quote 2** often comes from the raw file (`RAW:` below).

| Objection | Quote 1 | Quote 2 | Mentions | In the ad? | One plain, true line for each ignored one |
|---|---|---|---|---|---|
| Wholesaler | "Many 'cash buyers' now are just wholesalers who tie you up in contract..." | "Any contract that says "And assigns " Is a flipper A flipper who doesn't even have any money." | 564 | **Ignored** (cut in v2, no set-up) | "We buy it ourselves. We don't sell your contract to someone else." For the page and first reply, **after you reconfirm it** |
| Lowball | "...offered me pennies." | "they offered me $78k when I had multiple realtors tell me it's worth somewhere around $190k" (internal) | 253 | Answered: the admission | n/a |
| Scam | "Are those 'we buy ugly homes' and random mail offers legitimate?" | "They're not a scam by they're definitely paying below market value, that's how they make a profit." | 168 | Partly: "No obligation" on the end card | "No obligation. You can say no." (confirmed), on the page |
| Price drop late in the deal | "2 months later they offered 10% less than originally quoted..." | RAW: "Buyer offered "as is," wants to lower their offer after inspection." | 118 | **Ignored** | **No true line possible yet.** The policy is TBD. You'd need your real renegotiation policy before any line. |
| Predatory | "They focus on the three Ds: death, divorce, destitution." | RAW (Reddit Answers summary): "...can be predatory towards sellers in vulnerable situations." | 118 | Handled by tone (situation, not person; calm) | n/a |
| Proof of funds | "Proof of funds letters are often drawn on some vague LLC that they don't even own." | RAW: "Ask for proof of funds!" | 72 | **Can't answer** | None until real proof of funds exists. A page item. |
| Hidden fees | "...then they wanted 5% service fee and 2% closing fees." (internal; names a competitor) | RAW: "Just don’t know if theirs a hidden fees or anything I’m not aware of..." | 10 | Answered: "no commission, no fees" | n/a |
| A realtor gets more | "My 'as is' house sold in 3 days for asking price using a realtor friend of mine." | RAW: "99 times out of 100 an agent will get you more than the "We Buy Houses" companies." | 2 | Answered: the admission concedes it | n/a |

## §5 Copy chief (dimensionalization), original → rewrite → why

| Line | Tested rewrite | Decision |
|---|---|---|
| "House is sitting empty." | "Empty rooms, nobody paying." | **Kept.** The rewrite adds rent talk (missed rent), which is closer to a money attribute. The original is concrete, and the b-roll shows the house. |
| "Same mortgage, every month." | "Mortgage still comes out every month." | **Kept.** "Same" makes the contrast with "empty", in fewer words. |
| "Patch THAT and bet on the NEXT tenant?" | none | **Kept.** Already dimensionalized: THAT is the hole on screen. |
| "Fix it, list it, pay commission?" | "Contractors, showings, commission?" (4 words) | **Kept the original.** The nouns are more concrete but read like a caption. The verbs carry the fix-first mechanism ("Patch... Fix..."), and the FOR SALE b-roll supplies the scene. The rewrite would also change clip 2's Omni dialogue and action cue with no scored gain. |
| "Or sell it AS-IS." | none | Kept (the plain name) |
| "Our offer's LOWER than a fixed-up sale." | none | **Locked wording** (claim) |
| "But you pay no commission, no fees." | none | Kept (the terms, concrete) |
| "They left. That's how YOU leave too." | none | Kept (the payoff) |

- **Flow:** each line earns the next: the promise, the pain, the question, road 1, road 2, the answer, the catch, the offset, the payoff.
- **Temperature:** blunt and calm from the hook to the CTA, with no spike or drop.

## §4 Register variants (one line each; claims identical)
- **(a) News exposé:** "The tenant's gone, the damage stayed, and the mortgage still comes out. There's a way out that skips the repairs."
- **(b) Calm, empathetic expert:** "When a tenant leaves a place like this, you have a few roads: patch and re-rent, fix and list, or sell it as-is."
- **(c) Mid-scene story:** "Keys on the counter, a hole in the wall, the mortgage due again. Now what?"
- **(d) Blunt friend who's seen it all:** "The tenant left. Now you can too." **This is the one the ad uses.** Register (b) is the next register test if (d) fatigues.

## §7 Kill-check review (the kept hooks plus the body)

| Hook | Announce | Blind curiosity | Solvable without click | Accuse | Copyable | Body doesn't pay off | Closes in ad | Rank |
|---|---|---|---|---|---|---|---|---|
| H3 "Before the contractor, get the AS-IS number." | no | no | no | no | borderline | no | no | 1 |
| H1 "The tenant left. Now YOU can too." | no | no | no | no | borderline | no | no | 2 |
| H2 "What the tenant broke? Not YOURS to fix." | no | no | no | no | borderline | no | no | 3 |
| H4 "Walking away from THIS isn't giving up." | no | no | no | no | borderline | no | no | 4 |

Top 2 fixes for the losers:
- **#18 "Done playing landlord?"**
  1. Drop "playing" ("Done being a landlord?"), so it doesn't poke the humiliation wound.
  2. Cut a body word, so clip 1 fits 20.
- **#17 "Re-rent it or sell it?"**
  1. Use it only with a body that drops Open B.
  2. Or move it to the primary text.
- **#9 "Keys on the counter. And THIS."**
  1. Add a benefit ("...and you don't have to fix it").
  2. Or save it as a visual-only cold open.

## §9a Pre-mortem and skeptic
**Assume it failed after 90 days. The 5 most likely reasons, most likely first:**
1. **The click went nowhere:** a dead page (403 and a certificate error), and a name search that finds a UK training company.
2. **No proof:** "our offer's lower" without a real past deal reads as "they lowball". Stage 4 viewers had just seen buyers with proof.
3. **Looks like every "we buy houses" ad:** the hooks are borderline copyable, and the hook rate stays low.
4. **Targeting stripped** (Housing category): the ad reached homeowners without rentals, and only the word "tenant" qualified viewers.
5. **Slow or salesy first reply:** competitors reached the lead first (Jeremy Haynes).

**The skeptic, objection by objection:**
- "Lower by how much?" There is no number, by design, and the page must explain how the offer is built, if that is ever confirmed.
- "Are you a wholesaler?" Not answered in the ad. The page needs it.
- "Will you drop the price after the walkthrough?" No policy exists yet.
- "Who even are you?" No brand until the end card, and the search finds someone else.
- "Is that guy real?" An AI avatar. That is legal as company voice, but it must look native.

**Grade (my judgment, as a direct-response chief): 6/10.**
The 10/10 version has:
- the same script;
- one real past purchase shown with the seller's consent (a real proof slot for template #5);
- a working page that explains the as-is exit;
- a plain anti-wholesaler line and a written price-drop policy on that page;
- a first reply that teaches within the hour;
- a brand name that searches to this company.

## §9 Beat-by-beat (the claims in order)
1. The tenant left; you can leave too (promise, no timeline).
2. The house is empty; the mortgage is the same every month (situation).
3. What's the move? (question)
4. Patching and re-renting means betting on another tenant (opinion about an alternative).
5. Fixing and listing means paying commission (a general fact about listing).
6. You can sell it as-is (confirmed).
7. Our offer is lower than a fixed-up sale (**to confirm**).
8. You pay no commission and no fees (confirmed).
9. That's how you leave (the payoff).

No line contradicts, repeats or wanders from the one before. The only claim not on the confirmed list is #7, which is flagged.
