import names.names_utility as name_gen
import roll_tables.hair_tables as hair_gen
from Spec import Spec

class Person:
    def __init__(self, presets = {}):
        generated_name = name_gen.create_names(1)
        generated_hair = hair_gen.hair.roll()
        self.hair = generated_hair

test = Person()
print(test.hair)