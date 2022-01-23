from Person import Person
import roll_tables.specification_tables as spec_gen
import roll_tables.stat_tables as stat_gen
from data.number_suffix import suffixes


class Student(Person):
    def __init__(self, presets = {}):
        super().__init__(presets)

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

    def get_md(self):
        all_lines = []
        all_lines.append(f"# {self.name}")
        all_lines.append("---")
        all_lines.append("### Description")
        all_lines.append(f"- {self.year}{suffixes[self.year-1]} year {self.race} {self.spec} in {self.guild}")
        all_lines.append(f"- {self.hair}, {self.eyes} eyes, and {self.skin} skin")
        all_lines.append(f"- Is {self.trait1} and {self.trait2}, and has {self.ideal} as their ideal")
        all_lines.append("")

        all_lines.append("### Organizations")
        for org in self.organizations:
            member_type = org["type"]
            org_name = org["name"]
            all_lines.append(f"{member_type} of [[{org_name}]]")

        all_lines.append("### Relationships")
        for relationship in self.relationships:
            rel_type = relationship["type"]
            rel_name = relationship["name"]
            all_lines.append(f"[[{rel_name}]]: {rel_type}")

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

    def set_partyID(self, partyID):
        self.partyID = partyID

    def set_guild(self, guild):
        self.guild = guild

    def set_year(self, year):
        self.year = year

