from .Table import Table, MultiRoll
import random

def load_data(file_name):
    with open(file_name) as f:
        file_contents = f.read()
        return file_contents.split("\n")

traits = load_data("data/traits.txt")
flaws = load_data("data/flaws.txt")
ideals = load_data("data/ideals_alt.txt")
bonds = load_data("data/bonds.txt")
positive_traits = load_data("data/positive_interact.txt")
neutral_traits = load_data("data/neutral_interact.txt")
negative_traits = load_data("data/negative_interact.txt")

def get_element(list):
    return random.choice(list)

def get_trait():
    return get_element(traits)

def get_flaw():
    return get_element(flaws)

def get_ideal():
    return get_element(ideals)

def get_bond():
    return get_element(bonds)

def get_interact(trait_type):
    if trait_type == "positive":
        return get_element(positive_traits + neutral_traits)
    if trait_type == "negative":
        return get_element(negative_traits + neutral_traits)