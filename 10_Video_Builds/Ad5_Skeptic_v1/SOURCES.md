# Ad 5 v2 - footage sources

All footage is from Pexels. Licence checked live at pexels.com/license on 2026-09-24:
commercial use is allowed and "Attribution is not required."
Not allowed, and not done here: selling unaltered copies, redistributing to another stock
platform, using a clip as a trade mark, showing identifiable people in a bad light, or
implying a person endorses the product.

Pulled with a headless Chrome session against `https://www.pexels.com/download/video/<id>/`.
Nothing was screen recorded from another advertiser. No clip below appears anywhere else in
this project, so none of the IDs already in `07_Assets/Stock_Video/` is reused.

| Shot | Pexels ID | What it is |
|---|---|---|
| A | 6031853 | person on a couch scrolling a phone |
| B1 | 36778247 | suburban house, ground level, spring |
| B2 | 31965047 | aerial view of a suburban street |
| C | 5147319 | woman at a kitchen table with a laptop |
| D1, F2 | 37693796 | suburban home with a garden |
| D2 | 36778247 | the same house, later in the clip |
| D3, E2 | 8853415 | worker on a roof |
| D4 | 34835401 | empty interior, sunlit wooden floor |
| D5 | 7578426 | couple going in through a front door |
| E1 | 8471103 | hand putting SOLD on a for sale sign |
| E3 | 7210979 | woman labelling moving boxes |
| F1 | 8496474 | man looking straight at camera |

Voice: edge-tts `en-US-BrianNeural`, generated locally.
Music: `music.py`, synthesized here with numpy, seed 20260924. Original, nothing sampled.
Text, banner, captions, bar chart: `overlay.html`, drawn here, rendered as transparent PNGs.

## v3 additions, 2026-09-24: damage footage

| Shot | Pexels ID | What it is |
|---|---|---|
| D3, REPAIRS | 4882452 | interior with a collapsed ceiling, exposed joists, rubble on the floor |
| D4, OUR COSTS AND PROFIT | 12568633 | a wall broken open, debris across the floor |
| E2, REPAIRS AFTER INSPECTION | 7830152 | a long structural crack down a wall |
| E3, PAYMENTS WHILE IT SITS | 34835402 | damp stained wall in an old room the owner left sitting |

Dropped from v2: 8853415 (the tidy roof worker) and 7210979 (moving boxes). Both were too
clean to sit under a 38,000 repair number.

## Wording taken from the reference reel

`07_Assets/Reference_Ads/ref6_betterpath_testimonial_3797061540433548.mp4`, transcribed
locally on 2026-09-24. Its spoken lines are: "Fire your realtor! I did and it changed my
life. I sold my house exactly as it was. No cleaning, no repairs, no hassle. I got a no
pressure cash offer in 24 hours with no fees or commissions. The whole process was quick,
clear, and stress free. If you're dealing with the same thing, tap the button below, answer
a few quick questions, and see what your offer looks like today."

Two things were taken, both rewritten into company voice:
- "I sold my house exactly as it was" became the on screen kicker **WE BUY IT EXACTLY AS IT IS**.
- "see what your offer looks like today" became the end card line **SEE WHAT YOUR OFFER LOOKS LIKE**.

Nothing was taken from its frame. The reference is an actor speaking as a past customer,
which is an FTC risk under 16 CFR 465.2 and 255.1, so its first person framing was not copied.
Its "24 hours", "no fees or commissions" and "no cleaning, no repairs" promises were not
copied either, because they are that advertiser's terms and not verified facts here.
