from os import listdir, getcwd
from os.path import isfile, join
import yaml, re

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

    #TODO: implement get_relationships function
    notes = get_section_elements("Notes", loaded_file)
    relationships_raw = get_section_elements("Relationships", loaded_file)
    relationships = process_name_type_list(relationships_raw)
    organizations_raw = get_section_elements("Organizations", loaded_file)
    organizations = process_name_type_list(organizations_raw)

    student_presets = yaml.load(yaml_string, Loader=yaml.CLoader)
    student_presets["notes"] = notes
    student_presets["relationships"] = relationships
    student_presets["organizations"] = organizations
    student = Student(student_presets)

    return student

def process_name_type_list(relationships_raw: list):
    """Given a list of properly formated relationships, returns a list of 
    the relationships as dictionaries"""
    formatted_relationships = []
    
    for rel_string in relationships_raw:
        try:
            [rel_name, rel_type] = rel_string.split(": ")
            rel_dict = {"name": rel_name[2:-2], "type": rel_type}
            formatted_relationships.append(rel_dict)
        except:
            return f"Error: {rel_string} not properly formatted"
    return formatted_relationships

def get_section_elements(section_title: str, md_file_contents: str):
    """takes a section title and the string of a md_file and returns the elements under 
    that section"""
    regex_string = r"### " + section_title + r"\n(- .*\n)*"
    regex = re.compile(regex_string)
    result_match = regex.search(md_file_contents)

    ##Results is a list that starts with ### section_title and ends with a ""
    results = result_match.group().split("\n")

    processed_results = process_section(results)

    return processed_results

def process_section(section_array: list):
    """takes a section array from get_section and returns its entries without their
    bullet points"""
    processed_elements = []
    for entry in section_array:
        if entry != "" and  entry[0] == "-":
            processed_elements.append(entry[2:])
    return processed_elements


###Loads in a folder of student.md files as Student objects and 
###    returns it as a list
def load_roster(dir_path = "/students/"):
    student_files = get_files(dir_path)
    students = []

    for file in student_files:
        student = student_from_md(dir_path[1:] + file)
        students.append(student)
    
    return students
