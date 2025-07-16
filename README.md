# 🌌 Fusion Shift: Story Engine

**A generative storytelling system for multiplayer space strategy games.**

This engine turns player-driven events into dynamic, character-rich narratives — complete with faction drama, cinematic flair, and visual prompts for AI-generated media.

---

## 🚀 What It Does

Fusion Shift’s story engine listens to structured game data — battles, diplomacy, espionage — and responds with:

- 📝 **Auto-generated narrative**: Rich text describing what just happened (and why it matters)
- 🖼 **Image + video prompts**: For use with tools like Midjourney, DALL·E, Sora, or Runway
- 🎭 **Character and faction arcs**: Expanding over time, driven by real gameplay
- 🗞 **News feeds**: Personal, factional, and galactic-level perspectives

---

## 🧠 Core Modules

| Folder | Purpose |
|--------|---------|
| `engine/` | Core story engine logic (event processing, narrative generation) |
| `prototypes/` | Experimental tools (e.g. media prompt builders, tone mappers) |
| `docs/` | System design, architecture, and creative notes |
| `tests/` | Unit and functional test scripts |
| `assets/` | Optional folder for portraits, icons, example exports |

---

## 📄 Key Docs

- `docs/architecture/FS_StoryEngine_Architecture_v1.0.md`  
  🔧 System overview: layers, pipelines, inputs and outputs

- `docs/designNotes/FS_DesignCompanion_ReliabilityAndFlow_v0.1.md`  
  🧭 Narrative flow: event handling, async design, story queue principles

- `docs/designNotes/FS_VisualNarrative_Hooks_v0.1.md`  
  🎨 Visual storytelling: prompt scaffolding for images + videos

---

## 🔍 Example Usage

```bash
python prototypes/mediaPromptBuilder.py
