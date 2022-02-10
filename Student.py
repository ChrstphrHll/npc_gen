from Person import Person
import roll_tables.specification_tables as spec_gen
import roll_tables.stat_tables as stat_gen
import  data.number_suffix as sfx


class Student(Person):
    def __init__(self, presets = {}):
        super().base_generation(presets)

        #Generate Track and Spec
        if not self.set_if_preset("track", presets):
            self.track = spec_gen.get_track()
        if not self.set_if_preset("spec", presets):
            self.spec = spec_gen.get_spec()

        #Generate Stats
        if not self.set_if_preset("stats", presets):
            self.stats = stat_gen.get_stats(self.spec)

        #Generate Placeholder Year, Guild, and PartyID
        if not self.set_if_preset("year", presets):
            self.year = None
        if not self.set_if_preset("guild", presets):
            self.guild = None
        if not self.set_if_preset("partyID", presets):
            self.partyID = None
        
        self.tags = self.create_tags()

    def get_md(self):
        all_lines = []
        all_lines.append(f"# {self.name}")
        all_lines.append("### Description")
        all_lines.append(f"- {self.race} {self.spec} from {self.origin}")
        all_lines.append(f"- {sfx.suffixify_number(self.year)} year {self.track} student in {self.guild}")
        all_lines.append(f"- {self.hair}, {self.eyes} eyes, and {self.skin} skin")
        all_lines.append(f"- Is {self.trait1} and {self.trait2}, and has {self.ideal} as their ideal")
        all_lines.append("")

        all_lines.extend(self.readable_notes())
        all_lines.extend(self.readable_organizations())
        all_lines.extend(self.readable_relationships())

        all_lines.append("### Stats")
        all_lines.append(self.get_stat_block())

        return "\n".join(all_lines)

    def get_stat_block(self):
        stats = [self.stats["str"],self.stats["dex"],self.stats["con"],self.stats["int"],self.stats["wis"],self.stats["cha"]]
        stat_block = f"""```statblock
name: {self.name}
stats: {stats}
```"""
        return stat_block
    
    def create_tags(self):
        tags = super().create_tags()
        tags.append(self.spec)
        tags.append(self.track)
        tags.append("Student")
        tags.append(sfx.suffixify_number(self.year))
        tags.append(self.guild)
        return self.process_spaces(tags)

    def set_partyID(self, partyID):
        self.partyID = partyID

    def set_guild(self, guild):
        self.guild = guild

    def set_year(self, year):
        self.year = year

