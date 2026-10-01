# Example: game-look "One Mission: Stop the Drain" (33 s)

The team supplied this script and wanted it used as written. It carries claims the registry does not confirm, so it was built with the lines flagged NOT CLEARED and it waits for the owner before launch.

**Not reusable as written:** "back taxes" (the registry's unconfirmed "any situation"), "The back taxes get paid at closing, out of the sale" (unconfirmed), and "Get a cash offer. See the number" (implies an offer for every request; use "Ask for a cash offer. No obligation."). The HUD label HOME VALUE was also flagged: a bar whose remainder turns gold as "his" can read as "you keep the full value minus the taxes", which sits badly with the approved admission that cash offers usually come in lower than listing.

## Script

| Part | Narrator says | What we see |
|---|---|---|
| Open A | "Ray's losing a piece of his house every month." | Tight shot of the house as a shutter rips off and crashes, then wide on Ray; a 12-segment HOME VALUE bar loses a red segment on the comic freeze (RAY / HOMEOWNER) |
| Open B | "Back taxes. Penalties. Interest. And it keeps stacking." | Mail pours through a hallway mail slot; a segment drains after each word, with a red minus bar popping off (no digits) |
| Open C | "So he does what most people do. He hits pause." | 2 AM kitchen, unopened stack; PAUSED slams in over a dimmed, desaturated frame |
| Main | "But pause doesn't stop it. One move does. A cash offer. The house sells as-is." | The bar drains once more under the pause; the pause lifts, he picks up the phone; NEW MISSION: CASH OFFER; toast SELLS AS-IS |
| Close C | "The mail? Handled." | He reads an opened envelope, calm; toast MAIL: HANDLED |
| Close B | "The back taxes get paid at closing, out of the sale." | The stack vanishes in one soft white flash on "paid" and the red segments clear; he lays the letter down |
| Close A | "And what's left of the house? That's his. He picks the closing date." | Sunset at the mailbox, he looks up at the house, then turns to us; the remaining segments turn gold; MISSION COMPLETE |
| Ask | "Get a cash offer. See the number, then decide." | Held sunset frame with a slow push; NEW OBJECTIVE / GET A CASH OFFER |

## Shots made in Flow, and what went wrong

1. Character and house (Nano Banana Pro). A new character: an older man with a grey beard, glasses, denim shirt over a white tee; a two-story blue-grey wood house with a stuffed mailbox. The first kitchen still looked like a famous actor; the fix was a different face description plus "must not resemble any real person".
2. Hook (Veo, Ingredients): three takes. Take 2 tore the roof open and showed his back. Take 3 worked, but its first 1.2 s showed a different-looking face that morphed into Ray, which the review caught. The edit plays those frames as a tight crop of the house and cuts wide after the morph. A tiny stamp square on a mailbox envelope was tracked and painted out frame by frame.
3. Mail slot (Veo): white grid lines were baked into the first 4.5 s; only 4.6-8 s was usable.
4. Kitchen still, then the phone pick-up (Frames to Video from the still).
5. "Handled" still, then the stack-vanish clip (Frames to Video from it). Its first take vanished the stack and brought it back at 1.9 s; the fix kept the clean 1.8 s, exported the last clean frame and made a second clip from it, which joins with no visible cut. One re-roll used the wrong first frame, so the exact file was copied into the person's downloads folder with an obvious name.
6. Sunset close: Ingredients to Video (hook frame + house) gave a different, lighter-skinned man, opened the mailbox instead of closing it and lost the house. The fix: a Nano Banana Pro edit of the hook frame (empty, shut mailbox, golden sunset, everything else the same), then Frames to Video from it. In that clip he mouths words after 4.3 s, so the edit holds an earlier closed-mouth frame, picked after his head turn settles.

## Edit facts

- Builder: written for this ad from `scripts/build_hud_ad.py` (segmented bar instead of stars, PAUSED dim, dip to black, partial slow motion). The techniques are in `references/edit-pipeline.md` section 8.
- Voice: one narrator file, 28.9 s; pauses stretched for the freeze, the PAUSED slam, the toasts, the cuts and MISSION COMPLETE, to 33 s in total. The transcript matched the script word for word.
- Two QA rounds. The first (sync, visuals, compliance, each verified) found the morphing face, the silent mouthing, a RESUME / MAP / SETTINGS menu (Meta's "non-existent functionality" rule), late sounds, juddering slow motion, a jump cut, push-in twitch and subtitles over white envelopes. The re-check of the fixed render found side effects: the hold landed mid head turn, PAUSED covered his eyes, a sharpness pop at a clip join, interpolation shimmer. All were fixed.
- Launch blocked on: the owner confirming the flagged claims and the HUD label, written voice and sound-effect permissions naming this ad, owner review of the new character, and the landing page.
