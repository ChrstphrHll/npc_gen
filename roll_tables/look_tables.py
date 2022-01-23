from .Table import Table, MultiRoll
import random

hair_uncommon = Table(
    ("blue", 4),
    ("green", 4),
    ("pink", 4),
    ("violet", 4),
    ("turquoise", 2)
)

hair_color = Table(
    ("black", 10),
    ("grey", 10),
    ("platinum", 10),
    ("white", 10),
    ("dirty blonde", 10),
    ("blonde", 10),
    ("lighter blonde", 10),
    ("dark red", 10),
    ("red", 10),
    ("strawberry blond", 10),
    ("brunette", 20),
    ("auburn", 20),
    (hair_uncommon, 10)
)

short_hair = Table(
    ("parted to the left", 5),
    ("parted to the right", 5),
    (MultiRoll("kept back by a {} headband", hair_uncommon), 5),
    ("a tousled bed head", 5),
    ("geled back", 5),
    ("a buzz cut", 1),
)

medium_hair = Table(
    ("done up in a top knot", 5),
    (MultiRoll("braided with {} ribbon (med)", hair_uncommon), 5),
    ("put back in a short pony tail", 5),
    ("loose around the shoulders", 10),
    ("parted to the side, slightly obscuring an eye", 5),
    ("pulled to the side and buzzed on the right", 2),
    ("pulled to the side and buzzed on the left", 2),
)

long_hair = Table(
    ("put up in a large bun", 5),
    (MultiRoll("braided with {} ribbon (long)", hair_uncommon), 5),
    ("put back in a long pony tail", 5),
    ("hanging down to their back", 5),
    ("hanging down to their legs", 2),    
)

hair_length = Table(
    (short_hair, 20),
    (medium_hair, 20),
    (long_hair, 20)
)

hair_texture = Table(
    ("straight", [1,30]),
    ("wavy", [31,60]),
    ("curly", [61,90]),
    ("frizzy", 5)
)

hair = MultiRoll(
    "{} {} hair that's {}",
    hair_texture,
    hair_color,
    hair_length
)

metalic_table = Table(
    ("gold", 1),
    ("silver", 1),
    ("bronze", 1),
    ("brass", 1),
    ("copper", 1)
)
gemstones = Table(
    ("ruby", 1),
    ("topaz", 1),
    ("sapphire", 1),
    ("garnet", 1),
    ("amethyst", 1),
    ("quartz", 1),
    ("diamond", 1),
    ("onyx", 1),
    ("emerald", 1)
)

warforged_inset = MultiRoll(
    "smooth {} guilded with {}",
    metalic_table,
    Table((metalic_table, 5), (gemstones, 1))
)

numbers = Table(
    ("2", 1),
    ("3", 1),
    ("4", 1),
    ("5", 1),
    ("many", 1)
)

horn_type = Table(
    ("curled", 5),
    ("jagged", 3),
    ("straight", 5),
    ("hooked", 2),
    ("barbed", 2),
    ("twisted", 1),
)

dragonborn_hair = Table(
    (MultiRoll("{} {} horns", numbers, horn_type), 1),
    ("frills", 1),
    ("short spines", 1),
    ("long spines", 1)
)

kenku_hair = Table(
    ("sleek", 1),
    ("ruffled", 1),
    ("speckled", 1),
    ("striped", 1),
)

def get_hair(race):
    if race == "Warforged":
        return warforged_inset.roll()
    elif race == "Dragonborn":
        return dragonborn_hair.roll()
    elif race == "Kenku":
        return kenku_hair.roll()
    return hair.roll()

eye_colors = [
    "Amber",
    "Brown",
    "Hazel",
    'Green',
    "Blue",
    "Gray",
    "Pale Brown",
    "Pale Blue",
    "Pale Green",
    "Pale Gray"
]

rare_eye_colors = [
    "Yellow",
    "Aqua",
    "Red",
    "Purple",
    "Deep Blue",
    "Violet Red",
    "Orange",
    "Spring Green",
    "Sea Green",
    "Emerald Green"
]

def get_eyes(race):
    colorful_races = [
        "Tiefling",
        "Genasi",
        "Triton",
        "Dragonborn",
        "Warforged"
    ]

    selection_list = eye_colors.copy()

    if race in colorful_races:
        selection_list += rare_eye_colors
    
    return random.choice(selection_list)


def get_skin(race):
    selection_list = []
    if race == "Dragonborn":
        selection_list = ["gold", "silver", "bronze", "brass", "copper", "red", "blue", "black", "white", "green"]
    elif race == "Warforged":
        selection_list = ["gold", "silver", "bronze", "brass", "copper"]
    elif race == "Genasi":
        selection_list = ["earth", "fire", "water", "air"]
    elif race == "Firbolg":
        selection_list = [
            "Pale Brown",
            "Pale Blue",
            "Pale Green",
            "Pale Gray"
        ]
    elif race == "Half-Orc":
        selection_list = [
            "Green Blue",
            "Deep Green",
            "Pale Green",
            "Pale Gray"
        ]
    elif race == "Kenku":
        selection_list = [
            "Black",
            "Dark Blue",
            "Dark Purple",
            "Red",
            "Brown"
        ]
    elif race == "Triton":
        selection_list = [
            "Olive",
            "Aqua",
            "Pale Blue",
            "Pale Green",
            "Pale Gray",
            "Deep Blue",
            "Spring Green",
            "Sea Green",
            "Emerald Green"
        ]
    elif race == "Tiefling":
        selection_list = [
            "Red",
            "Orange",
            "Yellow",
            "Green",
            "Blue",
            "Purple",
            "Pale Yellow",
            "Dark Red",
            "Red-Orange",
            "Light Red",
            "Amber",
            "Olive",
            "Aqua",
            "Pale Brown",
            "Pale Blue",
            "Pale Green",
            "Pale Gray",
            "Deep Blue",
            "Violet Red",
            "Spring Green",
            "Sea Green",
            "Emerald Green",
        ]
    else:
        selection_list = [
            "Pale",
            "Fair",
            "Light",
            "Light Tan",
            "Tan",
            "Dark Tan",
            "Brown",
            "Dark Brown"
        ]
    
    return random.choice(selection_list)