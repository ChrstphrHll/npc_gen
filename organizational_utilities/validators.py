import random
from student import Student
from person import Person

def degree_of_success(degree, func):
    """Given a degree and a function, will return True degree% of the time
    and return the results of the function otherwise"""
    def biased_func(x):
        ##Chance that someone gets in regardless of spec
        if random.randint(0,99) > degree * 100:
            return True
        ##result of spec
        return func(x)
    return biased_func

def percent_above(degree):
    def dummy(student):
        if random.randint(0,99) > degree * 100:
            return True
        return False
    return dummy

def assert_specs(specs: list, student: Student):
    """Given a spec and a Student object, will return True if the 
    student is a member of any given spec"""
    if student.spec in specs:
        return True
    return False

def assert_specs_maker(specs: list):
    """Returns a function that checks for the given specs"""
    return lambda x: assert_specs(specs, x)

def prob_spec(specs: list, degree: float):
    """Makes a function that takes in a student and will return true
    degree% of the time, or True if the student is one of the specs
    listed"""
    specs_asserter = assert_specs_maker(specs)
    validator = lambda x: degree_of_success(degree, specs_asserter)
    return validator

def assert_field_maker(field: str, allowed_values: list):
    """Makes a validator function given the fields and values"""
    def dummy(student):
        if getattr(student, field) in allowed_values:
            return True
        return False
    return dummy

def prob_smth(field: str, values: list, degree: float):
    """Makes a function that has an returns True for field unless it's
    the 1-degree percent of the time that it doesn't"""
    return degree_of_success(degree, assert_field_maker(field, values))    

def probe_stat_m(stat: str, thresh: int):
    """Makes a function that probes a stat"""
    def dummy(student):
        if student.stats[stat] >= thresh:
            return True
        return False
    return dummy

def check_other_club_m(club: str):
    def dummy(student):
        for mem in student.organizations:
            if mem["name"] == club:
                return True
        return False
    return dummy

def silkball_m(guild: str):
    def dummy(student):
        guild_v = False
        if student.guild == guild:
            guild_v = True
        elif student.guild in ["Elkenval", "Fiesn"]:
            if random.randint(0,9) < 3:
                guild_v = True
        if not guild_v:
            return False
        
        if student.stats["str"] > 13:
            return True
        if student.stats["dex"] > 13:
            return True
        if student.stats["con"] > 15:
            return True
    return dummy


def main():
    probably_bard = degree_of_success(.9, lambda x: False)
    tim = Person({"spec": "Bard"})
    for _ in range(100): print(probably_bard(tim))