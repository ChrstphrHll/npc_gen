import names.names_utility as name_gen
import roll_tables.hair_tables as hair_gen

class Person:
    def __init__(self, presets = {}):
        ##Set Name
        if "name" in presets.keys():
            self.name = presets['name']
        else:
            self.name = name_gen.create_names(1)
        
        #Generate Hair
        generated_hair = hair_gen.hair.roll()
        self.hair = generated_hair

test = Person()
print(test.name)