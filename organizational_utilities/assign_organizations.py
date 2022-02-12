import random, yaml
from soupsieve import select

class Organization():
    MAX_ORGS = 3

    def __init__(self, name, size, validators, de_validators=[]):
        self.name = name
        self.size = size
        self.validators = validators
        self.de_validators = de_validators
        self.members = []
        self.head = None
        self.leadership = []



    def fill_out_roster(self, students: list):
        roster = []

        if len(students) < self.size:
            raise ValueError("Given list of students is too small")

        choices = [x for x in range(len(students))]
        random.shuffle(choices)
        while len(roster) < self.size:
            selected_index = random.choice(choices)
            candidate = students[selected_index]
            meets_requirements = False

            if len(candidate.organizations) >= self.MAX_ORGS:
                choices.remove(selected_index)
                continue

            ##If no validators are given all is fair game
            if len(self.validators) == 0:
                meets_requirements = True

            for validator in self.validators:
                if validator(candidate):
                    meets_requirements = True
                    break
            
            for deval in self.de_validators:
                if deval(candidate):
                    meets_requirements = False
                    break

            if meets_requirements:
                roster.append(candidate)
                choices.remove(selected_index)
    
        self.members = roster
    
    def select_leadership(self):
        """Put various people in leadership positions"""
        ##Select head of the club
        top_dog = self.members[0]
        for student in self.members:
            if student.year > top_dog.year and not student.check_leadership():
                top_dog = student
        
        self.head = top_dog
        top_dog.add_organization(self.name, "Leader")
        self.members.remove(top_dog)

        ##Select supporting leadership
        non_first_years = list(filter(lambda x: x.year > 1, self.members))
        number_supporting_leadership = len(self.members) // 10
        self.leadership = random.sample(non_first_years, k = number_supporting_leadership)
        for student in self.leadership:
            self.members.remove(student)
            student.add_organization(self.name, "Leadership")

    def codify_students(self):
        """Adds this organization to the student's list"""
        for student in self.members:
            student.add_organization(self.name, "Member")

    def get_md(self):
        all_lines = []
        all_lines.append(f"# {self.name}")
        all_lines.append("---")
        all_lines.append("### Description")
        all_lines.append("")
        all_lines.append("### Members")
        ##TODO:add members table here
        all_lines.append(f"Led by [[{self.head.name}]]")
        all_lines.append("Leadership")
        for l in self.leadership:
            all_lines.append(f"- [[{l.name}]]")
        all_lines.append("Members")
        for l in self.members:
            all_lines.append(f"- [[{l.name}]]")        
        return "\n".join(all_lines)


    def make_org_sheet(self, path_input=-1):        
        if path_input == -1:
            path = f"clubs/{self.name}.md"
        else:
            path = f"{path_input}/{self.name}.md"

        with open(path, "w") as f:
            f.write("---\n")
            f.write(yaml.dump({"tags": ["club"]}))
            f.write("---\n")
            f.write(self.get_md())


