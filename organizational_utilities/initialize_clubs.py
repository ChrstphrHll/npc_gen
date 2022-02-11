import organizational_utilities.validators
import organizational_utilities.assign_organizations

clubs = {
    "Half Notes": {
        "validators": [],
        "size": 15,
    },
    "Cracked Bell": {
        "validators": [],
        "size": 45,
    },
    "LOAM": {
        "validators": [],
        "size": 21,
    },
    "Wayfinders": {
        "validators": [],
        "size": 60,
    },
    "Splinters": {
        "validators": [],
        "size": 53,
    },
    "Aquaculture": {
        "validators": [],
        "size": 12,
    },
    "Grason's Claw": {
        "validators": [],
        "size": 24,
    },
    "Inner Circle Judges": {
        "validators": [],
        "size": 13,
    },
    "Treskal Silkball": {
        "validators": [],
        "size": 15,
    },
    "Alderden Silkball": {
        "validators": [],
        "size": 15,
    },
    "Jettenia Silkball": {
        "validators": [],
        "size": 15,
    },
    "Burk Silkball": {
        "validators": [],
        "size": 15,
    },
    "Trenchers": {
        "validators": [],
        "size": 25,
    },
    "Dragon Chess Club": {
        "validators": [],
        "size": 7,
    },
    "Mysten Students for a Better Revendale": {
        "validators": [],
        "size": 22,
    },
    "Ashari Cultural Group": {
        "validators": [],
        "size": 20,
    },
    "Forgetenders": {
        "validators": [],
        "size": 34,
    },
    "Threaded Needle": {
        "validators": [],
        "size": 34,
    },
    "Pious Fellowship": {
        "validators": [],
        "size": 33,
    },
    "Ruin Runners": {
        "validators": [],
        "size": 40,
    },
    "Hand of Order": {
        "validators": [],
        "size": 38,
    },
    "Spellweavers": {
        "validators": [],
        "size": 28,
    },
    "Golemic Consortium": {
        "validators": [],
        "size": 14,
    },
    "Enchantary": {
        "validators": [],
        "size": 19,
    },
    "Stack Scalers": {
        "validators": [],
        "size": 19,
    },
    "Tincture Tinkerers": {
        "validators": [],
        "size": 10,
    },
    "Inventors Initiative": {
        "validators": [],
        "size": 29,
    },
    "The Second Pillar Players": {
        "validators": [],
        "size": 17,
    },
    ##Deal with entanglement
    "Questboard Daily": {
        "validators": [],
        "size": 15,
    },
    "Walltoppers": {
        "validators": [],
        "size": 20,
    },
    "Masked Many": {
        "validators": [],
        "size": 30,
    },
    "Mendary Practitioners": {
        "validators": [],
        "size": 8,
    },
}

def test():
    totl = 0
    for element in clubs.values():
        totl += element["size"]
    print(totl)

def initialize_clubs():
    pass