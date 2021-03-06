import random

common = [
    "Dwarf",
    "Elf",
    "Gnome",
    "Half-Elf",
    "Halfling",
    "Human"
]

uncommon = [
    "Triton",
    "Dragonborn",
    "Half-Orc",
    "Tiefling",
    "Firbolg",
]

rare  = [
    "Kenku",
    "Aasimar",
    "Genasi",
    "Goliath",
    "Warforged"
]

def get_race():
    race_list = random.choices([common, uncommon, rare], [50, 35, 10])[0]
    race = random.choice(race_list)
    return race