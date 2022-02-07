class Organization():
    def __init__(self, name, size, validators):
        self.name = name
        self.size = size
        self.validators = validators
        self.members = []
        self.leaders = []
        self.supervisors = []

    def fill_out_roster(self, students: list):
        roster = []

        while len(roster) < self.size:
            candidate = students.pop()
            meets_requirements = True
            
            for validator in self.validators:
                if not validator(candidate):
                    meets_requirements = False
                    break
            
            if meets_requirements:
                roster.append(candidate)
    
        self.members = roster
    
    