# Ad 18 v10: three nested loops, A → B → C, closed C → B → A

Written 2026-09-29. The user on v9: "I want the hooks in this structure: Open A, then payload; Open B, then payload; Open C, then payload; Close C, then payload; Close B, then payload; Close A, then payload; CTA." Script only, no visuals.

- **Kept:** v8/v9's hook line, the closing timeline in the line after it, no name or company, cash as the main message, the legitimacy benefit.
- **Only the user's terms:** cash buyer, buys the house itself, as-is, belongings can stay, no commission, no fees, no closing costs, the seller picks the closing date, no obligation. Bonus = the middleman fee (user, 2026-09-29).

```text
[OPEN A]   Hold up. Cash for your house, plus a bonus nobody told you about.
[payload]  Any condition, on your timeline. You pick the closing date.
[OPEN B]   And how do you know this is legit? I'll show you.
[payload]  Take what you love, and leave the rest. Furniture, boxes, all of it.
[OPEN C]   Plus, there are three costs you get to cross off your list.
[payload]  You won't fix a thing, patch a thing, or paint a thing.
[CLOSE C]  Agent commission. Fees. Closing costs. All crossed off.
[payload]  Cash in your hand, and the house off your plate.
[CLOSE B]  So how do you know it's legit? I'm the actual buyer, I pay cash, and you're never obligated to say yes.
[payload]  No pressure. Just a straight cash offer.
[CLOSE A]  And that bonus nobody told you about? There's no middleman in my deals, so the middleman's fee stays with you.
[payload]  Cash, a bonus, and your closing date. All yours.
[CTA]      Tap the link below, tell me about the house, and I'll send you a cash offer.
```

## The loops
| Loop | Opens (the question) | Closes (the answer) |
|---|---|---|
| A | 0.00 s "a bonus nobody told you about" | 39.89 s: the middleman's fee stays with you |
| B | 7.84 s "how do you know this is legit?" | 30.34 s: the actual buyer, cash, never obligated |
| C | 16.02 s "three costs you get to cross off" | 24.20 s: commission, fees, closing costs |

The biggest promise (the bonus) closes last, and every close happens while another loop is still open (`loop-order-rule`).

## Numbers (estimates: words × 60/176)
- 162 words, 55.23 s at JMSN's 176 wpm (R2: 50.92 s, R3: 55.77 s).
- "cash" at 0.68 s, "bonus" at 2.73 s, "timeline" at 5.80 s.
- CTA at 49.77 s = 90.1%.
- Shared with R5's transcript: 0 four-word phrases, 1 three-word phrase ("the link below"). No name, no company.

## If there's a real closing number
Line 2 says "on your timeline" because no closing speed is confirmed. A real number of days would go there.
