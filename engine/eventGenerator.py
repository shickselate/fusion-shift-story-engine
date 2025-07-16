import random
from characterBuilder import generate_character

# Event types and settings
EVENT_TYPES = ["battle", "diplomacy", "espionage", "marriage"]

LOCATIONS = [
    "Icarus Drift", "Virel System", "Ashen Belt", "Zarim Core", "The Twin Moons of Quarn",
    "Junction Delta", "Cryos Reach", "Deep Station Nym", "The Veiled Expanse"]

MAGNITUDE = ["minor", "moderate", "major", "critical"]


EVENT_OUTCOMES = {
    "battle": ["victory", "defeat", "stalemate"],
    "diplomacy": ["treaty signed", "talks collapsed", "agreement delayed"],
    "espionage": ["intel recovered", "operative captured", "operation aborted"],
    "marriage": ["alliance sealed", "ceremony interrupted", "match withdrawn"]
}


def generate_event():
    event_type = random.choice(EVENT_TYPES)
    location = random.choice(LOCATIONS)
    magnitude = random.choice(MAGNITUDE)
    outcome = random.choice(EVENT_OUTCOMES.get(event_type, ["event unresolved"]))
    actor = generate_character()
    opposing_faction = random.choice([
        f for f in ["House Myrrk", "Solaris Union", "Cult of Mirrors", "Tyrian Pact", "Zarim Alliance"]
        if f != actor["faction"]
    ])

    event = {
        "type": event_type,
        "location": location,
        "magnitude": magnitude,
        "timestamp": "232.94.14.08",  # placeholder format
        "main_actor": actor,
        "involved_factions": [actor["faction"], opposing_faction,
        "outcome": outcome
    }

    return event

# Example usage
if __name__ == "__main__":
    event = generate_event()
    print("🎲 Event Generated:")
    for key, value in event.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for subkey, subval in value.items():
                print(f"  {subkey}: {subval}")
        else:
            print(f"{key}: {value}")
