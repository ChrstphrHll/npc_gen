nations = {
    "Aldercrown Empire": {
        "mysten_w": 24,
        "population": 75000
    },
    "Beleriand": {
        "mysten_w": 19,
        "population": 50000
    },
    "Principality of the Palus Peoples": {
        "mysten_w": 14,
        "population": 30000
    },
    "Shadesburry Initiative": {
        "mysten_w": 10,
        "population": 25000
    },
    "Magmus Centerhold": {
        "mysten_w": 9,
        "population": 60000
    },
    "Qualnis": {
        "mysten_w": 4,
        "population": 50000
    },
    "Verdain": {
        "mysten_w": 7,
        "population": 30000
    },
    "Chillwild Peaks": {
        "mysten_w": 4,
        "population": 10000
    },
    "Kordinia": {
        "mysten_w": 6,
        "population": 20000
    },
    "Glasscliff Garrisons": {
        "mysten_w": 0.5,
        "population": 5000
    },
    "Whyndiem": {
        "mysten_w": 2.5,
        "population": 25000
    },    
    "Floating Island": {
        "mysten_w": 8,
        "population": 10000
    },
}

def get_nations():
    return list(nations.keys())

def get_nation_populations():
    populations = []
    for nation in nations.values():
        populations.append(nation["population"])
    return populations

def get_mysten_wieghts():
    m_wieghts = []
    for nation in nations.values():
        m_wieghts.append(nation["mysten_w"] * nation["population"])
    return m_wieghts