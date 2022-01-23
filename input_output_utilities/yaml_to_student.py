from os import listdir, getcwd
from os.path import isfile, join
import yaml

from Student import Student

###Returns a list of all the files in a target directory
def get_files(relative_directory = ''):
    current_directory = getcwd()
    target_directory = current_directory + relative_directory
    return [f for f in listdir(target_directory) if isfile(join(target_directory, f))]

###Reads in a file and returns it as a string
def open_file(path):
    with open(path) as f:
        data = f.read()
        return data

###Takes in a string and removes the md info at the end
def extract_yaml(md_file):
    if md_file[0:3] != "---":
        raise ValueError
    
    stripped_md = md_file[3:]

    md_start_index = stripped_md.find("\n---")
    yaml_string = stripped_md[:md_start_index]
    
    return yaml_string

###Takes a path and returns a student created from the yaml
def student_from_md(path):
    loaded_file = open_file(path)
    yaml_string = extract_yaml(loaded_file)

    student_presets = yaml.load(yaml_string, Loader=yaml.CLoader)
    student = Student(student_presets)

    return student

###Loads in a folder of student.md files as Student objects and 
###    returns it as a list
def load_roster(dir_path = "/students/"):
    student_files = get_files(dir_path)
    students = []

    for file in student_files:
        student = student_from_md(dir_path[1:] + file)
        students.append(student)
    
    return students
