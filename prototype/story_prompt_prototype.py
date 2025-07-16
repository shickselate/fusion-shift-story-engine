# story_prompt_prototype.py
# Fusion Shift – Prototype for story generation prompt

import random
from datetime import datetime

# -----------------------------
# Step 1: Mock Game Data
# -----------------------------

factions = {
    "Solaris Union": {
        "leader": "Empress Aela Dren",
        "general": "Rika Kael",
        "traits": ["honour-bound", "strategic"],
        "fleet": {"Destroyers": 40, "Fighters": 200}
    },
    "House Myrrk": {
        "leader": "Lord Varn Tel",
        "general": "Korz Malen",
        "traits": ["aggressive", "technocratic"],
        "fleet": {"Corvettes": 300, "Cruisers": 5}
    }
}

event = {
    "type": "battle",
    "location": "Zeta-3",
    "timestamp": datetime.utcnow().isoformat(),
    "participants": ["Solaris Union", "House Myrrk"],
    "outcome": random.choice(["Solaris Victory", "Myrrk Victory", "Stalemate"]),
    "rumours": random.choice([
        "sabotage suspected within the Myrrk ranks",
        "Solaris weapons malfunctioned mysteriously",
        "both sides were ambushed by a third fleet"
    ])
}

# -----------------------------
# Step 2: Prompt Template
# -----------------------------

def generate_prompt(event, factions):
    outcome = event["outcome"]
    faction1, faction2 = event["participants"]
    general1 = factions[faction1]["general"]
    general2 = factions[faction2]["general"]
    location = event["location"]
    rumour = event["rumours"]

    return f"""
Write a galactic news report about a space battle in the {location} system.
The {faction1} was led by General {general1}, and the {faction2} by General {general2}.
The outcome was: {outcome}. Include a sense of drama and mention that: {rumour}.
Keep the tone serious, like a wartime dispatch from a respected interstellar journalist.
"""

# -----------------------------
# Step 3: Output Prompt
# -----------------------------

prompt = generate_prompt(event, factions)
print("=== STORY PROMPT ===")
print(prompt)
