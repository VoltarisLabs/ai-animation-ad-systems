export const meta = {
  name: 'story-ad-qa',
  description: 'QA a rendered story ad from 3 lenses (sync+sound, visuals+safe zones, compliance), adversarially verify each finding',
  whenToUse: 'After an animated story ad renders and passes qa_checks.sh, before sending it as final',
  phases: [
    { title: 'Review', detail: 'sync, visual, compliance reviewers' },
    { title: 'Verify', detail: 'try to refute each finding with evidence' },
  ],
}

// Claude Code Workflow script. Run with the Workflow tool, passing args like:
// {
//   "dir": "<ad folder, e.g. 10_Video_Builds/Ad_GTA>",          // builder, work/, src/
//   "video": "<ad folder>/out/ad.mp4",
//   "registry": "<repo>/11_Psychological_Hooks/claims-registry.md",  // a fresh copy
//   "python": "python3",                                         // a Python with faster-whisper
//   "script": "The ceiling's leaking, again. ...",
//   "onscreen": "HUD: minimap, STRESS star meter ...; titles ...; end card ...",
//   "builder": "build_hud_ad.py"
// }
// Returns the confirmed findings per lens; each has severity, time, issue, evidence and a concrete fix.

const A = args || {}
for (const k of ['dir', 'video', 'registry', 'python', 'script', 'onscreen', 'builder']) {
  if (!A[k]) throw new Error('qa_workflow: missing arg ' + k)
}
const CONTEXT = `
You are QA-ing a finished vertical 1080x1920 24 fps ad: ${A.video}
It is an animated story ad for a US cash home buyer. Spoken script: "${A.script}"
On screen: ${A.onscreen}
Build files in ${A.dir}: ${A.builder} (the builder), work/caps.ass (all on-screen text with final ad times), work/audio_graph.txt, work/video_graph.txt, work/vo_words.json (word times in the ORIGINAL voice file; the builder maps them to ad time), src/ (clips, stills, sound effects).
Tools in Bash: ffmpeg/ffprobe; Python with faster-whisper at ${A.python} (env HF_HUB_OFFLINE=1, model small.en, cpu, int8, word_timestamps=True). Extract frames with ffmpeg and look at them with the Read tool. Write scratch files ONLY under ${A.dir}/work/qa/ (create it). Do NOT modify any other file.
Safe zones: keep key text out of the top 13% (y<250), the bottom 20% (y>1536) and the right button rail (x>885 for y about 1000-1700).
Report only real, specific problems a viewer or an ad reviewer would notice, each with a timestamp, your evidence and a concrete fix to the builder or render script. No style preferences.
`

const FINDINGS = {
  type: 'object',
  properties: {
    findings: { type: 'array', items: { type: 'object', properties: {
      severity: { type: 'string', enum: ['high', 'medium', 'low'] },
      time: { type: 'string' }, issue: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' },
    }, required: ['severity', 'time', 'issue', 'evidence', 'fix'] } },
    checked: { type: 'string' },
  },
  required: ['findings', 'checked'],
}

const LENSES = [
  { key: 'sync', ask: `SYNC, TIMING AND SOUND. Transcribe the final audio with word timestamps. Check every subtitle, title, list item, strike-through, star pop and toast lands on its words (within about 0.25 s) and clears before the next line or cut; shot cuts fall between lines; nothing lingers across a cut. Check the audio: no clipped words, no clicks at edits, no sound effect masking a word (measure it: per-word band levels, and a whisper A/B with and without each effect), a jingle never buries the call to action, effects land on their visual moment (effects files often have silent lead-ins), overall level about -14 LUFS.` },
  { key: 'visual', ask: `VISUALS, SAFE ZONES, LEGIBILITY. Extract frames every 0.5 s and around every cut, and look at them. Check text or HUD over faces; key text in unsafe zones; text too small or low-contrast for a phone; overlapping text elements; AI glitches in the clips (hands, faces, character or house drift, garbled text or numbers generated in frame); freeze frames and stills (borders, softness, shimmer); jarring cuts.` },
  { key: 'compliance', ask: `COMPLIANCE. Read the claims registry at ${A.registry}; it is the source of truth. List every spoken and on-screen word and check each against its Section 5 checklist: only Section 1 claims in approved or narrower wording, neutral verbs (no "we buy", "we're the buyer", "no middleman"), nothing from Sections 2-4 (no numbers or $, no speed or timeline, no "any condition", no top dollar or best price, no fake urgency, no competitor names, no testimonial or "I sold my house" framing, no "you are / you have" + a personal attribute). An admission line keeps its hedge and its close. Also: no company name; no game or brand names, logos or lookalike logo fonts; no weapons, police or crime; no platform-UI lookalikes (a bare row of stars reads as a rating); a made-up character never reads as a real customer or as the one saying the company's lines; anything a Meta housing (Special Ad Category) reviewer could reject.` },
]

const results = await pipeline(
  LENSES,
  l => agent(`${CONTEXT}\nYOUR LENS: ${l.ask}`, { label: `review:${l.key}`, phase: 'Review', schema: FINDINGS }),
  (rev, l) => rev && rev.findings.length ? agent(
    `${CONTEXT}\nA reviewer (${l.key} lens) reported:\n${JSON.stringify(rev.findings, null, 1)}\n\nREFUTE each one: re-measure or re-look yourself. Keep only findings you confirm with your own evidence; drop wrong, exaggerated or taste-only ones. Sharpen the fixes you keep. Return only confirmed findings.`,
    { label: `verify:${l.key}`, phase: 'Verify', schema: FINDINGS }).then(v => v && ({ lens: l.key, reviewed: rev.findings.length, ...v }))
    : { lens: l.key, reviewed: 0, findings: [], checked: rev ? rev.checked : 'reviewer failed' },
)
return results.filter(Boolean)
