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

def assert_specs(specs: list, student: Student):
    """Given a spec and a Student object, will return True if the 
    student is a member of any given spec"""
    if student.spec in specs:
        return True
    return False

def assert_specs_maker(specs: list):
    """Returns a function that checks for the given specs"""
    return lambda x: assert_specs(specs, x)

def assert_specs_within_degree_maker(specs: list, degree: float):
    """Makes a function that takes in a student and will return true
    degree% of the time, or True if the student is one of the specs
    listed"""
    specs_asserter = assert_specs_maker(specs)
    validator = lambda x: degree_of_success(degree, specs_asserter)

def assert_field_maker(field: str, allowed_values: list):
    """Makes a validator function given the fields and values"""
    pass

def main():
    probably_bard = degree_of_success(.5, lambda x: assert_specs(["Bard"], x))
    tim = Student({"spec": "Ranger"})
    print(probably_bard(tim))