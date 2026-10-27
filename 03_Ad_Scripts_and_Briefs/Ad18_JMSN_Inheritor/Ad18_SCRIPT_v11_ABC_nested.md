# Ad 18 v11: three nested loops, A → B → C, closed C → B → A (2 lines rewritten)

Written 2026-09-29. v10 with 2 lines replaced after the user's note: "on your timeline. You pick the closing date. Choose something different, like 'Closing in 30 days or less'" and "So how do you know it's legit?… these doesnt sound good." The v10 brief, from the user on v9: "I want the hooks in this structure: Open A, then payload; Open B, then payload; Open C, then payload; Close C, then payload; Close B, then payload; Close A, then payload; CTA." Script only, no visuals.

- **Closing timeline:** "within 30 days" is the user's own number (2026-09-29: "Closing in 30 days or less"); "or whenever you're ready" keeps the confirmed seller-picks-the-date term.
- **Kept:** v8/v9's hook line, no name or company, cash as the main message, the legitimacy benefit.
- **Only the user's terms:** cash buyer, buys the house itself, as-is, belongings can stay, no commission, no fees, no closing costs, the seller picks the closing date, no obligation. Bonus = the middleman fee (user, 2026-09-29).

```text
[OPEN A]   Hold up. Cash for your house, plus a bonus nobody told you about.
[payload]  Any condition. Closed within 30 days, or whenever you're ready.
[OPEN B]   And how do you know this is legit? I'll show you.
[payload]  Take what you love, and leave the rest. Furniture, boxes, all of it.
[OPEN C]   Plus, there are three costs you get to cross off your list.
[payload]  You won't fix a thing, patch a thing, or paint a thing.
[CLOSE C]  Agent commission. Fees. Closing costs. All crossed off.
[payload]  Cash in your hand, and the house off your plate.
[CLOSE B]  Here's how you know it's legit. I'm the one buying it. I'm paying cash. And nothing happens until you say yes.
[payload]  No pressure. Just a straight cash offer.
[CLOSE A]  And that bonus nobody told you about? There's no middleman in my deals, so the middleman's fee stays with you.
[payload]  Cash, a bonus, and your closing date. All yours.
[CTA]      Tap the link below, tell me about the house, and I'll send you a cash offer.
```

## The loops
| Loop | Opens (the question) | Closes (the answer) |
|---|---|---|
| A | 0.00 s "a bonus nobody told you about" | 39.89 s: the middleman's fee stays with you |
| B | 7.84 s "how do you know this is legit?" | 30.34 s: the one buying it, paying cash, nothing happens until you say yes |
| C | 16.02 s "three costs you get to cross off" | 24.20 s: commission, fees, closing costs |

The biggest promise (the bonus) closes last, and every close happens while another loop is still open (`loop-order-rule`).

## Numbers (estimates: words × 60/176)
- 162 words, 55.23 s at JMSN's 176 wpm (R2: 50.92 s, R3: 55.77 s).
- "cash" at 0.68 s, "bonus" at 2.73 s, "timeline" at 5.80 s.
- CTA at 49.77 s = 90.1%.
- Shared with R5's transcript: 0 four-word phrases, 2 three-word phrases ('30 days or', 'the link below'). No name, no company.

