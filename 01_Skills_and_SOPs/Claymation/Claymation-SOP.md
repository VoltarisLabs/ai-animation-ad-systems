# Claymation SOP
Source: https://www.canva.com/design/DAHFo1UG8aA/_zSEiFDatzhKEz8l2D7FCA/view (Canva whiteboard by "Howieee")
Extracted: 2026-09-21. Text only: the board's embedded example images/videos are not included.

## What is claymation?
A stop-motion animation technique where characters and objects made from clay are moved slightly between each frame to create the illusion of movement.

## Automation process
Pipeline: ChatGPT (prompt writer) -> NanoBanana 2 (frames) -> Kling 3.0 (video).

---

## 1. ChatGPT

### Setup
- Go to ChatGPT.
- Left column -> "New Project."
- Name the project to your liking.
- Once created, click "sources".
- Click "add", select text input, paste all the contents of THIS document into the "text" section. Title is not needed.
- Save.

### How to use
- Click the text bar below the project name to start a new conversation.
- Literally describe what you want to see in the frame. Example: "A close up shot of an anthropomorphized tomato taking a walk in a garden. The sun is beaming on the top right of the corner. It's holding a Gucci bag. Wearing Prada sunglasses. The tomato character must be in the center of the frame."
- Send the message and watch it cook.

### Don't know what to say/show? Ask:
- What is this part of the script actually saying in one sentence?
- What does the viewer need to understand here?
- Is this moment explaining, proving, transitioning, or creating emotion?
- If I could only show one thing here, what would it be?
- What would be confusing if I showed nothing?

### Tips on prompting
If you created a clay character and want GPT to refer to it, include at the beginning of the script:
- Image generated with the previous prompt: "With the image generated above as reference image."
- Image of the character from a separate conversation: upload the image to GPT, then "The attached image will also be given to nanobanana as a reference image."

Simple background: "Make the background simple"

Shot angle options:
- 3/4 shot
- Over the shoulder shot
- Straight on shot
- Close-up shot
- Macro shot

Basic structure:
`[shot angle] [character] [action] [background]`

No need to give lighting directions or camera quality, unless you have special requests.

---

## 2. NanoBanana 2
- Once you get the output from ChatGPT, copy and paste everything into NanoBanana 2.
- Use 1k quality and 9:16 frame size.

---

## 3. Kling 3.0

### Setup
- Select Kling 3.0 as the video generation model.
- Select 780p.
- Turn off audio.

### Want continuous flow?
- For a video that looks like it is constantly transitioning, use the start/end frame in Kling 3.0. You need to generate start/end frames.

"How do I know when I need a start frame and end frame?"

Example script: "But our body can only make so much IGF-1, that's why you can't break through your plateau even with more food."

- First generate audio for the script to gauge how long a section takes to say. Based on the audio length, decide how many clips fill the section.
- Rule: 3-5 second audio section = 1 clip. 6-9 second audio section = 2 clips.
- Say "But our body can only make so much IGF-1" takes 3 seconds and "that's why you can't break through your plateau even with more food" takes 5 seconds. Two clips: one 3 seconds, one 5 seconds.
- Clip 1: generate X as start frame, Y as end frame. Set Kling to 3 seconds, input prompt, generate.
- Clip 2: use Y as start frame, generate Z as end frame. Set Kling to 5 seconds, input prompt, generate.

### Want just a clip?
For a normal claymation clip you only need a start frame. Give it to Kling, input your directions, generate.

### Prompting process
If a character is involved, include:
"Keep character facial consistency. No character redesign. No facial feature changes."

Camera directions:
- Static (stays still)
- Slight push-in (camera moves towards subject, often confused with zoom in)
- Slow pan left (stationary camera that horizontally rotates to the left)
- Arc right

Must include animation directions:
"Ensure handmade stop-motion clay animation throughout the video. Non CGI. Non cinematic. Animation must start at the first frame. Non-disney. Non cartoon."

Structure:
`[Visual direction] [camera directions] Ensure handmade stop-motion clay animation throughout the video. Non CGI. Non cinematic. Animation must start at the first frame. Non-disney. Non cartoon.`

Settings must be: no sounds & 780p.

Example prompt:
"Vines around the frame pull back and out of the frame. Hovenial Dulcis falls from the vine it's attached to into the mug of beer. The camera is static. Ensure handmade stop-motion clay animation throughout the video. Non CGI. Non cinematic. Animation must start at the first frame. Non-disney. Non cartoon."

"What if I don't know what to say?"
Replace the `[Visual direction] [camera directions]` sections with:
"Create a handmade stop-motion clay animation transition between start and end frame."
