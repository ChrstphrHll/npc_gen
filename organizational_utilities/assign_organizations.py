import random

class Organization():
    def __init__(self, name, size, validators):
        self.name = name
        self.size = size
        self.validators = validators
        self.members = []
        self.head = None
        self.leadership = []

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
    
    def select_leadership(self):
        """Put various people in leadership positions"""
        ##Select head of the club
        top_dog = self.members[0]
        for student in self.members:
            if student.year > top_dog.year:
                top_dog = student
        
        self.head = top_dog
        top_dog.add_organization(self.name, "Leader")
        self.members.remove(top_dog)

        ##Select supporting leadership
        non_first_years = filter(lambda x: x.year > 1, self.members)
        number_supporting_leadership = len(non_first_years) // 10
        self.leadership = random.choices(non_first_years, k = number_supporting_leadership)
        for student in self.leadership:
            self.members.remove(student)
            student.add_organization(self.name, "Leadership")

    def codify_students(self):
        """Adds this organization to the student's list"""
        for student in self.members:
            student.add_organization(self.name, "Member")


