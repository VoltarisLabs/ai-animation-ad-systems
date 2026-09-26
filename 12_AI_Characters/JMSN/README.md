# JMSN — realistic UGC avatar

Built with the Kristian Jennings method: a real phone photo is the base, and one Nano Banana Pro prompt turns it into the JMSN face. The studio character sheet (`C_Sheet.jpeg`, Google AI-generated, SynthID) is used only as the face and hair guide.

| File | What it is |
|---|---|
| `JMSN_car_v1.png` | Result, 1792 × 2400, 3:4 |
| `ref_car_selfie_flickr_49508457808.jpg` | Real reference photo (image 1) |
| `identity_strip_from_C_Sheet.jpg` | Front, 3/4 and profile crop of `C_Sheet.jpeg` (image 2) |
| `prompt_v1.txt` | The one-shot edit prompt |
| `kie_nbp.py` | Upload → createTask → poll → download script. Usage in its docstring. Reads `KIE_API_KEY` from the project `.env`. |
| `compare_ref_vs_v1.jpg` | Reference and result side by side |

## Generation

- Engine: Kie.ai `nano-banana-pro`, 2K, 3:4, PNG
- Task: `e4263b178869fc8c6f721f2b0c133a8d`, 2026-09-25
- Cost: 18 credits (balance 4263 → 4245). Kie's price page lists $0.09 per 1K–2K image.

## Reference photo source

"Car Selfie of Famous Celebrity Joseph Carrillo" by josephthecelebrity, https://www.flickr.com/photos/182909271@N07/49508457808, licensed CC BY-SA 2.0. Found through Openverse.

ShareAlike: an adapted work must carry the same licence and credit the creator. Check that this fits the ad before it runs. A CC BY (no ShareAlike) or self-shot reference avoids the question.

## v1 gaps (open)

1. No visible 360 waves. The hair came out as a plain short buzz.
2. The framing moved back to a centred, dash-mount look. The reference's close, off-centre arm's-length angle was lost.
3. The goatee is lighter and the lips look slightly smoothed compared to the rest of the skin.
