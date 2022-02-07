import random
from Student import Student

def degree_of_success(degree, func):
    """Given a degree and a function, will return True degree% of the time
    and return the results of the function otherwise"""
    def biased_func(x):
        if random.randint(0,99) < degree * 100:
            return True
        return func(x)
    return biased_func

def assert_specs(specs: list, student):
    """Given a spec and a Student object, will return True if the 
    student is a member of any given spec"""
    if student.spec in specs:
        return True
    return False

def main():
    probably_bard = degree_of_success(.5, lambda x: assert_specs(["Bard"], x))
    tim = Student({"spec": "Ranger"})
    print(probably_bard(tim))