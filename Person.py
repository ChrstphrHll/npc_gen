import names.names_utility as name_gen
import roll_tables.hair_tables as hair_gen
import roll_tables.personality_tables as person_gen
import roll_tables.race_tables as race_gen

class Person:
    def __init__(self, presets = {}):
        ##Set Name
        if "name" in presets.keys():
            self.name = presets['name']
        else:
            self.name = name_gen.create_names(1)[0]
        
        #Generate Race
        self.race = race_gen.get_race()

        #Generate Hair
        generated_hair = hair_gen.hair.roll()
        self.hair = generated_hair

        #Generate Personality Traits
        self.trait = person_gen.get_trait()
        self.flaw = person_gen.get_flaw()
        self.bond = person_gen.get_bond()
        self.ideal = person_gen.get_ideal()
        self.interaction = person_gen.get_interact()
    
    def get_description(self):
        current_character_description = ""
        for property, value in vars(self).items():
            current_character_description += f"{property}: {value}\n"
        return current_character_description