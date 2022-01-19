import json, random 
from Student import Student

def create_students():
    ##Read in list of finalized names
    with open("names/final_list.json") as f:
        names = json.load(f)['names']

    ##Create a student object for each of the loaded names
    students = []
    for name in names:
        temp = Student({"name": name})
        students.append(temp)

    ##Shuffle the list of students
    random.shuffle(students)

    ##Create parties of students of size 2-5
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

    ##Assign parties to guilds
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

    ##Assign years to parties
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

    ##Some visualization for looking at the generated results
    for name, parties in guilds.items():
        l = [0,0,0,0,0,0,0,0,0]
        for party in parties:
            l[party[0].year - 1] += 1

        print(name[:3], l)
        