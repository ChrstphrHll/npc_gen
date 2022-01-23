from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from Student import Student

def open_file(path):
    with open(path) as f:
        data = f.read()
        return data

def extract_yaml(md_file):
    if md_file[0:3] != "---":
        raise ValueError
    
    stripped_md = md_file[3:]

    md_start_index = stripped_md.find("\n---")
    yaml_string = stripped_md[:md_start_index]
    
    return yaml_string

def student_from_md(path):
    loaded_file = open_file(path)
    yaml_string = extract_yaml(loaded_file)

    student_presets = load(yaml_string, Loader=Loader)
    student = Student(student_presets)

    return student
