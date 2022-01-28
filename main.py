from Person import Person
from Student import Student
import student_body as sb_gen
import organizational_utilities.roster_utilities as ru
import relational_functions.connect_party as cp
import input_output_utilities.yaml_to_student as read
import roll_tables.look_tables as gen_looks

import json, random

##TODO:
# fix hair tables
# add in organizations
# add friendships based on organizations
# add in origins
# relationships
# familial bonds
# professors

def update_roster(roster, functions = []):
    for student in roster:
        for function in functions:
            function(student)
        student.write_char_sheet()

def update_eyes(person):
    person.eyes = gen_looks.get_eyes(person.race)


# update_roster(read.load_roster(), [update_eyes])

if __name__ == "__main__":
    for _ in range(1000):
        person = Person()
        if 3:
            print(person.name)