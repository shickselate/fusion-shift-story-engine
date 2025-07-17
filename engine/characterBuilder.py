# characterBuilder.py

import random

# Shared faction list (used in both character and event generation)
FACTIONS = [
    "Tyrian Pact", "Zarim Alliance", "House Myrrk", "Solaris Union", "Cult of Mirrors",
    "Virel Enclave", "The Obsidian Fold", "Nomads of Icarus"
]

ROLES = [
    "Warlord", "High Priestess", "Admiral", "Scientist", "Diplomat", "Spy", "Explorer",
    "Heir", "Governor", "Archivist", "Engineer", "Fleet Commander"
]

NAMES = [
    "Kael", "Aurea", "Vel", "Thorne", "Nyra", "Rika", "Corven", "Syle", "Jalen", "Vexa",
    "Doran", "Zirra", "Ash", "Lira", "Varek", "Myrr", "Zhale", "Erix", "Talon", "Ilyr"
]

TITLES = [
    "of the Crimson Star", "from Nexus Prime", "of Quarn's Moon", "of the Forgotten Ring",
    "from the Ion Reach", "of Deep Station Nym", "of the Silent Spire", "from Helix Verge"
]

TRAITS = [
    "ambitious", "calculating", "honour-bound", "ruthless", "visionary",
    "secretive", "charismatic", "disciplined", "impulsive", "stoic"
]

# Function to generate a character
def generate_character():
    name = f"{random.choice(NAMES)} {random.choice(NAMES)}"
    role = random.choice(ROLES)
    faction = random.choice(FACTIONS)
    title = random.choice(TITLES)

    return {
        "name": name,
        "role": role,
        "faction": faction,
        "title": title
        "traits": traits
    }

# Optional: test output
if __name__ == "__main__":
    print(generate_character())
