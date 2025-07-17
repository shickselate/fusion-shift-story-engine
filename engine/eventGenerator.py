import random
from characterBuilder import generate_character, FACTIONS

# Event types and settings
EVENT_TYPES = ["battle", "diplomacy", "espionage", "marriage", "exploration", "ceremony", "disaster"]

LOCATIONS = [
    "Icarus Drift", "Virel System", "Ashen Belt", "Zarim Core", "The Twin Moons of Quarn",
    "Junction Delta", "Cryos Reach", "Deep Station Nym", "The Veiled Expanse",
    "Nexus Prime", "Kepler System", "Drift Core", "Helix Verge", "Ion Reach"
]

ENVIRONMENT_TYPES = [
    "ocean world", "asteroid field", "orbital station", "gas giant moon", "crystalline world", "expanse", "plasma field"
]

MAGNITUDE = ["minor", "moderate", "major", "critical"]

INSTABILITY_LEVELS = ["golden age", "stable", "tense", "unrest", "on brink of revolt"]

STRATEGIC_IMPORTANCE = [
    "military stronghold", "trade nexus", "research outpost", "ancient ruins", "diplomatic hub"
]

COMPLICATIONS = ["solar flare", "traitor revealed", "data leak", "supply failure", "psychic interference"]

TRIGGERS = ["border violation", "failed negotiation", "ancient signal received", "leadership change", "rival provocation"]

OUTCOME = {
    "battle": ["victory", "defeat", "stalemate", "retreat"],
    "diplomacy": ["treaty signed", "agreement delayed", "talks collapsed"],
    "espionage": ["data stolen", "spy captured", "operation aborted"],
    "exploration": ["new world charted", "anomaly encountered", "team lost"],
    "ceremony": ["alliance sealed", "heir crowned", "ritual disrupted"],
    "disaster": ["evacuation ordered", "colony lost", "containment successful"]
}

def generate_event():
    event_type = random.choice(EVENT_TYPES)
    location = random.choice(LOCATIONS)
    environment = random.choice(ENVIRONMENT_TYPES)
    strategic_value = random.choice(STRATEGIC_IMPORTANCE)
    instability = random.choice(INSTABILITY_LEVELS)
    magnitude = random.choice(MAGNITUDE)
    outcome = random.choice(OUTCOME.get(event_type, ["event unresolved"]))
    actor = generate_character()
    opposing_faction = random.choice([f for f in FACTIONS if f != actor["faction"]])
    trigger = random.choice(TRIGGERS)
    complication = random.choice(COMPLICATIONS)

    return {
        "type": event_type,
        "location": location,
        "environment": environment,
        "strategic_importance": strategic_value,
        "instability": instability,
        "magnitude": magnitude,
        "timestamp": "232.94.14.08",
        "main_actor": actor,
        "involved_factions": [actor["faction"], opposing_faction],
        "trigger": trigger,
        "complication": complication,
        "outcome": outcome
    }

if __name__ == "__main__":
    from pprint import pprint
    pprint(generate_event())
