from Person import Person
import roll_tables.specification_tables as spec_gen


class Student(Person):
    def __init__(self, presets = {}):
        super().__init__(presets)

        #Generate Track and Spec
        self.track = spec_gen.get_track()
        self.spec = spec_gen.get_spec()

        #Generate Placeholder Year, Guild, and PartyID
        self.year = None
        self.guild = None
        self.partyID = None

