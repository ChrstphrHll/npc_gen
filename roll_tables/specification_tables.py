import random

specs = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rouge",
    "Sorcerer",
    "Wizard"
]

tracks = [
    "Assault",
    "Diplomacy",
    "Exploration",
    "Protection"
]

def get_track():
    return random.choice(tracks)

def get_spec():
    return random.choice(specs)