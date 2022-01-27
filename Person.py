import names.names_utility as name_gen
import roll_tables.look_tables as look_gen
import roll_tables.personality_tables as person_gen
import roll_tables.race_tables as race_gen
import roll_tables.birthday_tables as bday_gen
import roll_tables.origin_tables as ori_gen

import yaml

class Person:
    def __init__(self, presets = {}, tag_generation = True):
        ##Set Name
        if not self.set_if_preset("name", presets):
            self.name = name_gen.create_names(1)[0]
        
        #Generate Race
        if not self.set_if_preset("race", presets):
            self.race = race_gen.get_race()

        #Generate Appearence
        if not self.set_if_preset("hair", presets):
            self.hair = look_gen.get_hair(self.race)
        if not self.set_if_preset("eyes", presets):
            self.eyes = look_gen.get_eyes(self.race)
        if not self.set_if_preset("skin", presets):
            self.skin = look_gen.get_skin(self.race)

        #Generate Personality Traits
        if not self.set_if_preset("ideal", presets):
            self.ideal = person_gen.get_ideal()
        if not self.set_if_preset("trait1", presets):
            self.trait1 = person_gen.get_interact("positive")
        if not self.set_if_preset("trait2", presets):
            self.trait2 = person_gen.get_interact("negative")

        if not self.set_if_preset("trait", presets):
            self.trait = person_gen.get_trait()
        if not self.set_if_preset("flaw", presets):
            self.flaw = person_gen.get_flaw()
        if not self.set_if_preset("bond", presets):
            self.bond = person_gen.get_bond()

        #Generate Birthday
        if not self.set_if_preset("birthday", presets):
            self.birthday = bday_gen.get_bday()

        #Generate Origin
        if not self.set_if_preset("origin", presets):
            self.origin = ori_gen(self.race)

        #Initialize placeholders
        if not self.set_if_preset("relationships", presets):
            self.relationships = []
        if not self.set_if_preset("organizations", presets):
            self.organizations = []

        #Set tags
        if tag_generation:
            self.tags = self.create_tags()
    
    def set_if_preset(self, element, presets):
            if element in presets.keys():
                setattr(self, element, presets[element])
                return True
            return False

    def create_tags(self):
        tags = [self.race]
        return tags

    def get_description(self):
        current_character_description = ""
        for property, value in vars(self).items():
            current_character_description += f"{property}: {value}\n"
        return current_character_description

    def get_file_path(self):
        ##TODO: make sure students directory is present
        return f"students/{self.name}.md"

    def get_md(self):
        all_lines = []
        all_lines.append(f"# {self.name}")
        all_lines.append("---")
        all_lines.append("### Description")
        all_lines.append(f"- {self.race}")
        all_lines.append(f"- {self.hair}, {self.eyes} eyes, and {self.skin} skin")
        all_lines.append(f"- Is {self.trait1} and {self.trait2}, and has {self.ideal} as their ideal")
        all_lines.append("")
        all_lines.append("### Relationships")
        for relationship in self.relationships:
            rel_type = relationship["type"]
            rel_name = relationship["name"]
            all_lines.append(f"[[{rel_name}]]: {rel_type}")

        return "\n".join(all_lines)



    def write_char_sheet(self, path_input = -1):
        yaml_frontmatter = yaml.dump(self.__dict__, sort_keys = False)
        
        if path_input == -1:
            path = self.get_file_path()
        else:
            path = path_input

        with open(path, "w") as f:
            f.write("---\n")
            f.write(yaml_frontmatter)
            f.write("---\n")
            f.write(self.get_md())