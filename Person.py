import names.names_utility as name_gen
import roll_tables.look_tables as look_gen
import roll_tables.personality_tables as person_gen
import roll_tables.race_tables as race_gen
import roll_tables.stat_tables as stat_gen
import roll_tables.birthday_tables as bday_gen

class Person:
    def __init__(self, presets = {}):
        ##Set Name
        if "name" in presets.keys():
            self.name = presets['name']
        else:
            self.name = name_gen.create_names(1)[0]
        
        #Generate Race and Spec
        self.race = race_gen.get_race()
        self.spec = stat_gen.get_spec()

        #Generate Stats
        self.stats = stat_gen.get_stats(self.spec)

        #Generate Appearence
        self.hair = look_gen.get_hair(self.race)
        self.eyes = look_gen.get_eyes(self.race)
        self.skin = look_gen.get_skin(self.race)

        #Generate Personality Traits
        self.ideal = person_gen.get_ideal()
        self.trait1 = person_gen.get_interact("positive")
        self.trait2 = person_gen.get_interact("negative")

        self.trait = person_gen.get_trait()
        self.flaw = person_gen.get_flaw()
        self.bond = person_gen.get_bond()

        #Generate Birthday
        self.birthday = bday_gen.get_bday()

        #Initialize placeholders
        self.relationships = []
    
    def get_description(self):
        current_character_description = ""
        for property, value in vars(self).items():
            current_character_description += f"{property}: {value}\n"
        return current_character_description