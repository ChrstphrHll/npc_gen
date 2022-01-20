from Person import Person
from Student import Student
import student_body as sb_gen
import organizational_utilities.roster_utilities as ru
import relational_functions.connect_party as cp

import json, random

# test = Student()
# test.write_char_sheet()

roster = sb_gen.create_students()

cp.connect_party(roster)

for stud in roster:
    stud.write_char_sheet()