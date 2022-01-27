nations = {
    "Aldercrown Empire": {
        "population" : 75000
    },
    "Beleriand": {
        "population" : 50000
    },
    "Principality of the Palus Peoples": {
        "population" : 30000
    },
    "Shadesburry Initiative": {
        "population" : 25000
    },
    "Magmus Centerhold": {
        "population" : 60000
    },
    "Qualnis": {
        "population" : 50000
    },
    "Verdain": {
        "population" : 30000
    },
    "Chilliwld Peaks": {
        "population" : 10000
    },
    "Kordinia": {
        "population" : 20000
    }
}

def get_nations():
    return list(nations.keys())

def get_nation_populations():
    populations = []
    for nation in nations.values():
        populations.append(nation["population"])
    return populations