import random

class Table:
    def __init__(self, *argv):
        list_of_entries = []
        list_of_pickers = []

        index = 0
        for element in argv:
            if isinstance(element[1], list):
                item_range = range(element[1][0],element[1][1]+1)
            else:
                item_range = range(element[1])

            if isinstance(element[0], list):
                for internal_element in element[0]:
                    list_of_entries.append(internal_element)
                    temp = [index for _ in item_range]
                    list_of_pickers += temp
                    index += 1
            else:
                list_of_entries.append(element[0])
                temp = [index for _ in item_range]
                list_of_pickers += temp
                index += 1

        
        self.list_of_entries = list_of_entries
        self.list_of_pickers = list_of_pickers

    def roll(self):
        index = random.randrange(len(self.list_of_pickers))
        element_index = self.list_of_pickers[index]
        element = self.list_of_entries[element_index]
        if isinstance(element, Table) or isinstance(element, MultiRoll):
            return element.roll()
        return element

class MultiRoll():
    def __init__(self, value, *argv):
        self.value = value
        self.tables = [argv[x] for x in range(len(argv))]

    def roll(self):
        results = []
        for element in self.tables:
            results.append(element.roll())
        return self.value.format(*results)