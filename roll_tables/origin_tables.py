from random import choices, randrange
import data.nations as ng

##Concentration is 0-1 based on how the race has spread from its
## main hubs
race_concentrations = {
    "Dwarf": {
        "concentration": 0.6,
        "hubs": ["Aldercrown Empire", "Shadesburry Initiative", "Beleriand"],
        "hubs_w": [70, 20, 10]
    },
    "Elf": {
        "concentration": 0.7,
        "hubs": ["Aldercrown Empire", "Beleriand"],
        "hubs_w": [40, 60]
    },
    "Gnome": {
        "concentration": 0.8,
        "hubs": ["Shadesburry Initiative"],
        "hubs_w": [100]
    },
    "Half-Elf": {
        "concentration": 0.4,
        "hubs": ["Beleriand", "Aldercrown Empire"],
        "hubs_w": [60, 40]
    },
    "Halfling": {
        "concentration": 0.4,
        "hubs": ["Verdain", "Kordinia"],
        "hubs_w": [50, 50]
    },
    "Human": {
        "concentration": 0.2,
        "hubs": ["Qualnis"],
        "hubs_w": [50]
    },
    "Triton": {
        "concentration": 0.9,
        "hubs": ["Glasscliff Garisons", "Whyndiem"],
        "hubs_w": [20, 80]
    },
    "Dragonborn": {
        "concentration": 0.7,
        "hubs": ["Draconia", "Magmus Centerhold"],
        "hubs_w": [85, 15]
    },
    "Half-Orc": {
        "concentration": 0.7,
        "hubs": ["Magmus Centerhold", "Verdain", "Chillwild Peaks"],
        "hubs_w": [70, 10, 20]
    },
    "Tiefling": {
        "concentration": 0,
        "hubs": [],
        "hubs_w": []
    },
    "Firbolg": {
        "concentration": 0.8,
        "hubs": ["Verdain", "Shadesburry Initiative", "Principality of the Palus Peoples"],
        "hubs_w": [90, 5, 5]
    },
    "Kenku": {
        "concentration": 0.8,
        "hubs": ["Black Rock", "Shadesburry Initiative"],
        "hubs_w": [90, 10]
    },
    "Aasimar": {
        "concentration": 0,
        "hubs": [],
        "hubs_w": []
    },
    "Genasi": {
        "concentration": 0.4,
        "hubs": ["Magmus Centerhold", "Verdain"],
        "hubs_w": [50, 50]
    },
    "Goliath": {
        "concentration": 0.7,
        "hubs": ["Chillwild Peaks"],
        "hubs_w": [100]
    },
    "Warforged": {
        "concentration": 0.98,
        "hubs": ["Shadesburry Initiative", "Qualnis"],
        "hubs_w": [50, 50]
    }
}

def process_percentage(percent: float) -> bool:
    return randrange(100) < percent * 100

def get_origin(race=None):
    if not race:
        return get_origin_general()
    else:
        race_origin_data = race_concentrations[race]
        within_core = process_percentage(race_origin_data["concentration"])
        if within_core:
            return choices(race_origin_data["hubs"], race_origin_data["hubs_w"])[0]

    return get_origin_general()

def get_origin_general():
    nations = ng.get_nations()
    weights = ng.get_mysten_wieghts()
    return choices(nations, weights)[0]