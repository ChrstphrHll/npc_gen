import sys, os, random, json

###Given a file name and a delimiter, it will return a list of all the
## data in the file
def read_names(file_name, delimiter):
    with open(file_name) as file:
        raw_data = file.read()
        split_data = raw_data.split(delimiter)
    return split_data

###Reads in data from specifically named files in the given directory path
## Files should be named as follows
## dictionaryKey_specifier_format.txt
def loader(dir):
    name_dict = {}

    arr = os.listdir(dir)
    arr = filter(lambda x: x[:1] != "n_", arr)
    for file_name in arr:
        loaded_names = []
        full_file_name = dir + file_name
        list_info = file_name.split("_")
        if len(list_info) != 3:
            print("Not a valid name")
            continue
        (key, spec, format) = list_info
        processed_format = format.split(".")[0]

        if processed_format == "csv":
            loaded_names = read_names(full_file_name, ", ")
        elif processed_format == "dn":
            loaded_names = read_names(full_file_name, "\n\n")
        elif processed_format == "newline":
            loaded_names = read_names(full_file_name, "\n")
        else:
            print("Not a valid file format")
            continue
        
        if key in name_dict.keys():
            name_dict[key] += loaded_names
        else:
            name_dict[key] = loaded_names

    return name_dict

###Create n randomly generated names from the raw data in names_raw
## Returns a list of the generated names
def create_names(n, dir = "names/names_raw/"):
    #Read in names from names_raw dir
    raw_names = loader(dir)

    #Set first and last name list with wieghts for weighted random selection
    first_name_lists = [raw_names["first"], raw_names["altFirst"]]
    first_name_weights = [45, 55]

    last_name_lists = [raw_names["last"], raw_names["wild"]]
    last_name_weights = [1, 4]

    names = []
    for _ in range(n):
        first_name_list = random.choices(first_name_lists, first_name_weights)[0]
        last_name_list = random.choices(last_name_lists, last_name_weights)[0]

        chosen_first = random.choice(first_name_list)
        chosen_last = random.choice(last_name_list)

        created_name = chosen_first + " " + chosen_last
        names.append(created_name)
    
    return names



