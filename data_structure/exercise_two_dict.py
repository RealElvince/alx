"""
Docstring for exercise_two_dict
We have been provided with a basic nested dictionary containing African tree species. We have just received more detailed information on these trees and need to add it to this nested dictionary. Use the code provided as a starting point, adding in the extra information where required.
New information

Baobab:

country – Zimbabwe
average_height – 25
Acacia:

country – South Africa
average_height – 15
"""

# basic dictionary provided 
african_trees = {
    "Baobab": {
        "common_name": "Baobab",
        "scientific_name": "Adansonia",
    },
    "Acacia": {
        "common_name": "Acacia",
        "scientific_name": "Acacia",
    }
}


# update new information
baobab_new_info = {'country':'Zimbabwe','average_height':25}
african_trees['Baobab'].update(baobab_new_info)


acacia_new_info = {'country':'South Africa','average_height':15}
african_trees['Acacia'].update(african_trees)

print(african_trees)