import random

# Preset character pools
NAMES = [
    "Kael Vox", "Rika Kael", "Thorne Malen", "Aurea Syle", "Vel Marrek",
    "Lyra Dax", "Juno Nyre", "Corven Ash", "Zera Thal", "Elion Vey"
]

ROLES = [
    "Admiral", "Spymaster", "High Priestess", "Industrial Magnate",
    "Emperor", "Envoy", "Warlord", "Archivist", "Diplomat", "Fleet Commander"
]

FACTIONS = [
    "House Myrrk", "Solaris Union", "Cult of Mirrors", "Tyrian Pact", "Zarim Alliance"
]

TRAITS = [
    "ruthless", "visionary", "calculating", "charismatic", "impulsive",
    "loyal", "cunning", "honour-bound", "mysterious", "ambitious"
]

VISUAL_STYLES = {
    "dynastic_art": "formal, ornate, regal lighting, portrait style",
    "signal_drift": "glitchy, surreal, fragmented facial geometry",
    "techno_realist": "military aesthetic, sharp lines, cinematic realism"
}

def generate_character():
    name = random.choice(NAMES)
    role = random.choice(ROLES)
    faction = random.choice(FACTIONS)
    selected_traits = random.sample(TRAITS, 3)
    visual_style_key = random.choice(list(VISUAL_STYLES.keys()))
    portrait_prompt = (
        f"{role}, {', '.join(selected_traits)}, "
        f"{VISUAL_STYLES[visual_style_key]}"
    )

    return {
        "name": name,
        "role": role,
        "faction": faction,
        "traits": selected_traits,
        "visual_style": visual_style_key,
        "portrait_prompt": portrait_prompt
    }

# Demo
if __name__ == "__main__":
    character = generate_character()
    for key, value in character.items():
        print(f"{key}: {value}")
