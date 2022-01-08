
set = []

record = False
num_recorded = 7
with open("data/raw.txt") as f:
    current = 'ding'
    while current != "":
        current = f.readline()
        ##print(current)
        if num_recorded == 6:
            record = False
        if record:
            num_recorded += 1
            if not current in set:
                set.append(current)
        if current[:-1] == "Flaw:":
            record = True
            num_recorded = 0

# with open("data/ideals.txt") as f:
#     current = "ding"
#     while current != "":
#         current = f.readline()
#         if not current in set:
#             set.append(current)

set.sort()
with open("data/flaw_test.txt", "w") as f:
    for element in set:
        f.write(element)

    