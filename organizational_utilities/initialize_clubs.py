from organizational_utilities.validators import *
import organizational_utilities.assign_organizations as org

clubs = {
    "Half Notes": {
        "validators": [prob_spec(["Bard"], 0.2)],
        "size": 15,
    },
    "Cracked Bell": {
        "validators": [prob_spec(["Rogue"], 0.46)],
        "size": 45,
    },
    "LOAM": {
        "validators": [prob_smth("track", ["Diplomacy", "Exploration"], 0.8)],
        "size": 21,
    },
    "Wayfinders": {
        "validators": [
            assert_field_maker("track", ["Exploration"]),
            assert_specs_maker(["Ranger"]),
            percent_above(.3)
        ],
        "size": 60,
    },
    "Splinters": {
        "validators": [
            assert_specs_maker(["Fighter", "Barbarian", "Ranger", "Paladin", "Rogue", "Monk"]),
            assert_field_maker("track", ["Assault"]),
            percent_above(.83)
        ],
        "size": 53,
    },
    "Aquaculture": {
        "validators": [
            assert_field_maker("origin", ["Glasscliff Garisons", "Whyndiem"]),
            percent_above(.80)
        ],
        "size": 12,
    },
    "Grason's Claw": {
        "validators": [
            assert_field_maker("spec", ["Druid", "Ranger"]),
            assert_field_maker("track", ["Assault"]),
            percent_above(.3)
        ],
        "size": 24,
    },
    "Inner Circle Judges": {
        "validators": [
            assert_field_maker("track", ["Diplomacy"]),
            percent_above(.8)
        ],
        "size": 13,
    },
    "Treskal Silkball": {
        "validators": [            
            silkball_m("Treskal")
        ],
        "devals": [
            check_other_club_m("Jettenia Silkball"),
            check_other_club_m("Burk Silkball"),
            check_other_club_m("Alderden Silkball"),
        ],
        "size": 15,
    },
    "Alderden Silkball": {
        "validators": [            
            silkball_m("Alderden")
        ],
        "devals": [
            check_other_club_m("Jettenia Silkball"),
            check_other_club_m("Burk Silkball"),
            check_other_club_m("Treskal Silkball"),
        ],
        "size": 15,
    },
    "Jettenia Silkball": {
        "validators": [
            silkball_m("Jettenia")
        ],
        "devals": [
            check_other_club_m("Alderden Silkball"),
            check_other_club_m("Burk Silkball"),
            check_other_club_m("Treskal Silkball"),
        ],
        "size": 15,
    },
    "Burk Silkball": {
        "validators": [            
            silkball_m("Burk")
        ],
        "devals": [
            check_other_club_m("Jettenia Silkball"),
            check_other_club_m("Alderden Silkball"),
            check_other_club_m("Treskal Silkball"),
        ],
        "size": 15,
    },
    "Trenchers": {
        "validators": [
            probe_stat_m("str", 13),
            percent_above(.6)
        ],
        "size": 25,
    },
    "Dragon Chess Club": {
        "validators": [
            probe_stat_m("int", 13),
            percent_above(.8)
        ],
        "size": 7,
    },
    "Mysten Students for a Better Revendale": {
        "validators": [],
        "size": 22,
    },
    "Ashari Cultural Group": {
        "validators": [
            assert_specs_maker(["Monk", "Druid"]),
            assert_field_maker("race", ["Genasi"]),
            percent_above(.86)
        ],
        "size": 20,
    },
    "Forgetenders": {
        "validators": [
            assert_specs_maker(["Artificer", "Fighter"]),
            assert_field_maker("track", ["Exploration"]),
            assert_field_maker("race", ["Dwarf", "Gnome"]),
            percent_above(.58)
        ],
        "devals": [check_other_club_m("Threaded Needle")],
        "size": 34,
    },
    "Threaded Needle": {
        "validators": [
            assert_specs_maker(["Fighter", "Ranger", "Druid", "Rogue", "Monk"]),
            percent_above(.57)
        ],
        "devals": [check_other_club_m("Forgetenders")],
        "size": 34,
    },
    "Pious Fellowship": {
        "validators": [
            assert_specs_maker(["Paladin", "Cleric"]),
            percent_above(.69)
        ],
        "size": 33,
    },
    "Ruin Runners": {
        "validators": [
            assert_field_maker("track", ["Exploration"]),
            percent_above(.29)
        ],
        "size": 40,
    },
    "Hand of Order": {
        "validators": [
            assert_specs_maker(["Fighter", "Paladin", "Barbarian"]),
            assert_field_maker("track", ["Protection"]),
            percent_above(.64)
        ],
        "size": 38,
    },
    "Spellweavers": {
        "validators": [
            assert_specs_maker(["Wizard", "Sorcerer", "Bard"]),
            percent_above(.90)
        ],
        "size": 28,
    },
    "Golemic Consortium": {
        "validators": [
            assert_specs_maker(["Artificer", "Wizard", "Sorcerer"]),
            percent_above(.78)
        ],
        "size": 14,
    },
    "Enchantary": {
        "validators": [
            assert_specs_maker(["Artificer", "Wizard", "Sorcerer", "Cleric", "Bard"]),
            percent_above(.95)
        ],
        "size": 19,
    },
    "Stack Scalers": {
        "validators": [
            assert_specs_maker(["Wizard"]),
            assert_field_maker("track", ["Exploration"]),
            percent_above(.34)
        ],
        "size": 19,
    },
    "Tincture Tinkerers": {
        "validators": [
            assert_specs_maker(["Rogue"]),
            assert_field_maker("track", ["Exploration"]),
            assert_field_maker("race", ["Gnome"]),
            percent_above(.72)
        ],
        "size": 10,
    },
    "Inventors Initiative": {
        "validators": [
            assert_specs_maker(["Artificer"]),
            assert_field_maker("track", ["Exploration"]),
            assert_field_maker("race", ["Gnome"]),
            percent_above(.5)
        ],
        "size": 29,
    },
    "The Second Pillar Players": {
        "validators": [
            assert_specs_maker(["Bard"]),
            assert_field_maker("track", ["Diplomacy"]),
            percent_above(.58)
        ],
        "size": 17,
    },
    ##Deal with entanglement
    "Questboard Daily": {
        "validators": [
            assert_field_maker("track", ["Exploration", "Diplomacy"]),
            percent_above(.93)
        ],
        "size": 15,
    },
    "Walltoppers": {
        "validators": [
            probe_stat_m("con", 13),
            percent_above(.6)
        ],
        "size": 20,
    },
    "Masked Many": {
        "validators": [
            assert_field_maker("track", ["Diplomacy"]),
            percent_above(.86)
        ],
        "size": 30,
    },
    "Mendary Practitioners": {
        "validators": [
            assert_field_maker("spec", ["Druid", "Ranger"]),
            assert_field_maker("track", ["Protection"]),
            percent_above(.8)
        ],
        "size": 16,
    },
    "Phantasmal Reality Lab": {
        "validators": [
            assert_specs_maker(["Wizard"]),
            assert_field_maker("track", ["Exploration"]),
            percent_above(.89)
        ],
        "size": 6,
    },
}

def test():
    totl = 0
    for element in clubs.values():
        totl += element["size"]
    print(totl)

def initialize_clubs(students):
    for student in students:
        student.organizations = []

    #TODO: wieght silkball teams
    #Sep between

    for title, specifiers in clubs.items():
        if "devals" in specifiers:
            devals = specifiers["devals"]
        else:
            devals = []
        temp = org.Organization(title, specifiers["size"], specifiers["validators"], de_validators=devals)
        
        temp.fill_out_roster(students)
        temp.select_leadership()
        temp.codify_students()
        temp.make_org_sheet()