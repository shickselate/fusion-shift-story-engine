import random

# Basic tone modifiers
TONE_TEMPLATES = {
    "neutral": "{event_intro} {character_name} of the {faction} acted with {trait_phrase}.",
    "cinematic": "As the stars blazed above, {character_name}, a {role} of {faction}, {event_action}.",
    "poetic": "Beneath twin moons, {character_name} moved like fate itself — {event_action}, {trait_phrase}.",
    "military": "Commander {character_name} ({role}, {faction}) initiated {event_action}. Outcome: pending.",
}

# A small event action bank for now
EVENT_ACTIONS = {
    "battle": [
        "launched a full-scale assault on the outer rim stronghold",
        "led a last-ditch defence against overwhelming forces",
        "commandeered a rogue fleet for an unauthorised strike"
    ],
    "diplomacy": [
        "brokered a fragile truce after weeks of silence",
        "met in secret to forge a shadow alliance",
        "publicly denounced the actions of a rival house"
    ],
    "espionage": [
        "dispatched covert operatives behind enemy lines",
        "intercepted encrypted transmissions revealing enemy intent",
        "uncovered a spy ring operating within the core worlds"
    ],
    "marriage": [
        "announced a union between rival dynasties",
        "hosted a ceremonial binding aboard the throne cruiser",
        "sealed a political pact with an ancient vow"
    ]
}

def format_narrative(character, event_type="battle", tone="neutral", outcome=None):
    template = TONE_TEMPLATES.get(tone, TONE_TEMPLATES["neutral"])
    action = random.choice(EVENT_ACTIONS.get(event_type, ["took a mysterious action"]))
    trait_phrase = ", ".join(character["traits"])

    base_story = template.format(
        event_intro=f"A new {event_type} event has occurred.",
        event_action=action,
        character_name=character["name"],
        role=character["role"],
        faction=character["faction"],
        trait_phrase=trait_phrase
    )

    if outcome:
        return f"{base_story} Outcome: {outcome}."
    else:
        return base_story


# Example usage
if __name__ == "__main__":
    example_character = {
        "name": "Vel Marrek",
        "role": "Admiral",
        "faction": "Tyrian Pact",
        "traits": ["calculating", "ruthless", "charismatic"]
    }

    print(format_narrative(example_character, event_type="battle", tone="cinematic"))
