# Fusion Shift – AI Story Engine Architecture (v1.0)

> This document describes the system architecture for the Fusion Shift AI story engine — a modular storytelling pipeline that transforms gameplay data into character-rich, emotionally resonant narrative output.

---

## 🧾 1. Input Layer – Game Data Ingestion

### Purpose
Standardise structured input from the Fusion Shift game engine (or mock data generator) for downstream processing.

### Key Inputs
- **Events** – e.g. `battle`, `espionage`, `marriage`, `discovery`, `expansion`, `catastrophe`
- **Characters** – name, role, traits, relationships, status (alive/lost/legendary)
- **Factions** – name, ethos, assets, political status

### Example Event
```json
{
  "event_type": "battle",
  "location": "Zeta-3",
  "timestamp": "2025-07-16T12:00:00Z",
  "participants": ["Solaris Union", "House Myrrk"],
  "key_characters": ["Rika Kael", "Korz Malen"],
  "outcome": "stalemate",
  "metadata": {
    "ship_stats": {
      "Solaris Union": {"Fighters": 200, "Destroyers": 40},
      "House Myrrk": {"Corvettes": 300, "Cruisers": 5}
    },
    "rumours": ["sabotage suspected"]
  }
}
```

---

## 🧠 2. Narrative Logic Layer

### Purpose
Select events for storytelling, determine appropriate perspective, and track narrative threads.

### Components
- **Event Prioritiser** – scores events by drama, novelty, and impact
- **Perspective Selector** – chooses story format: news report, diary entry, diplomatic memo, etc.
- **Thread Tracker** – stores open story arcs (e.g. a spy mission), character histories, unresolved tensions

---

## ✍️ 3. Story Construction Layer

### Purpose
Turn structured data into compelling narrative using prompt engineering and LLMs.

### Pipeline
1. **Template Selector** – e.g. `"battle_report"`, `"spy_dossier"`, `"wedding_announcement"`
2. **Prompt Generator** – injects names, tone, stats, and memory into a prompt string
3. **LLM Call** – runs through GPT, Claude, or local model
4. **Post-processing** – tag entities, check tone, archive or thread output

---

## 📡 4. Publishing Layer

### Purpose
Deliver generated stories to players through multiple narrative surfaces.

### Output Formats
- **Galactic Newsfeed** – the main stream of public events
- **Character Chronicle** – focused story history for key individuals
- **Faction Digest** – summarised political and military updates
- **Optional Extensions** – alerts, visual media prompts, public archives

---

## 🔁 5. Reliability & Flow Enhancements

### Error Handling
- Fall back to structured summary if generation fails
- Remove non-critical elements (quotes, subplots) if prompt fails validation

### Async Story Queue
- Queue-based event processor
- Each event has `urgency`, `expiry`, and `narrative weight`
- Pacing system ensures tone balance and readable delivery cadence

### Thread + Character Memory
- Maintain per-character logs of:
  - Events participated in
  - Relationships formed/broken
  - Traits and evolution
- Track open threads (e.g. "spy mission unresolved", "treaty in negotiation")

---

## 🎭 6. Event Types & Narrative Modes

| Event Type       | Narrative Modes                          |
|------------------|------------------------------------------|
| `battle`         | News dispatch, admiral's log, heroic saga |
| `espionage`      | Dossier, intercepted memo, rumour         |
| `marriage`       | Treaty preamble, wedding speech, tabloid  |
| `expansion`      | Colonial charter, settler's diary         |
| `assassination`  | Breaking alert, survivor account, theory  |
| `coronation`     | Public speech, mythic prophecy            |
| `discovery`      | Research bulletin, explorer log           |
| `catastrophe`    | Emergency transmission, journal fragment  |

---

## 🚀 7. Deployment Plan

| Phase        | Description                                      |
|--------------|--------------------------------------------------|
| Prototype    | Local mock data, generate prompt + story output |
| Connected    | Pull from live game logs                        |
| Interactive  | Player-facing interface, tone preferences       |

---

## 🧠 8. End Goal

Create a storytelling engine that makes the galaxy feel alive — weaving game state, character arcs, and emergent conflict into a tapestry of personal, playable lore.

This system should be:
- Modular ✅  
- Extensible ✅  
- Emotionally engaging ✅  
- Artistically generative ✅
