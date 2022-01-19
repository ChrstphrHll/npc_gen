
def get_party_lists(roster):
    party_dict = {}

    for student in roster:
        if student.partyID in list(party_dict.keys()):
            party_dict[student.partyID].append(student)
        else:
            party_dict[student.partyID] = [student]

    return list(party_dict.values())
