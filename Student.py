from Person import Person
import roll_tables.specification_tables as spec_gen
import roll_tables.stat_tables as stat_gen


class Student(Person):
    def __init__(self, presets = {}):
        super().__init__(presets)

        #Generate Track and Spec
        self.track = spec_gen.get_track()
        self.spec = spec_gen.get_spec()

        #Generate Stats
        self.stats = stat_gen.get_stats(self.spec)

        #Generate Placeholder Year, Guild, and PartyID
        self.year = None
        self.guild = None
        self.partyID = None
        
    def set_partyID(self, partyID):
        self.partyID = partyID

    def set_guild(self, guild):
        self.guild = guild

    def set_year(self, year):
        self.year = year

