from .Table import Table, MultiRoll
import random

def load_data(file_name):
    with open(file_name) as f:
        file_contents = f.read()
        return file_contents.split("\n")

traits = load_data("data/traits.txt")
flaws = load_data("data/flaws.txt")
ideals = load_data("data/ideals.txt")
bonds = load_data("data/bonds.txt")
interacts = load_data("data/interact.txt")

def get_element(list):
    random.shuffle(list)
    return list[0]

def get_trait():
    return get_element(traits)

def get_flaw():
    return get_element(flaws)

def get_ideal():
    return get_element(ideals)

def get_bond():
    return get_element(bonds)

def get_interact():
    return get_element(interacts)