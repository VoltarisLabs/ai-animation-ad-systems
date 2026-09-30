# Example: GTA-style "Stress Meter" (34 s)

Chosen from a four-angle judge panel (mission / stress stars / cutscene name cards / loading-screen tips) because it had the strongest first second and the most recognisable game device.

## Final script (Option A, no company name)

| Part | Narrator says | What we see |
|---|---|---|
| Open A | "The ceiling's leaking, again. Stress meter? Maxed out." | Ceiling patch bursts onto Ray's face; STRESS stars slam on; comic freeze with RAY / HOMEOWNER |
| Open B | "Repair quotes piling up, weekends on a ladder, and everyone says: fix it all, then list it." | Kitchen table behind a stack of papers (still, push-in); Ray up a ladder, head drops. Toasts + REPAIR QUOTES, + WEEKENDS LOST; objective FIX IT ALL. THEN LIST IT. |
| Open C | "There's another way out." | Porch, a glowing mission marker appears in the driveway. NEW MISSION: SELL IT AS-IS |
| Main | "Listing means repairs, cleanup, commission and closing costs. This cash offer? None of that." | Red cost list builds item by item; camera orbits Ray inside the light; list struck through, first star pops |
| Close C | "Take what matters, leave the rest." | Porch steps, cap pushed back, relief; star pops (LEAVE WHAT YOU DON'T WANT) |
| Close B | "Fix it all first? No need. The house sells as-is." | Same kitchen still becomes a clip: one arm sweep sends the stack into the bin; objective struck through; star pops (SELLS AS-IS) |
| Close A | "You pick the closing date. And that stress meter? Empty." | Walks down the driveway with a keepsake box, glances back and smiles; last stars pop; MISSION COMPLETE |
| Ask | "Ask for a cash offer. No obligation." | Poster end card: sitting on the tailgate. NEW OBJECTIVE / ASK FOR A CASH OFFER / No obligation. |

## Shots made in Flow (order of generation)

1. Ray character sheet (Nano Banana Pro) and the house (Nano Banana Pro) — prompts in `references/flow-prompting.md`.
2. C1 splash (Veo, Ray): living room, drip at 0-1 s, dinner-plate patch bursts at 1 s onto his face, ceiling stays intact.
3. S2 kitchen still (Nano Banana, Ray): head in hand, tall blank stack with a paint roller at the table's left, blue bin on the floor at the left. Kept exactly: it is also C6's first frame.
4. C2 ladder (Veo, Ray + house): already three rungs up an unmarked ladder, climbs one more, stares along the sagging gutter, head drops.
5. C3 beam (Veo, Ray + house): back to camera at the top of the porch steps, wipes his brow, a plain cylinder of golden light rises in the driveway, slow push-in.
6. C4 orbit (Veo, Ray + house + a frame of the beam): standing arms crossed inside the light, quarter orbit 0-3 s, then one skeptical nod.
7. C5 porch (Veo, Ray + house): seated on the steps, pushes cap back, wipes forehead, long breath out.
8. C6 sweep (Veo Frames to Video, first frame = S2): lifts head, one arm sweep pushes stack and roller into the bin, sits back smiling.
9. C7 walk (Veo, Ray + house): carries a box (baseball glove, back of a photo frame) down the driveway past a plain teal pickup with no emblem or plate, glances back and smiles.
10. S8 end card (Nano Banana, Ray + house + a frame of the truck and box): sits on the lowered tailgate, whole body visible, box and glove beside him, halftone sunset.

## Edit facts

- Voice: an ElevenLabs voice of a voice artist used with his stated consent (written consent to be filed before launch); 32 s, already tight; pauses stretched after "maxed out" (0.45), "another way out" (0.45), "none of that" (0.55), "empty" (0.75). An earlier 43 s version used the Brian library voice.
- Star pops at the end of: "None of that", "leave the rest", "sells as-is", "closing date", "Empty".
- Sound: clip ambience 0.16-0.30; short effects on the star slams, toasts, pops, the mission title and the end card, and a closing jingle after "Empty" ducked under the CTA; master fade at the end. Only synthesized effects (`scripts/make_synth_sfx.sh`) or effects with a written licence filed in PERMISSIONS.md may run.
- Builder: `scripts/build_hud_ad.py`. Loudness -14.0 LUFS.
- Launch blocked on: landing page 403, written voice and sound-effect permissions, owner review of the Ray character.
