# Example: claymation "Put the hammer down" (bonus-cash hook, 43-44 s)

Team lead's idea: open on "Bonus cash if you put the hammer down" with money bursting out of the wall as the clay man hits it. The bonus is not in the claims registry: the ad cannot run until the owner confirms the amount, who qualifies and when it is paid, and adds it to the registry.

**Not reusable as written:** "Bonus cash" / "ask about your cash bonus" are not in the registry, and the Ask "Get an offer." implies an offer for every submission (registry Section 3, not confirmed; use "Ask for a cash offer.").

## Structure

Open A "Bonus cash if you put the hammer down." → story of the leak ("It started with one little leak. Then the ceiling. Then the floor. Now every weekend belongs to this house.") → Open B worry ("if I sell it like this, will I get ripped off?") → more pile-up (repair quotes, the garage) → Open C "Here's the part nobody tells you about selling a house like this." → Main "You can sell it exactly the way it is. No repairs. Leave what you don't want. And you pick the closing date." → Close C "That's the part nobody tells you: you never had to fix it first." → Close B "That's why the choice stays yours. No commission. No closing costs. No obligation." → Close A "So put the hammer down, and ask about your cash bonus." → Ask "Get an offer."

## What the edit did

- The first cut ran 57 s (a 55 s voice read) with long pauses ("too much dead space"). The card-reel builder cut 23 pauses (12.6 s) to reach 43 s, put lead words up at each shot start, enlarged the card and type, zoomed in on the wide house shots, snapped cuts to frames (the text had drifted behind the pictures) and split one long hold into two pops.
- The hook was remade: a new Veo smash clip (prompt in `references/flow-prompting.md`) cut into two shots with a punch-in, shake and 2-frame flash on impact, and an excited re-read of the first line in ElevenLabs (same voice, stability 25, style 60, speed 1.05) spliced over the old one, levelled to about 2 LU above the rest. The hook text moved to the top, above his head, away from the like/share buttons.
- Builder: `scripts/build_card_reel.py` (card look), configured as it rendered this ad, including the new-hook block (`USE_INTRO`). The card backgrounds from `make_card_assets.py` are a close recreation of the originals.
