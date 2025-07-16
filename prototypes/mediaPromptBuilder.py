import random

# Example style presets
STYLE_PRESETS = {
    "mythic_grunge": ["epic", "textured", "golden haze", "mythic scale"],
    "techno_realist": ["clean", "metallic", "cinematic lighting", "industrial"],
    "signal_drift": ["glitch", "VHS lines", "retro-futurist", "low fidelity"],
    "dynastic_art": ["iconic", "ornate", "formal", "stylised portrait"]
}

# Main function
def generate_media_prompt(event):
    event_type = event.get("event_type")
    location = event.get("location", "unknown star system")
    characters = ", ".join(event.get("key_characters", [])) or "Unnamed figures"
    factions = ", ".join(event.get("participants", [])) or "unknown factions"
    tone = event.get("tone", "dramatic")

    if event_type == "battle":
        base_prompt = f"A space battle scene near {location}, showing fleets of {factions}, with {characters} in command"
    elif event_type == "espionage":
        base_prompt = f"A shadowy spy meeting in {location}, featuring {characters}, with holographic maps and secrecy"
    elif event_type == "marriage":
        base_prompt = f"An interstellar royal wedding between houses at {location}, elegant attire, banners, and starlit ceremony"
    elif event_type == "discovery":
        base_prompt = f"A scientific outpost discovering alien ruins on a rocky world in {location}, awe and mystery"
    else:
        base_prompt = f"A galactic event at {location}, with presence of {characters} and unknown implications"

    # Choose a style
    style_key = random.choice(list(STYLE_PRESETS.keys()))
    style_tags = STYLE_PRESETS[style_key]

    return {
        "image_prompt": base_prompt,
        "style_tags": style_tags,
        "visual_style": style_key,
        "tone": tone
    }

# Example usage
if __name__ == "__main__":
    mock_event = {
        "event_type": "battle",
        "location": "Zeta-3",
        "key_characters": ["Rika Kael", "Korz Malen"],
        "participants": ["Solaris Union", "House Myrrk"],
        "tone": "tense"
    }

    prompt_data = generate_media_prompt(mock_event)
    for k, v in prompt_data.items():
        print(f"{k}: {v}")
