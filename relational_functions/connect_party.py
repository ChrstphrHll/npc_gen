from organizational_utilities.roster_utilities import get_party_lists

def connect_party(student_body):
    parties_to_process = get_party_lists(student_body)
    

    for party in parties_to_process:
        for studentA in party:
            for studentB in party:
                if studentA != studentB:
                    relationship = {"name": studentB.name, "type": "partymate"}
                    studentA.relationships.append(relationship)
                
