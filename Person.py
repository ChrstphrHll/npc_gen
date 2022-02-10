import names.names_utility as name_gen
import roll_tables.look_tables as look_gen
import roll_tables.personality_tables as person_gen
import roll_tables.race_tables as race_gen
import roll_tables.birthday_tables as bday_gen
import roll_tables.origin_tables as ori_gen
import roll_tables.voice_tables as voice_gen

import yaml

class Person:
    def __init__(self, presets = {}):
        self.base_generation(presets)
        self.tags = self.create_tags()
    
    def base_generation(self, presets):
        #Makes sets the core attributes of the person
        ##Set Name
        if not self.set_if_preset("name", presets):
            self.name = name_gen.create_names(1)[0]
        
        #Generate Race
        if not self.set_if_preset("race", presets):
            self.race = race_gen.get_race()

        #Generate Appearance
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
            self.origin = ori_gen.get_origin(self.race)

        #Generate Voice
        if not self.set_if_preset("voice", presets):
            self.voice = voice_gen.get_voice()

        #Set relevance
        if not self.set_if_preset("relevance", presets):
            self.relevance = 0

        #Initialize placeholders
        if not self.set_if_preset("relationships", presets):
            self.relationships = []
        if not self.set_if_preset("organizations", presets):
            self.organizations = []
        if not self.set_if_preset("notes", presets):
            self.notes = []

    def set_if_preset(self, element, presets):
            if element in presets.keys():
                setattr(self, element, presets[element])
                return True
            return False

    def create_tags(self):
        tags = [self.race, self.origin]
        for org in self.organizations:
            tags.append(org["name"])
        return self.process_spaces(tags)
        
    def process_spaces(self, list: list) -> list:
        """Takes a list of strings and returns a list with spaces 
        replaced by _s"""
        processed_list = []
        for element in list:
            processed_list.append(element.replace(" ", "_"))
        return processed_list

    def __str__(self):
        current_character_description = ""
        for property, value in vars(self).items():
            current_character_description += f"{property}: {value}\n"
        return current_character_description

    def get_file_path(self):
        ##TODO: make sure students directory is present
        return f"students/{self.name}.md"

    def add_organization(self, org: str, status: str):
        """Adds an organization org of type status to the person"""
        membership = {"name": org, "type": status}
        self.organizations.append(membership)

    def get_md(self):
        all_lines = []
        all_lines.append(f"# {self.name}")
        all_lines.extend(self.readable_description())
        all_lines.extend(self.readable_organizations())
        all_lines.extend(self.readable_relationships())
        return "\n".join(all_lines)

    def readable_description(self):
        """Function to be used by get_md. Returns a list of lines that describe the person"""
        description = []
        description.append("### Description")
        description.append(f"- {self.race} from {self.origin}")
        description.append(f"- {self.hair}, {self.eyes} eyes, and {self.skin} skin")
        description.append(f"- Is {self.trait1} and {self.trait2}, and has {self.ideal} as their ideal")
        description.append("")
        return description

    def readable_organizations(self):
        """Function to be used by get_md. Returns a list of lines that describe the organizations
        a person is a part of"""
        organizations = []
        organizations.append("### Organizations")
        for org in self.organizations:
            member_type = org["type"]
            org_name = org["name"]
            organizations.append(f"- {member_type} of [[{org_name}]]")
        organizations.append("")
        return organizations

    def readable_relationships(self):
        """Function to be used by get_md. Returns a list of lines that describe the
        relationships of the person"""
        relationships = []
        relationships.append("### Relationships")
        for relationship in self.relationships:
            rel_type = relationship["type"]
            rel_name = relationship["name"]
            relationships.append(f"- [[{rel_name}]]: {rel_type}")
        relationships.append("")
        return relationships

    def readable_notes(self):
        """Function to be used by get_md. Returns a list of lines that are notes 
        about the person"""
        notes_lines = []
        notes_lines.append("### Notes")
        for note in self.notes:
            notes_lines.append(f"- {note}")
        notes_lines.append("")
        return notes_lines

    def write_char_sheet(self, path_input = -1):
        yaml_frontmatter = yaml.dump(self.__dict__, sort_keys = False)
        
        if path_input == -1:
            path = self.get_file_path()
        else:
            path = f"{path_input}/{self.name}.md"

        with open(path, "w") as f:
            f.write("---\n")
            f.write(yaml_frontmatter)
            f.write("---\n")
            f.write(self.get_md())