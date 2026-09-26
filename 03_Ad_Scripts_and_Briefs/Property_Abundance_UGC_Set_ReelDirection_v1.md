# Property Abundance - UGC ad set, directed with Reel_direction

**Made:** 2026-09-24
**Skill:** `Reel_direction` (`~/.claude/skills/Reel_direction/`), adapted for a paid offer. See "How the skill was adapted" below.
**Inputs:**
- `04_Audience_Research/Research_Document_Cash_Home_Buying.md` (personas, objections, ICP language)
- `03_Ad_Scripts_and_Briefs/Cash_Home_Buying_Winning_Concepts.md` (which competitor concepts got traction)
- `03_Ad_Scripts_and_Briefs/Cash_Home_Buying_8_Ads_Reference.md` (shot by shot on 6 competitor ads)
- Fresh web pass, 2026-09-24. Sources listed in "Market pass" below.

**Scope:** 5 UGC ads. One persona each. Scripts, hooks, on screen text, shot lists, captions, CTA, compliance notes. No production files.

`[ ]` = your real fact. An ad does not run with a bracket still in it.

---

## How the skill was adapted

Reel_direction was written for @billy.coder, an organic coding account whose product is a comment that triggers a DM. This is a paid housing offer. Four beats carry over, one does not.

| Reel_direction beat | What it becomes here |
|---|---|
| 1. A named paid thing loses, price said out loud in 5 seconds | A named cost the seller is paying **right now** loses. The agent commission, the repair quote, the monthly payment on a house they do not want. |
| 2. Proof on a real screen | The offer worksheet on screen. Value, minus repairs, minus our costs, equals the offer. Winning Concepts Finding 4: none of the 6 competitor ads does this. It is the open gap. |
| 3. The presenter, cut out, composited over the footage | Same. UGC talking head over the house, the paperwork, the worksheet. No floating box. |
| 4. One uppercase word, comment it and I send something | **Split.** Paid version ends on the form. Organic version keeps the comment keyword. Both written below. |

Rules kept as written: sound and motion at frame 0, one declarative banner held from frame 0, no dead frames, no em dashes, never invent a number, change the palette between ads, avoid orange and purple on dark, check the delivered file and not the build log.

Rules dropped as not applicable: never show the repo name, the licence line, the burned keyword list at `~/Documents/Notes/reel-system/keywords_burned.txt` (that list belongs to @billy.coder, not to this brand; start a separate one).

---

## Market pass, 2026-09-24

New since the 2026-09-22 research. Two findings change the creative.

**1. Meta's Housing Special Ad Category strips the targeting.** Age, gender and ZIP targeting are removed and detailed targeting is restricted for housing ads, so the creative has to qualify the lead instead of the audience settings. Source: adadvisor.ai, "Facebook Ads for Real Estate Investors: Motivated Sellers (2026)". This was open item 4 in Winning Concepts and it is now answered: **one situation per ad is not a style choice, it is the only targeting left.**

**2. Situation hooks beat offer hooks.** The same source lists live situation openers: "Inherited a property you don't want?", "Behind on payments or facing foreclosure?", "Own a vacant or damaged house?". A generic "we buy houses" competes on price with every other buyer in the feed.

Second source, leadsync.me "Real Estate Facebook Ad Examples (2026)", reports a cluster pattern of "sell house fast", "cash home buyers", "avoid foreclosure help" and quotes a 27% conversion lift for "Sell fast, no repairs needed" over a generic call to action. **Treat that number as the vendor's claim, not a verified fact.** It is not in an ad below and must never go on screen.

---

## What the research says to say, and what to drop

Straight out of `Research_Document_Cash_Home_Buying.md`.

**They want (lead with these):**
- Be done with it. Peace of mind over the last dollar. "I just wanted it SOLD."
- No clean out, no repairs. The hoarder house, the parent's belongings.
- A close that cannot fall apart. No financing, no appraisal, no late price cut.
- They pick the move date.
- A price with the math shown, not a number from nowhere.
- Stop the money leak.

**They ignore or distrust (cut these):**
- "Top dollar", "best price guaranteed", "we pay more than anyone". The research says readers call these lies outright.
- Fake urgency. "We cap how many homes we buy each month", "before it is too late". Reads as a scam signal.
- The feature list every competitor runs: no repairs, no fees, no showings, no inspections. All 6 reference ads say it, so it carries no information. Say **one** of them, once, and spend the rest of the ad on proof.
- Cash fanning, money counting, suitcases of cash. Looks like the ads they are afraid of.
- Claims about competitors you cannot prove. Ref 3 and 5's "below half the value, guaranteed" is the weak spot in the highest viewed ad in the set.
- An actor speaking as a real past customer. Ref 6 does it, got 77 views a day, and it is an FTC risk under 16 CFR 465.2 and 255.1.

**The objection to answer out loud, by name:** "you will lowball me" and "this is a scam". They are the top two in the research. Naming the doubt before the viewer does is the entire trust move.

---

## Gate scores

Each concept was scored through the skill's own gate, `topic_gate.py`, run 2026-09-24. Pass mark 55.

| Ad | Persona | Score |
|---|---|---|
| 1 | Heir Far Away (Inherited Irene) | 92 |
| 2 | Behind on Payments (Foreclosure Frank) | 87 |
| 3 | Burned Out Landlord (Tired Landlord Larry) | 88 |
| 4 | The House Needs Everything (Fixer Upper Fran) | 58 |
| 5 | The Skeptic, offer math | 92 |

**What the score is and is not.** The gate scores the yes/no answers I gave it, and those answers are my judgment about each concept, not a measurement of any ad. The weights were calibrated on 12 posts from a coding account, so the scale transfers as a ranking and not as a prediction. Read it as: ad 4 is the weakest of the five and should get the smallest budget, ads 1 and 5 the largest.

---

## Shared spec

| | |
|---|---|
| Frame | 1080 x 1920, 30 fps, full bleed |
| Length | 25 to 35 seconds. 65 to 95 spoken words at about 170 wpm. |
| Audio | 48 kHz stereo, -14 LUFS integrated, true peak under -1 dBTP |
| Frame 0 | Sound and motion. The measured killer on the reference account was silence at 0.1s. |
| Banner | One declarative line, top third, held from frame 0, never changing |
| Captions | 1 to 4 words a card, one keyword in colour, inside the safe zone |
| Cuts | A new shot about every 2 seconds |
| Presenter | One person, chest up, straight to camera, matted over the footage. Same person across all shots in an ad. |
| Last shot | The real form on a phone, plus the brand name |
| Palette | Different per ad, named below. No orange. No purple on dark. |

---

## Ad 1 - Heir Far Away

**Persona:** Inherited Irene. **Gate 92.** **Palette:** slate blue and warm cream.
**Objection answered:** am I getting ripped off because I am in a rush.
**Named cost that loses:** the tax bill, the insurance bill and the drive, every month, on a house she never asked for.

**Hook, three options. Pick one on camera, shoot all three.**

| Pattern | Line |
|---|---|
| 18, Do this instead | "If you are driving hours to check on a house you inherited, do this instead." |
| 17, Myth bust | "The myth about an inherited house is that holding it costs you nothing." |
| 6, You're doing it wrong | "You are paying for a house you never asked for, and nobody told you there was another way." |

**Banner (held from frame 0):** THE HOUSE YOU INHERITED IS STILL BILLING YOU

**Script, six lines, 78 words.**
1. If you are driving hours to check on a house you inherited, do this instead.
2. Every month it takes a tax bill, an insurance bill, and a tank of gas.
3. Nobody is living there. It is still charging you rent.
4. We buy it as is. You take what you want out, and you leave the rest.
5. Here is how we get to the number. [Show the worksheet.]
6. [CTA line, see CTA block.]

**On screen at line 5 (the worksheet):**
```
Worth, fixed up        $[A]
Repairs we pay for     $[B]
Our costs and profit   $[C]
Your offer             $[A minus B minus C]
```

**Shot list**
| t | Shot | Audio |
|---|---|---|
| 0.0 | Car on a highway at speed, windscreen view, road noise up | line 1 |
| 2.5 | Mailbox stuffed with envelopes, one pulled out | line 2 |
| 5.0 | Empty front room, dust in the light, a chair still there | line 3 |
| 9.0 | Presenter matted over the empty room, cut hard left to right | line 4 |
| 14.0 | Worksheet fills the frame, numbers land one line at a time | line 5 |
| 22.0 | Boxes going into a car boot, front door closes | line 6 |
| 28.0 | The form on a phone, brand name | tail |

**Caption:** You inherited it. You did not sign up to keep paying for it. Tell us about the house and we will show you the number and how we got it. [City or state]. [CTA].

---

## Ad 2 - Behind on Payments

**Persona:** Foreclosure Frank. **Gate 87.** **Palette:** deep green and bone.
**Objection answered:** you are a vulture preying on me.
**Named cost that loses:** another month of payments he cannot make while the equity burns off.

> **Tone rule, from the research.** Calm, not predatory. No countdown, no "before it is too late", no red flashing. The research names urgency hype as the reason this audience assumes a scam. **This ad names the housing counselor out loud.** No reference ad does. That single line is the trust asset.

**Hook, three options.**

| Pattern | Line |
|---|---|
| 2, Newcomer warning | "If you are two payments behind, you need to hear this before you do anything." |
| 10, Diagnosis plus fix | "Why the letters from your lender keep coming, and what still works after they do." |
| 17, Myth bust | "The myth is that once you are behind, selling is off the table." |

**Banner:** BEHIND ON PAYMENTS IS NOT THE END OF YOUR OPTIONS

**Script, six lines, 81 words.**
1. If you are two payments behind, you need to hear this before you do anything.
2. Call a HUD approved housing counselor first. It costs you nothing and they work for you, not for us.
3. If the answer is to sell, there is equity in the house while it is still yours.
4. We buy it as is, and we close on the date you pick.
5. Here is how we get to the number. [Show the worksheet.]
6. [CTA line.]

**On screen at line 2:** HUD APPROVED HOUSING COUNSELOR. Put the real phone number or URL on screen. Verify it the day you shoot.

**Shot list**
| t | Shot | Audio |
|---|---|---|
| 0.0 | A stack of lender envelopes dropped on a table, sound of the drop | line 1 |
| 2.5 | A hand dialling a phone, calm, no rush | line 2 |
| 7.0 | Counselor line burned on screen over a quiet kitchen | line 2 tail |
| 10.0 | Presenter matted over the kitchen, full frame | line 3 |
| 14.0 | Calendar, a finger picks a date | line 4 |
| 18.0 | Worksheet fills the frame | line 5 |
| 26.0 | Form on a phone, brand name | line 6 |

**Caption:** Talk to a HUD approved counselor first. If selling turns out to be your best move, we will show you the offer and the math behind it. No pressure and no obligation. [CTA].

---

## Ad 3 - Burned Out Landlord

**Persona:** Tired Landlord Larry. **Gate 88.** **Palette:** charcoal and pale gold.
**Objection answered:** nobody buys with a problem tenant inside.
**Named cost that loses:** the attorney invoice plus a mortgage with no rent coming in.

> **Only run this ad if you actually buy occupied houses.** The whole ad is that one promise. It is TBD in the research doc. If you do not buy with tenants in place, kill this ad instead of softening it.

**Hook, three options.**

| Pattern | Line |
|---|---|
| 19, Harder than promised | "Nobody told you an eviction was going to take this long." |
| 18, Do this instead | "If you are paying an attorney by the hour to get your house back, do this instead." |
| 6, You're doing it wrong | "You are covering a mortgage on a house somebody else is living in." |

**Banner:** YOU ARE PAYING FOR A HOUSE SOMEBODY ELSE LIVES IN

**Script, six lines, 76 words.**
1. Nobody told you an eviction was going to take this long.
2. The rent stopped. The mortgage did not. The attorney bills by the hour.
3. Every month you wait, that is money you are never getting back.
4. We buy it with the tenant still in it. You are out, and the problem is ours.
5. Here is how we get to the number. [Show the worksheet.]
6. [CTA line.]

**Shot list**
| t | Shot | Audio |
|---|---|---|
| 0.0 | Court docket sheet slapped on a desk | line 1 |
| 2.0 | Attorney invoice, hours column scrolling | line 2 |
| 6.0 | Bank app, a payment going out, red | line 3 |
| 10.0 | Presenter matted, cut hard, side to side | line 4 |
| 15.0 | Worksheet | line 5 |
| 23.0 | Keys handed over, door not entered | line 6 |
| 28.0 | Form on a phone, brand name | tail |

**Caption:** Tenant still in it, back rent owed, case still open. Tell us about the property and we will show you the offer and how we got there. [CTA].

---

## Ad 4 - The House Needs Everything

**Persona:** Fixer Upper Fran, retired, fixed income. **Gate 58, the weakest of the five. Smallest budget.**
**Palette:** terracotta and stone. **Objection answered:** you will offer me pennies because it is ugly.
**Named cost that loses:** the contractor's quote she cannot pay.

> Why it scores lowest: there is no named party a stranger already recognises and nobody is angry this exists. It is the gentlest concept in the set. Run it, but do not expect ad 1 or 5 reach.

**Hook, three options.**

| Pattern | Line |
|---|---|
| 17, Myth bust | "The myth is that you have to fix the roof before anyone will buy the house." |
| 14, Overcomplicated | "Everyone makes selling an old house harder than it is." |
| 10, Diagnosis plus fix | "Why the quotes keep coming back higher, and what to do instead of paying them." |

**Banner:** YOU DO NOT HAVE TO FIX IT FIRST

**Script, six lines, 74 words.**
1. The myth is that you have to fix the roof before anyone will buy the house.
2. You got the quote. Roof, furnace, the kitchen. It is more than you have.
3. A lender will not finance a buyer for a house in that shape, so the quote is not optional on the open market.
4. It is optional with us. We buy it exactly as it stands.
5. Here is how we get to the number, and yes, the repairs come off it. [Show the worksheet.]
6. [CTA line.]

> Line 5 is doing the honest work. The research says this audience already knows a cash offer comes in under a retail sale. Admitting the repair deduction out loud is what separates you from the ads they have stopped believing. Do not hide it.

**Shot list**
| t | Shot | Audio |
|---|---|---|
| 0.0 | Water coming through a ceiling stain into a bucket, sound of the drip | line 1 |
| 3.0 | Contractor quote on paper, the total circled | line 2 |
| 7.0 | Old furnace, panel open | line 3 |
| 12.0 | Presenter matted over the hallway | line 4 |
| 16.0 | Worksheet, the repair line highlighted | line 5 |
| 25.0 | Form on a phone, brand name | line 6 |

**Caption:** Roof, furnace, kitchen, all of it. We buy it as it stands and we show you where the repair number came from. [CTA].

---

## Ad 5 - The Skeptic

**Persona:** every persona, at the moment they decide you are like the rest. **Gate 92.** **Palette:** ink navy and white.
**Concept rank 1 from Winning Concepts.** Contrarian callout of the category, then the receipt.
**Objection answered:** it is a scam, and you will lowball me.

**Hook, three options.**

| Pattern | Line |
|---|---|
| 3, Withheld truth | "Here is the part no cash buyer ad shows you." |
| 6, You're doing it wrong | "You are comparing cash offers by the number, and that is why they all look the same." |
| 17, Myth bust | "The myth is that a cash buyer will not show you the math." |

**Banner:** YES, WE ARE ONE OF THOSE CASH BUYERS

**Script, six lines, 88 words.**
1. Here is the part no cash buyer ad shows you.
2. Yes, we are one of those companies. Our offer comes in under a retail sale. That is how this works.
3. What you should be asking is what you actually walk away with.
4. So here is ours, line by line. Worth fixed up. Repairs. Our costs and profit. Your number.
5. Compare it to a listing. Commission, the repair list after the inspection, and the payments you keep making while it sits.
6. [CTA line.]

**On screen at line 5, the comparison.** Do not type a commission rate. Use the seller's own agent quote, or leave the field for them to fill.
```
LIST IT                          SELL TO US
Sale price        $[     ]       Offer          $[     ]
Commission        $[     ]       Commission     $0
Repairs after     $[     ]       Repairs        $0
inspection
Payments while    $[     ]       Closing costs  $[     ]
it sits
You walk with     $[     ]       You walk with  $[     ]
```

> **Compliance on this table.** The research records commenters quoting about 6% commission plus 1 to 2% transfer tax. That is a Reddit opinion, not a verified fact, and it does not go on screen as yours. Either the seller enters their own agent's quote, or the field stays blank on camera. And if the listing column wins for a particular house, say so. The research says the moment you claim you always beat a realtor, this audience stops reading.

**Shot list**
| t | Shot | Audio |
|---|---|---|
| 0.0 | Thumb scrolling a feed of near identical cash buyer ads, fast | line 1 |
| 2.5 | Presenter, full frame, straight to camera, no b roll behind | line 2 |
| 8.0 | Worksheet, one line at a time | line 3 and 4 |
| 17.0 | Two column comparison, both columns filling | line 5 |
| 27.0 | Presenter matted beside the table | line 6 |
| 31.0 | Form on a phone, brand name | tail |

**Caption:** We are a cash buyer. Our offer is under a retail sale, and we will show you exactly how we got there so you can compare what you walk away with. If listing wins for your house, we will tell you that too. [CTA].

---

## CTA block

**Paid version, all five ads.** Line 6 is the same shape every time. No keyword, no scarcity.
> "Tell us about the house. We will send the offer and the math. You can say no."

On screen: the form, the brand name, a button that reads GET MY OFFER AND THE MATH.
The form is 3 to 5 questions: address, condition, timeline, who is on the title, what the house owes.

**Organic version.** Keep Reel_direction's mechanic. One uppercase word, new every time, wired into the DM automation before the post goes live because it is spoken on camera and cannot change afterwards.

| Ad | Keyword | Deliverable it sends |
|---|---|---|
| 1 | HEIR | A one page checklist for selling an inherited house from out of state |
| 2 | COUNSELOR | The HUD counselor lookup, plus what happens at each stage of a missed payment |
| 3 | OCCUPIED | What a sale with a tenant in place actually looks like |
| 4 | ASIS | The repair deduction, explained, with a blank worksheet |
| 5 | MATH | The offer worksheet as a blank you can run on your own house |

These five are clean against `~/Documents/Notes/reel-system/keywords_burned.txt`, but that file belongs to @billy.coder. Start a separate burned list for this brand before the first post.

---

## Before any of this runs

1. **The website.** `propertyabundanceusa.com` returned HTTP 403 on 2026-09-22. An ad that sends traffic to a dead form burns the whole budget. Re-check it, and re-check it the day you launch.
2. **The worksheet has to be real.** Ads 1 to 5 all end on it. You need a value, repairs and costs line you are willing to show a seller. Without it this set has no payoff beat and it turns into the same feature list as everyone else.
3. **Fill every `[ ]`.** No number on screen unless it is true for this business.
4. **Ad 3 needs a yes on buying occupied houses.** Ad 2 needs the real counselor link.
5. **Housing Special Ad Category.** Register the ad account for it. Expect targeting to be stripped. That is why each ad is one situation.
6. **Fair Housing.** Nothing in a script or a visual may signal a preference by race, colour, religion, sex, disability, familial status or national origin. Cast and caption with that in front of you.
7. **No testimonial staging.** The presenter speaks as the company. Never as a past customer.
8. **Name conflict.** "Property Abundance" is also a UK property training company. A seller who searches the name after seeing the ad will probably find them. Decide the ad facing name before spending.
