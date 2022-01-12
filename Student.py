from Person import Person
import roll_tables.specification_tables as spec_gen


class Student(Person):
    def __init__(self):
        super().__init__()

        #Generate Track and Spec
        self.track = spec_gen.get_track()
        self.track = spec_gen.get_spec()

