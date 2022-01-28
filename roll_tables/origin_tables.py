from random import choices
import data.nations as ng

##Concentration is 0-1 based on how the race has spread from its
## main hubs
race_concentrations = {
    "Dwarf": {
        "concentration": 0.5,
        "hubs": ["Aldercrown Empire", ],
        "hubs_w": []
    },
    "Elf": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Gnome": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Half-Elf": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Halfling": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Human": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Triton": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Dragonborn": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Half-Orc": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Tiefling": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Firbolg": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Kenku": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Aasimar": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Genasi": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Goliath": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    },
    "Warforged": {
        "concentration": 0.7,
        "hubs": [],
        "hubs_w": []
    }
}


def get_origin(race=-1):
    #TODO: update to include race
    if race:
        nations = ng.get_nations()
        weights = ng.get_nation_populations()
        return choices(nations, weights)[0]

    return get_origin_general()

def get_origin_general():
    nations = ng.get_nations()
    weights = ng.get_nation_populations()
    return choices(nations, weights)[0]