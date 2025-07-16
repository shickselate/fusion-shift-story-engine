# Fusion Shift – Visual Narrative Hooks (v0.1)

> This document outlines how the Fusion Shift story engine can support rich visual storytelling using generative image and video tools.

---

## 🖼️ 1. Visual Layer Overview

The visual layer is not required for basic storytelling, but can significantly enhance:
- Emotional connection
- Social sharing
- Worldbuilding immersion

Visuals are imagined as:
- **In-line media**: portraits, ships, scenes embedded in story feeds
- **Standalone formats**: cinematic shorts, recruitment posters, breaking news clips

---

## 🔗 2. Image Generation Hooks

The story engine can emit **tagged prompts** for each story, e.g.:

```json
{
  "image_prompt": "a damaged fleet of Solaris Union destroyers limping home through a red nebula",
  "tags": ["battle aftermath", "space", "Solaris Union", "red colour grade"]
}
```

### Prompt Sources
- Character/faction descriptors (from character ledger)
- Event context (location, weather, emotional tone)
- Narrative mode (e.g. "epic", "gritty", "romantic")

### Output Format Options
- 📷 `image_url` – (if automatically generated)
- 📝 `image_prompt.md` – save prompt text for later generation
- 🔖 `image_tags` – optional metadata (aesthetic style, media format, mood)

---

## 🎬 3. Video / Cinematic Hooks

For high-drama events (coronations, invasions, catastrophes), the engine could generate:
- A **scene description**: structured as a script outline or trailer-style prose
- A **Sora-style prompt**: suitable for tools like Runway or Pika

### Example
```
INT. COMMAND BRIDGE – NIGHT

Admiral Rika Kael watches the starfield as warning lights blink red. Behind her, the crew braces.

— Sora Prompt —
“a cinematic sci-fi scene on the bridge of a starship, emergency lighting, dramatic tension, admiral watching stars, digital rain overlay”
```

---

## 🎨 4. Styles & Aesthetics

| Style Name      | Inspiration                | Mood             |
|------------------|----------------------------|------------------|
| `Mythic Grunge` | Dune, Moebius              | Epic, textured   |
| `Techno Realist`| Foundation, Expanse        | Clean, industrial|
| `Signal Drift`  | VHS, glitchy, lo-fi        | Haunting, retro  |
| `Dynastic Art`  | Mughal, Byzantine, Persian | Formal, iconic   |

The system may eventually let factions or players define their visual style preference for consistent worldbuilding.

---

## 🛠️ 5. Implementation Options

### Phase 1 – Prompt Only
- Output markdown-style prompts alongside stories
- Enable later generation via Midjourney, DALL·E, etc.

### Phase 2 – Batch Generation
- Script tool generates batches of images (via API)
- Cache and tag image links to embed in player UI

### Phase 3 – Player-Controlled
- Players request portraits or scenes via interface
- Possibly steer tone via a few style presets

---

## 🚧 6. Open Questions

- Should every story have an image, or only major ones?
- Should characters get permanent portraits, or evolve over time?
- Will players want to create *their own* visuals? If so, how do we combine those with generated ones?

---

## 🧠 Design Philosophy

Visuals should *serve the story*, not distract from it. They should:
- Reinforce mood  
- Clarify world identity  
- Surprise and delight  

Done well, a single portrait or visual moment can anchor a player’s whole experience of a faction or event.

---

