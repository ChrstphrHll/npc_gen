import random

class Spec:
    def check_priority_lst(lst):
        needed_stats = ["str", "dex", "con", "int", "wis", "cha"]

        for element in lst:
            if not element in needed_stats:
                raise Exception("Incorrect Prio list")

    def __init__(self, name, priority_lst):
        self.check_priotity_lst()

        self.name = name
        
        #Rolls stats
        raw_stats = []
        for trial in range(6):
            #Roll four times
            rolls = random.choices([1,2,3,4,5,6], k=4)
            
            #Drop lowest roll
            rolls.sort()
            result = 0
            for roll in range(3):
                result += roll
            raw_stats.append(result)
        
        stats = {}
        raw_stats.sort()
        for stat_type in priority_lst:
            stats[stat_type] = raw_stats.pop()

        self.stats = stats
        
class Wizard(Spec):
    def check_priority_lst(lst):
        return super().check_priority_lst(lst)

    def __init__(self):
        super().__init__("wizard", ["int", "wis", "dex", "str", "cha", "con"])

tom = Wizard()
tom.name