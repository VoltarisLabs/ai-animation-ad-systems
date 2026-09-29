<!-- Last reviewed 2026-09-29 -->
# AI Animation Ad Systems (Ugc_on_Demand)

The UGC ad studio for **Property Abundance** (cash home buying), plus a reference library for AI ad creative. Not a code project: no build, no tests. It holds skills, prompt libraries, ad scripts, audience research, templates, characters and audio assets.

Since 2026-09-25 the production route for AI UGC is **Kie.ai**: Nano Banana Pro makes the avatar image, Gemini Omni makes the talking video. Claude writes the prompts and settings. The user runs the generations in the Kie web app.

Since 2026-09-21 it is a git repo, pushed to `https://github.com/VoltarisLabs/ai-animation-ad-systems` (remote `origin`, branch `main`). `.gitignore` keeps these out of the repo, and they stay local only: `07_Assets/`, `08_Software/`, `.env`, `__pycache__/`, five `.webarchive` files over GitHub's 100 MB per-file limit (the four in `01_`/`02_`/`05_` plus the root `research.webarchive`), and Emily's real reference photo with its two compare sheets (`12_AI_Characters/Emily/ref_car_selfie.jpeg`, `compare_ref_vs_v1.jpg`, `compare_ref_vs_v4.jpg`; licence unknown and the repo is **public**). Personal data is kept out too (user rule, 2026-09-26: "do not share any personal data"): `session-chat/` and `11_Psychological_Hooks/Screenshot*`. Everything else, including `13_Generated/`, was committed on 2026-09-26.

**Public repo, no personal data.** Before any push, scan the files for names, local paths (`/Users/...`), personal emails, phone numbers, passwords and screenshots. Scripts find the project root relative to their own file, never by a hard-coded home path. Commits use the repo-local identity `VoltarisLabs <257142603+VoltarisLabs@users.noreply.github.com>` in UTC (`TZ=UTC`), never a personal email.

## Open questions (owner decisions pending)

- (a) The repo is public, but the README warns it holds verbatim Ad Creators Lab course material. Make the repo private, or remove that material?
- (b) Business-model contradiction plus unconfirmed offer terms. The owner's 2026-09-25 confirmation said "Property Abundance buys the house itself (no wholesaling)", but the owner's Sep 29 2026 meeting notes (strategy call) describe the core business as wholesaling: secure a property under contract, sell the contract to an investor, profit the spread. Decision needed: the owner must rule on which model the ads speak for. Until then every direct-buyer claim ("we buy it ourselves", "we're the buyer", "no middleman", "not wholesalers") is do-not-use; see `11_Psychological_Hooks/claims-registry.md` Section 2. If wholesaling is the model, Ohio R.C. 5301.95 requires a signed wholesaler disclosure before every contract, and ads attacking wholesalers are deceptive (FTC Act s.5). Still unconfirmed either way: offer/closing speed, "we show you the math", "any condition".
- (c) `propertyabundanceusa.com` returns HTTP 403, which blocks all ad CTAs.
- (d) No LICENSE file on a public repo.
- (e) Git history is ~693 MiB with a 53.6 MiB .mov tracked (`10_Video_Builds/Ad15_Emily_30s_UGC/Ad15_full_merged.mov`); LFS or a history rewrite is an owner decision.
- (f) The root commit 3504adb carries the owner's personal email in public git history, against the repo identity rule. Fixing requires a history rewrite (git filter-repo mailmap) + force push + GitHub support purge; all 24 commit hashes change. Owner must approve before anyone attempts it.
- (g) `03_Ad_Scripts_and_Briefs/README.md` now indexes script statuses; keep it current when adding scripts.

## Layout

| Folder | What lives here |
|---|---|
| `01_Skills_and_SOPs/` | One subfolder per ad format. Each holds the skill or SOP file **plus** its related tutorials and prompt PDFs: `Skeleton_Ads/`, `Claymation/`, `Crochet_Ad_Visuals/`, `Seedance_UGC/`, `Singing_Animation_Ads/`, `Talking_Objects/` |
| `02_Prompt_Libraries/` | Cross-format prompt banks (Ad Creator's Lab, POPPY, SORA 2 Pro hooks) |
| `03_Ad_Scripts_and_Briefs/` | Finished and in-progress ad scripts, clip prompts, headline banks, scripting frameworks |
| `04_Audience_Research/` | Research on cash home sellers. `Buyer_Avatar/` holds the three buyer avatars and their hook map. `Research_Document_Cash_Home_Buying.md` holds the offer terms (still PLACEHOLDER). |
| `05_Tutorials/` | Tutorials that do not belong to one format, and the one hook psychology file |
| `06_Canva_Ad_Templates/` | 61 numbered Canva template PDFs (1-62 with 45 missing) |
| `07_Assets/Audio/` | Sound-effects library (`Sound Effects/`) + loose music/SFX mp3s |
| `07_Assets/Stock_Video/` | B-roll (local only). Video: 24 Pexels clips pulled through the API on 2026-09-22, plus 7 object-only clips added on 2026-09-26 (`closet_`, `house_`, `forsale_`, `roof_`, `junk_`, `contract_`, `ceiling_`; see `10_Video_Builds/Ad15_Emily_30s_UGC/SOURCES_v4.md`). |
| `07_Assets/Reference_Ads/` | Downloaded reference ads (local only). `v2/` holds 35 cash-buyer ads + contact sheets + measurements; the write-up is `07_Assets/Reference_Ads/Reference_Videos_for_House_Buying.md` (renamed from `Cash_Home_Buying_Reference_Ads_v2.md` on 2026-09-26) |
| `08_Software/` | Installers (Ollama.dmg) |
| `09_Characters/` | `CHARACTER_SHEET_PROMPT_TEMPLATE.md` and the `JMSN-3D` animated character |
| `10_Video_Builds/` | One subfolder per rendered ad: the working files (scene file, voice, timings, synth scripts, contact sheet). Ad 5 and Ad 6 still hold their final mp4s from before 2026-09-25. New finished videos go in `13_Generated/videos/`. |
| `11_Psychological_Hooks/` | Hook scripts built with psychology (nested loops A→B→C, closes in reverse), plus the copywriting playbook (merged in from `14_` on 2026-09-26): `frameworks.md`, `triggers-index.md`, `research-playbook.md`, `offer-and-mechanism.md`, `testing-and-iteration.md`, `01-copywriters/`, `02-psychology/`, `03-modern-creators/`, `prompts/` (copy-prompts.md with 11 ready-to-paste prompts, plus the transcript extraction prompt), `templates/` (including `script-and-scene-breakdown.md`) and `transcripts/` (extractions go here). Its `README.md` is the index. Writing an ad starts at its `AD_COPY_CHECKLIST.md`; the psychology is in `triggers-index.md`. The hook psychology research report stays in `05_Tutorials/Hook_Psychology_Research_Report.md`. |
| `12_AI_Characters/` | One subfolder per realistic UGC avatar: the real reference photo with its licence, the prompts, the README and compare sheets. The avatar PNGs made up to 2026-09-25 (JMSN v1, Emily v1 and v4) are still here. New avatar images go in `13_Generated/images/`. |
| `13_Generated/` | **Every generated image and video.** Two subfolders only: `images/` and `videos/`. The loose media that used to sit at the root moved into them on 2026-09-25 (there are no `C_/` or `videos_Free/` subfolders). Committed to git since 2026-09-26. |
| `session-chat/` | One `.session.md` per working session. Read these first. Local-only: `session-chat/` is gitignored and not on GitHub. |

## AI UGC pipeline (Kie.ai)

The method is the `kristian_jennings_ai_ugc_workflow` skill. Read its `SKILL.md` before any UGC job. Effort split 50 / 25 / 25: the reference image, then one locked video prompt, then the rest of the script.

| Step | Skill | Kie model | Output goes to |
|---|---|---|---|
| 1. Script and hooks | `reel_direction_2`, `hook-engine`, `humanizer` + `05_Tutorials/Hook_Psychology_Research_Report.md`. Every script must pass `11_Psychological_Hooks/AD_COPY_CHECKLIST.md` before voice or video. | none | `03_Ad_Scripts_and_Briefs/` or `11_Psychological_Hooks/` |
| 2. Storyboard | Kristian: script lines left, visual right, "AI UGC" where the face shows | none | `03_Ad_Scripts_and_Briefs/` |
| 3. Reference frame | Kristian step 1: a real frame from real phone footage | none | `12_AI_Characters/<Name>/ref_*` |
| 4. Avatar image | Kristian step 2 + `nano_banana_photo_formula` or `json-prompting` | `nano-banana-pro` | `13_Generated/images/` (prompts stay in `12_AI_Characters/<Name>/`) |
| 5. Talking clips | Kristian step 3 | `gemini-omni-video` | `13_Generated/videos/` |
| 6. Edit and captions | `dynamic_captions_3click`, ffmpeg | none | Final mp4 in `13_Generated/videos/`. Working files in `10_Video_Builds/<Ad>/` |

Other skills that fit here: `character_anchor_gemini` (same face across scenes), `ugc-style-video` (Kie model routing; its `tools/` scripts do not exist, so use it for routing ideas only), `dan_kieft_ugc_workflow` (Sora 2 / Kling 3.0 recipe), `anthropic-skills:seedance-20-ugc-ad-director` (Seedance prompts). The format skills (`talking-objects-ads`, `claymation-ads`, `skeleton-ads`, `crochet-ad-visuals`, `singing-song-style-ads`) cover the non-human ad styles.

**Note for repo readers:** several skills and memories named in this pipeline (`kristian_jennings_ai_ugc_workflow`, `reel_direction_2`, `hook-engine`, `humanizer`, `nano_banana_photo_formula`, `json-prompting`, `dynamic_captions_3click`, `character_anchor_gemini`, `ugc-style-video`, `dan_kieft_ugc_workflow`, and the `veo-realism-prompt-rules` and `loop-order-rule` memories) are local-only in the owner's Claude environment and are not files in this repo. Treat the pipeline table as owner-environment documentation, not as steps reproducible from a fresh checkout; the repo-side pieces that do exist are the scripts (`kie_nbp.py`, `kie_omni.py`), the checklists in `11_Psychological_Hooks/` and the SOPs in `01_Skills_and_SOPs/`.

### Kie models and settings (docs.kie.ai, checked 2026-09-25)

All jobs: `POST https://api.kie.ai/api/v1/jobs/createTask`, then poll `GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=<id>`. One credit is $0.005 (Kie pricing page).

| Job | Model | Settings | Cost |
|---|---|---|---|
| Avatar image | `nano-banana-pro` | Up to 8 `image_input` URLs. `aspect_ratio` includes `9:16`, `3:4`, `4:5`. `resolution` `1K` / `2K` / `4K`. `output_format` `png` / `jpg`. | 18 credits per image, measured for 1K and for 2K (2026-09-25) |
| Talking clip | `gemini-omni-video` | `duration` is a string: `"4"`, `"6"`, `"8"`, `"10"`. `aspect_ratio` `9:16` / `16:9`. `resolution` `720p` (default) / `1080p` / `4k`. Max 7 slots: 1 per image, 1 per character ID, 2 per video. Prompt up to 20,000 characters. | 720p/1080p: 63 / 84 / 105 / 126 credits for 4 / 6 / 8 / 10 s. 4K: 147 / 168 / 189 / 210. With a video input: 168 (1080p) or 252 (4K). Kie list prices, not measured. |
| Locked character | `POST /api/v1/omni/character/create` | `image_urls`: portrait at index 0, optional body shot at index 1. Plus `descriptions` and `character_name`. Returns a character ID to pass as `character_ids` in Omni video. | Not published. Measure it. |
| Draft clip | `google/gemini-omni-flash-1-1` | Same durations. Adds `360p`. | Not measured. Kristian uses full Omni, not Flash, for finals. |
| Alternative | `veo-3-1` | `duration` 4 / 6 / 8. `720p` / `1080p` / `4k`. `9:16`, `16:9` or `Auto`. | Kie tagline: $0.4 Fast, $2 Quality per video. Not measured. |

### Script

`python3 12_AI_Characters/JMSN/kie_nbp.py <prompt.txt> 13_Generated/images/<Ad>_<what>_v<n>.png <aspect> <res> <img1> [img2 ...]`

It uploads the reference images, creates a `nano-banana-pro` task, polls it and downloads the PNG. It reads `KIE_API_KEY` from `.env`. The video runner is `12_AI_Characters/kie_omni.py` (Kie Gemini Omni, checked 2026-09-26): same upload/create/poll/download flow for `gemini-omni-video` talking clips, with upload and download retries, taking `<prompt.txt> <out.mp4> <duration> <aspect> <res> <img1> [img2 ...]`.

### Rules for Kie work

- **Hand-off is the default.** Give the prompt, which images to upload in which order, and the settings (model, aspect, resolution, duration). Call the API only when the user says "generate" in their own words. A settings change such as "1K, not 2K" is not a go-ahead. On 2026-09-25 that misread spent 18 credits nobody approved.
- **Before any API run,** say the number of generations and the credits. Check the balance before and after with `GET https://api.kie.ai/api/v1/chat/credit` (free), and write both numbers in the session file.
- **1080p means 1080 × 1920 vertical.** Nano Banana Pro 3:4 measured 896 × 1200 at 1K and 1792 × 2400 at 2K. Both cost 18 credits, so use 2K and downscale. The 9:16 pixel sizes are not measured yet.
- **One-shot the avatar edit.** Put every change in one prompt and regenerate it. Never stack edits: each edit adds seams that show once the image is animated.
- **The avatar must be a different person.** Change eye colour, nose, face shape and skin, not only hair and clothes. Emily v1 kept the reference's brows, nose, smile and jaw and failed this test.
- **State the framing.** Both v1 avatars drifted to a centred, pulled-back dash-mount shot. Write "close, off-centre, arm's-length selfie" and the camera angle into every prompt.
- **Screen the reference.** Real phone footage only. Measure the face box for clipped pixels (all channels ≥ 250). Record the source and licence in the character's README. A CC BY-SA photo needs a ShareAlike check before the ad runs.
- **Omni prompt in three parts:** scene and camera, dialogue in quotes, stacked rules ending with "one continuous take, no jump cuts". Lock it on one line, then change only the dialogue. Pad a line that falls between 4 / 6 / 8 / 10 s and cut the padding in the edit. CAPITALISE a word to stress it.
- **Realism rules** from the `veo-realism-prompt-rules` memory apply to Omni too: amateur handheld look, no "cinematic" or "photorealistic", no printed text or screens facing the camera, simple hand actions, the full character description repeated in every clip.
- **Compliance.** A "customer" avatar needs an on-screen AI and dramatization label (16 CFR 255.2(c)). No prices, timelines, counts or guarantees in frame while the offer terms in `04_Audience_Research/Research_Document_Cash_Home_Buying.md` are PLACEHOLDER.
- **Hooks** use nested or staggered loops only (`loop-order-rule` memory). Hook psychology lives in `11_Psychological_Hooks/` (the playbook); the deeper research report is `05_Tutorials/Hook_Psychology_Research_Report.md`.

### Review hub (Airtable)

Base `appJ28xFZNqaHmW4u`, table `Content` (`tblFSvTEVLwDXOk2G`), set up 2026-09-25 through the Airtable MCP. There is **one row per ad**. Each stage has its own status field (Script, Storyboard, Image, Video, Final): Pending → Generated → Approved / Rejected.

- The user deleted the cost fields (Credits Estimate, Cost Estimate (USD), Credits Spent) on 2026-09-25. Don't recreate them. Put the cost before generation in the chat summary, and put the measured cost spent in the row's `Notes`.
- The `creator-engine` skill's Python `tools/` folder is not installed, so write rows with the Airtable MCP.
- Ad 15 is row `recf8ByD6pxQSMwp9`.

**Rule: UGC images and videos go on Airtable, nothing else (user rule, 2026-09-25).**
- **In:** the pictures and videos of the AI UGC ads: avatar reference frames, avatar images, talking clips, UGC b-roll and the final UGC cut. That applies whether the user made them in the Kie web app or Claude made them through the API.
- **Out:** the other formats (claymation, crochet, skeleton, singing, talking objects, whiteboard, 3D), research and reference-ad downloads, and non-UGC renders in `10_Video_Builds/`. These stay local only.
0. **Before any paid generation:** post a cost summary as plain chat text and wait for a typed go-ahead. No pop-up question. The summary lists what gets made, how many, the service, the model, the settings, the inputs, the credits and $ per item and in total, the Kie balance before and after, and where the files go.
1. **New ad:** create its row first. Fill in the Script and the prompts before anything is generated.
2. **After a generation:** attach the file to its field with `python3 12_AI_Characters/airtable_attach.py <recordId> "<field>" <file> [file ...]`.
   - Avatar images go in `Generated Image 1` / `2`.
   - Talking clips and b-roll go in `Generated Videos`, with filenames `<Ad>_clip1_…`, `<Ad>_clip2_…`.
   - The finished edit goes in `Final Video`.
   - Reference frames and face anchors go in `Reference Images`.
3. **Then** set that stage's status to `Generated`, and write the credits spent in `Notes`: check the Kie balance before and after (`GET https://api.kie.ai/api/v1/chat/credit`, free).
4. **Only the user** sets `Approved` or `Rejected`. The next stage uses Approved files only.

How `airtable_attach.py` works:
- It uses Airtable's upload API. Each file can be up to 5 MB, and it adds to what's already in the field.
- A PNG over 5 MB is sent as a JPEG copy; the original is left alone.
- A video over 5 MB won't upload this way. Attach it with `update_records` and the Kie result URL instead: `{"url": "<kie result url>"}`, and Airtable copies the file.
- The token comes from `~/.claude.json` → `mcpServers.airtable.env.AIRTABLE_API_KEY` and is never printed.
- Tested on 2026-09-25: ` AI_ref.jpeg` went into Ad 15's `Reference Images` (736 × 981, 67,627 bytes).

### Characters

| Character | Folder | Who | State (2026-09-29) |
|---|---|---|---|
| JMSN | `12_AI_Characters/JMSN/` | Male, 360 waves, thin mustache and goatee. Property Abundance's buyer (company voice). | v1 done. Gaps listed in its `README.md`. v2 (2026-09-26): 3 house-walkthrough avatar prompts in `prompt_v2_house_walkthrough.md`, not generated yet. |
| Emily | `12_AI_Characters/Emily/` | Woman, 42. Since 2026-09-25 she is **Property Abundance's presenter (company voice)**, never a seller. `character.yaml` still says "heir who sold" and needs updating. | v1 (`Emily_car_v1.png`) rejected: too close to the reference woman. v4 is current: `Emily_car_v4_a.png` and `Emily_car_v4_b.png` are generated, from `prompt_v4_avatar.txt`, `prompt_v4_oneshot.txt` and `prompt_v4_oneshot_9x16.txt` (plus `faces_v4_ab.jpg` for comparison). The v3 two-step prompts (`prompt_v3_step1_sheet.txt`, `prompt_v3_step2_car_selfie.txt`) are superseded and kept for history only. |

**Emily's reference image** (scene, framing and light only, never the face) is `12_AI_Characters/Emily/ref_car_selfie.jpeg`. It is gitignored and local-only (not on GitHub, so it is absent from a fresh checkout). The old root copy ` AI_ref.jpeg` (filename starting with a space) no longer exists in the project root. It is 736 × 981 and its licence is unknown.

`C_Sheet.jpeg` (the JMSN character sheet) is Google AI-generated (C2PA + SynthID). Use it as a face guide only, never as the base frame.

## Rules for this folder

- **Keep a format's files together.** A new skill, its tutorials, its prompt PDFs and its example scripts go in the same `01_Skills_and_SOPs/<Format>/` subfolder. Do not split them by file type.
- **Generated images and videos go in `13_Generated/` (user rule, 2026-09-25).** This covers every AI image and video from any tool (Kie, Gemini, Dreamina, Veo) and every finished render.
  - Images go in `13_Generated/images/`. Videos go in `13_Generated/videos/`.
  - Name new files `<Ad>_<what>_v<n>.<ext>`, e.g. `Ad15_Emily_avatar_v5.png`, `Ad15_clip1_v1.mp4`, `Ad15_final_v1.mp4`.
  - Never save generated media to the project root, `03_Ad_Scripts_and_Briefs/` or `12_AI_Characters/`.
  - These stay out of `13_Generated/`: real reference photos (`12_AI_Characters/<Name>/`), build working files and intermediates (`10_Video_Builds/<Ad>/`), downloaded reference ads and stock (`07_Assets/`).
  - Files moved in on 2026-09-25 kept their old names. `example.com` is an MP4.
- **Never rename or delete the user's source files.** Sorting means `mv` only. Delete only with the user's approval, and send files to the Finder Trash (`osascript` → Finder `delete`), not `rm`.
- New session → write `session-chat/YYYY-MM-DD_<slug>.session.md` at the end.
- **Pushing to GitHub needs the `VoltarisLabs` account.** The user's personal GitHub account has pull-only access (`push: false`) and its push returns HTTP 403. The VoltarisLabs fine-grained token is in `.env` as `GITHUB_TOKEN` (repo `ai-animation-ad-systems`, Contents read/write; tested 2026-09-26: login `VoltarisLabs`, `push: true`). Claude Code's auto-mode check blocks Claude's own `git push` to this public repo (`Out-of-Place Publication`) unless the user gives permission for that push in their message. On 2026-09-26, "upload it directly from here. I give you permission" let Claude push (`c1463cc..4e99aa6`). Without that, the user runs this in Terminal:
  `export GITHUB_TOKEN=$(grep '^GITHUB_TOKEN=' .env | cut -d= -f2-) && git -c credential.helper= -c 'credential.helper=!f() { echo username=x-access-token; echo "password=$GITHUB_TOKEN"; }; f' -c http.postBuffer=1048576000 push origin main`
- Kie is paid. The global free-engines rule is overridden for this project by the user's choice (2026-09-25), but never spend credits without the go-ahead above.

## Gotchas

- `kie_nbp.py` has no download retry. On `ContentTooShortError` the task has already succeeded: re-fetch the result URL from `recordInfo`. It costs nothing.
- The Kie upload host that worked is `https://kieai.redpandaai.co/api/file-stream-upload`. Uploaded file URLs are what the models take, not local paths.
- The Unsplash napi returns a bot wall. Openverse works without a key for licensed reference photos.
- B-roll for AI UGC ads is **objects and places only, no other people** (user rule, 2026-09-26). The picture follows her words: closet on "closet", sign on "listing", and so on.
- B-roll video: the Pexels API key is gone from `.env`. On 2026-09-26, with the user's go-ahead to collect from the web, clips were found through pexels.com search and pulled from the site's own download link. The script resolves the 302 redirect and streams the file with curl; loading a whole 4K file into memory got the process killed. Build: `10_Video_Builds/Ad15_Emily_30s_UGC/build_v4.py`. Convert 30/60 fps stock by keeping every source frame and re-timing it (`setpts=N/(24*TB)`); `fps=24` judders on pans. Pexels' ToS bans bulk scraping, so keep downloads to the handful a cut needs.
- Old note (2026-09-26): Pexels' ToS bans scraping. Openverse (`license=cc0,pdm`) gives stills of at most 1024 px. The user rejected stills as "frozen", so use video. Before using a sign or paper, check it for other brokers' names, phone numbers and logos.
- `.webarchive` files are Safari saves. Read them with Playwright or `textutil`; `curl` on the original URL usually fails (Canva returns "Unsupported client" to a default UA; a Safari UA works).
- Canva boards are JS-rendered: the HTML carries no board text. Pull them with Playwright MCP + `document.body.innerText`. Browser rule: always open a **new** Safari window, never reuse the user's tab.
- The claude.ai **Canva MCP connector is not authorized**: OAuth cannot run non-interactively. Any Canva API work is blocked until the user authorizes it.
- Several PDFs are image-only (no text layer). To read one: `sips -s format png --resampleWidth 500 file.pdf --out out.png`, then read the PNG.
- `05_Tutorials/The_video_tutorial.html` is an empty Notion shell: it contains no lesson text.

## Open items

- Emily v4 is current (`Emily_car_v4_a.png` / `Emily_car_v4_b.png`, prompts `prompt_v4_*`); the v3 two-step prompts are superseded. Each new result is attached to Ad 15's row on Airtable and compared against the reference.
- JMSN v1 gaps (no visible waves, framing drift, softened goatee) and its CC BY-SA reference licence.
- Emily's reference licence is unknown.
- No Omni video has been made yet. Lock the first prompt on one line before scripting the rest.
- Offer terms, confirmed by the user on 2026-09-25 and usable under either business model: buys as-is, belongings can stay, no commission, no fees or closing costs, seller picks the closing date, no obligation. **Contradicted (2026-09-29):** the same 2026-09-25 confirmation said Property Abundance buys the house itself (no wholesaling), but the owner's Sep 29 2026 meeting notes describe the core business as wholesaling (secure a property under contract, assign the contract to an investor, profit the spread). The owner must rule on which model the ads speak for; until then every direct-buyer claim is do-not-use per `11_Psychological_Hooks/claims-registry.md` Section 2. Ad-copy consequence: the Hook Bank's "The Catch" v3.1 and every "We're the buyer / no middleman" line CANNOT run. **Not confirmed:** showing the seller the offer math, and any offer or closing speed. So "we show you the math" in Ad12, Ad13 and Ad14 can't run as written. `04_Audience_Research/Research_Document_Cash_Home_Buying.md` still marks all of these PLACEHOLDER.
- Ad 16 (JMSN house walkthrough, 30 s): `03_Ad_Scripts_and_Briefs/Property_Abundance_Ad16_JMSN_Walkthrough_30s_v1.md`. It holds the storyboard and the 4 locked Omni prompts. 76 words, 4 clips of 8 s, 474 credits at list price (not run). None of the 9 vertical refs has a walking presenter, so the walkthrough is an original format. Damage close-up b-roll still has to be found.
- Ad 16 script v2 (history, superseded): `03_Ad_Scripts_and_Briefs/Property_Abundance_Ad16_JMSN_Walkthrough_Script_v2.md` replaced the v1 dialogue (hook "Stop getting repair quotes.", 2 nested loops, 94 words, 5 Omni clips of 6/8/10/8/8 s, 525 credits at list price, aimed at the "House Needs Everything" seller). The current version is `Property_Abundance_Ad16_JMSN_Breakdown_v3.md`; v2 is kept only as the pain-hook control.
- Ad 16 current deliverable: `03_Ad_Scripts_and_Briefs/Property_Abundance_Ad16_JMSN_Breakdown_v3.md` (script + scene breakdown). v2 is kept as the pain-hook control.
- Ad 15 full cut (2026-09-26): `13_Generated/videos/Ad15_final_v2.mp4`, 23.208 s. The picture comes from `10_Video_Builds/Ad15_Emily_30s_UGC/build_final_v1.py` and the sound from `build_final_v2.py` (v1 was too quiet: music 18 dB under the voice). It is clips 1 + 2 (the v4 cut) plus clip 3, which the user generated in another model after Kie Omni failed 7 times: `13_Generated/videos/Woman_recording_car_selfie_video_20260926041442.mp4`. The cut has no brand name, CTA or end card. Waiting on the user's review.
- Latest script: `03_Ad_Scripts_and_Briefs/Property_Abundance_Ad15_Emily_30s_UGC_v2.md` (30 s, 94 words, last word at 28.42 s at 199.1 wpm). Emily speaks as Property Abundance's voice, like the 9 vertical refs in `07_Assets/Reference_Ads/`. **The user does not want AI or dramatization labels**, so an AI avatar never speaks as a seller or customer. The earlier Ad15 files (the long version and the 30 s v1) have Emily as a labelled seller and are replaced. Next step: the storyboard.
- `propertyabundanceusa.com` still returned HTTP 403 "No application found" on 2026-09-25. Fix it before any ad sends traffic there.
