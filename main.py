from Person import Person
from Student import Student
import student_body as sb_gen
import organizational_utilities.roster_utilities as ru
import relational_functions.connect_party as cp
import input_output_utilities.yaml_to_student as read
import roll_tables.look_tables as gen_looks
import roll_tables.origin_tables as ori_gen
import roll_tables.voice_tables as voice_gen
import organizational_utilities.validators as v
import organizational_utilities.initialize_clubs as init_clubs

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

def update_hair(person):
    person.hair = gen_looks.get_hair(person.race)

def update_origin(person):
    if person.relevance == 0:
        person.origin = ori_gen.get_origin(person.race)

def refresh_tags(person: Student):
    person.tags = person.create_tags()

def update_voice(person):
    person.voice = voice_gen.get_voice()

# update_roster(read.load_roster(), [update_eyes])

if __name__ == "__main__":
    students = read.load_roster()
    current_updaters = [
        refresh_tags
    ]
    update_roster(students, current_updaters)
    
