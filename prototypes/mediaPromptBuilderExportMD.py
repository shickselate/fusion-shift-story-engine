import random
import os
from datetime import datetime

STYLE_PRESETS = {
    "mythic_grunge": ["epic", "textured", "golden haze", "mythic scale"],
    "techno_realist": ["clean", "metallic", "cinematic lighting", "industrial"],
    "signal_drift": ["glitch", "VHS lines", "retro-futurist", "low fidelity"],
    "dynastic_art": ["iconic", "ornate", "formal", "stylised portrait"]
}

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

    style_key = random.choice(list(STYLE_PRESETS.keys()))
    style_tags = STYLE_PRESETS[style_key]

    return {
        "image_prompt": base_prompt,
        "style_tags": style_tags,
        "visual_style": style_key,
        "tone": tone
    }

def export_prompt_to_markdown(prompt_data, output_dir="exports"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/prompt_{timestamp}.md"

    with open(filename, "w") as f:
        f.write("# 🎨 Generated Media Prompt\n\n")
        f.write(f"**Visual Prompt**: {prompt_data['image_prompt']}\n\n")
        f.write(f"**Style Tags**: {', '.join(prompt_data['style_tags'])}\n\n")
        f.write(f"**Visual Style**: `{prompt_data['visual_style']}`\n\n")
        f.write(f"**Tone**: *{prompt_data['tone']}*\n")

    print(f"Prompt exported to: {filename}")

# Demo
if __name__ == "__main__":
    mock_event = {
        "event_type": "espionage",
        "location": "Zarim's Edge",
        "key_characters": ["Kael Vox", "The Listening Blade"],
        "participants": ["House Tyval", "Cult of Mirrors"],
        "tone": "mysterious"
    }

    prompt = generate_media_prompt(mock_event)
    for k, v in prompt.items():
        print(f"{k}: {v}")
    export_prompt_to_markdown(prompt)
