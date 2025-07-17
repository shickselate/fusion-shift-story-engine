# Fusion Shift: Story Engine
A generative storytelling system for multiplayer space strategy games.

This engine turns player-driven events into dynamic, character-rich narratives — complete with faction drama, cinematic flair, and visual prompts for AI-generated media.

## 🚀 What It Does
Fusion Shift’s story engine listens to structured game data — battles, diplomacy, espionage — and responds with:

- 📝 Auto-generated narrative: Rich text describing what just happened (and why it matters)
- 🖼 Image + video prompts: For use with tools like Midjourney, DALL·E, Sora, or Runway
- 🎭 Character and faction arcs: Expanding over time, driven by real gameplay
- 🗞 News feeds: Personal, factional, and galactic-level perspectives
- 🧠 Outcome-driven events: Each game event includes a resolution (victory, defeat, treaty, sabotage, etc.)

## 🧠 Core Modules

| Folder       | Purpose |
|--------------|---------|
| `engine/`    | Core story engine logic (event processing, narrative generation, story queue) |
| `prototypes/`| Experimental tools (e.g. media prompt builders, tone mappers) |
| `docs/`      | System design, architecture, and creative notes |
| `tests/`     | Unit and functional test scripts |
| `assets/`    | Optional folder for portraits, icons, example exports |

## 📄 Key Docs

- `docs/architecture/FS_StoryEngine_Architecture_v1.0.md`  
  🔧 System overview: layers, pipelines, inputs and outputs

- `docs/designNotes/FS_DesignCompanion_ReliabilityAndFlow_v0.1.md`  
  🧭 Narrative flow: event handling, async design, story queue principles

- `docs/designNotes/FS_VisualNarrative_Hooks_v0.1.md`  
  🎨 Visual storytelling: prompt scaffolding for images + videos

## 🔍 Example Usage

```bash
python engine/storyQueue.py

```


Outputs a styled image prompt based on an example in-game event.  
Future versions will run live against real game data or player submissions.

---

## 🧪 Status

This is a **work-in-progress prototype**, being developed collaboratively by:

- **Stephen Hicks** – creative director, narrative systems  
- **ChatGPT** – technical assistant and code collaborator

Designed to integrate with the multiplayer game *Fusion Shift* created by Andy Longhurst.

---

## 🌱 Goals

- Provide compelling, player-specific stories in real time  
- Blend text, media, and memory across turns and campaigns
- Track world state for memory and causality  
- Eventually allow player agency in shaping stories, alliances, betrayals, and dynasties

---

## 📬 Contact

To get involved, ask questions, or contribute:  
→ [Reach out here or drop an issue on GitHub]

---

## 📜 License

MIT (or TBD — placeholder for now)

---

> *“The stars remember. Let the game tell why.”*
