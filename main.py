from Person import Person
from Student import Student

import json, random

test = Student()
print(test.get_description())

def create_students():
    with open("names/final_list.json") as f:
        names = json.load(f)['names']

    students = []
    for name in names:
        temp = Student({"name": name})
        students.append(temp)

    random.shuffle(students)

    students_processed = []
    party_id = 1
    while students != []:
        party_sizes = [2,3,4,5]
        party_size_wieghts = [2,3,3,1]
        if len(students) <= 5:
            party_size = len(students)
        else:
            party_size = random.choices(party_sizes, party_size_wieghts)[0]
        
        temp_party = []
        for _ in range(party_size):
            current = students.pop()
            current.partyID = party_id
            temp_party.append(current)

        students_processed.append(temp_party)
        party_id += 1


    guilds = {
        "Alderden": [],
        "Fiesn": [],
        "Jettenia": [],
        "Elkenval": [],
        "Treskal": [],
        "Burk": []
    }

    for element in students_processed:
        guild = random.choice(list(guilds.keys()))
        for student in element:
            student.guild = guild
        guilds[guild].append(element)

    years = [1,2,3,4,5,6,7,8,9]
    year_weights = [18*2, 13*2, 11*2, 8*2, 5*2, 4*2, 3+6, 5, 1]
    for key, value in guilds.items():
        print(key)
        total = 0
        for party in value:
            year = random.choices(years, year_weights)[0]
            for kid in party:
                kid.year = year
            total += len(party)
        print("parties:", len(value), "kids:", total)

    for name, parties in guilds.items():
        l = [0,0,0,0,0,0,0,0,0]
        for party in parties:
            l[party[0].year - 1] += 1

        print(name[:3], l)
        