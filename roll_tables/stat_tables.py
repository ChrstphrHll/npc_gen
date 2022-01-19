import random, json

stats = {
    "str": "Strength",
    "dex": "Dexterity",
    "con": "Constitution",
    "int": "Intelligence",
    "wis": "Wisdom",
    "cha": "Charisma",
}

high_stats = {
    "Artificer": "int",
    "Barbarian": "str",
    "Bard": "cha",
    "Cleric": "wis",
    "Druid": "wis",
    "Fighter": ["str", "dex"],
    "Monk": "dex",
    "Paladin": "str",
    "Ranger": "dex",
    "Rouge": "dex",
    "Sorcerer": "cha",
    "Wizard": "int"
}

def get_spec():
    return random.choice(list(high_stats.keys()))

def get_best_stat(spec):
    best_stat_or_stats = high_stats[spec]
    if isinstance(best_stat_or_stats, list):
        return random.choice(best_stat_or_stats)
    return best_stat_or_stats

def get_stats(spec):
    #Rolls stats
    raw_stats = []
    stats_returned = {
        "str": 10,
        "dex": 10,
        "con": 10,
        "int": 10,
        "wis": 10,
        "cha": 10
    }

    for trial in range(6):
        #Roll four times
        rolls = random.choices([1,2,3,4,5,6], k=4)
        
        #Drop lowest roll
        rolls.sort(reverse = True)
        result = 0
        for index in range(3):
            result += rolls[index]
        raw_stats.append(result)
    
    raw_stats.sort()

    #See if best or second best roll will go to recommended best stat
    choice_list = [True, False]
    choice_list_weights = [75, 25]
    best_stat_first = random.choices(choice_list, choice_list_weights)[0]

    #Get a list of the needed stats
    stats_to_be_processed = list(stats_returned.keys())

    #Get recommended best stat and remove it from the list, then shuffle
    best_stat = get_best_stat(spec)
    stats_to_be_processed.remove(best_stat)
    random.shuffle(stats_to_be_processed)

    if not best_stat_first:
        selected_stat_name = stats_to_be_processed.pop()
        selected_stat_num = raw_stats.pop()
        stats_returned[selected_stat_name] = selected_stat_num
    
    selected_stat_num = raw_stats.pop()
    stats_returned[best_stat] = selected_stat_num

    while stats_to_be_processed != []:
        selected_stat_name = stats_to_be_processed.pop()
        selected_stat_num = raw_stats.pop()
        stats_returned[selected_stat_name] = selected_stat_num

    return stats_returned