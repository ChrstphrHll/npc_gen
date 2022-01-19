from Person import Person
from Student import Student
import student_body as sb_gen
import relational_functions.connect_party as cp

import json, random

# test = Student()
# print(test.get_description())

#sb_gen.create_students()

test = []
for num in range(10):
    temp = Student()
    temp.set_partyID(num % 3)
    test.append(temp)

cp.connect_party(test)

for stud in test:
    print(stud.name, stud.relationships, "\n")