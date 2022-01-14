import names.names_utility as name_gen
import roll_tables.look_tables as look_gen
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

        #Generate Appearence
        self.hair = look_gen.get_hair(self.race)
        self.eyes = look_gen.get_eyes(self.race)
        self.skin = look_gen.get_skin(self.race)

        #Generate Personality Traits
        self.ideal = person_gen.get_ideal()
        self.positive_trait = person_gen.get_interact("positive")
        self.negative_trait = person_gen.get_interact("negative")

        self.trait = person_gen.get_trait()
        self.flaw = person_gen.get_flaw()
        self.bond = person_gen.get_bond()
    
    def get_description(self):
        current_character_description = ""
        for property, value in vars(self).items():
            current_character_description += f"{property}: {value}\n"
        return current_character_description