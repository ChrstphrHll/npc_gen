import names.names_utility as name_gen
import roll_tables.look_tables as look_gen
import roll_tables.personality_tables as person_gen
import roll_tables.race_tables as race_gen
import roll_tables.stat_tables as stat_gen
import roll_tables.birthday_tables as bday_gen

import yaml

class Person:
    def __init__(self, presets = {}):
        def set_if_preset(element):
            if element in presets.keys():
                setattr(self, element, presets[element])
                return True
            return False

        ##Set Name
        if not set_if_preset("name"):
            self.name = name_gen.create_names(1)[0]
        
        #Generate Race
        if not set_if_preset("race"):
            self.race = race_gen.get_race()

        #Generate Appearence
        if not set_if_preset("hair"):
            self.hair = look_gen.get_hair(self.race)
        if not set_if_preset("eyes"):
            self.eyes = look_gen.get_eyes(self.race)
        if not set_if_preset("skin"):
            self.skin = look_gen.get_skin(self.race)

        #Generate Personality Traits
        if not set_if_preset("ideal"):
            self.ideal = person_gen.get_ideal()
        if not set_if_preset("trait1"):
            self.trait1 = person_gen.get_interact("positive")
        if not set_if_preset("trait2"):
            self.trait2 = person_gen.get_interact("negative")

        if not set_if_preset("trait"):
            self.trait = person_gen.get_trait()
        if not set_if_preset("flaw"):
            self.flaw = person_gen.get_flaw()
        if not set_if_preset("bond"):
            self.bond = person_gen.get_bond()

        #Generate Birthday
        if not set_if_preset("birthday"):
            self.birthday = bday_gen.get_bday()

        #Initialize placeholders
        if not set_if_preset("relationships"):
            self.relationships = []
        if not set_if_preset("organizations"):
            self.organizations = []
    
    def get_description(self):
        current_character_description = ""
        for property, value in vars(self).items():
            current_character_description += f"{property}: {value}\n"
        return current_character_description

    def get_file_path(self):
        ##TODO: make sure students directory is present
        return f"students/{self.name}.md"

    def get_md(self):
        title = f"#{self.name}"
        line = "---"
        desc = "### Description"
        appe = f"- {self.hair}, {self.eyes} eyes, and {self.skin} skin"
        psnl = f"Is {self.trait1} and {self.trait2}, and has {self.ideal} as their ideal"
        nwln = ""
        

    def write_char_sheet(self):
        yaml_frontmatter = yaml.dump(self.__dict__)
        path = self.get_file_path()

        with open(path, "w") as f:
            f.write("---\n")
            f.write(yaml_frontmatter)
            f.write("---\n")