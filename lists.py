# list constructor
birds = list(("Eagle","Penguin","Parrot"))
print(birds)

# range() function to generate a sequence of numbers based on a given start and end point.

range_list = list(range(0,5))
print(range_list)

# list type
print(type(birds))
print(type(range_list))

# concat two lists 

new_list = birds + range_list
print(new_list)

# copy a list using copy()

range_list_copy = range_list.copy()
print(range_list_copy)

mammals = list(("Elephant","Lion","Dolphin"))

# nested lists

animal_grouped = [mammals,birds]
print(animal_grouped)

# access second mammal

second_mammal = animal_grouped[0][1]
print(second_mammal)
