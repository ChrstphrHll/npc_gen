from random import choices
import data.nations as ng

def get_origin(race=-1):
    #TODO: update to include race
    if race:
        nations = ng.get_nations()
        weights = ng.get_nation_populations()
        return choices(nations, weights)[0]
    return "the void"