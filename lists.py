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


# slicing list from 2nd to 3rd index

names = ["Elvis","Otieno","Toto","Malia","Nyandolo"]

sliced_names = names[2:4]

print(sliced_names)

# list modification
names_copy = names.copy()

# append: This adds the element passed into it as a single element to the end of the list.
names_copy.append("Kelvin")
print(names_copy)

names_copy.append(["Moses","Rachel"])
print(names_copy)

# use of extend :This adds elements passed into it as separate elements to the end of the list.

names_copy.extend(["Oliver","Meshack","Ken"])
print(names_copy)

# insert(): : This inserts an element at a specified position

names_copy.insert(2,"Elijah")
print(names_copy)

# del,remove,pop
# del : This deletes an element or multiple elements from the list at the specified index value/s.

del names_copy[1]
del names_copy[2:5]
print(names_copy)


# remove(): This removes the first occurrence of a specified value from the list.

names_copy.remove("Kelvin")
print(names_copy)

# pop(): This removes and returns the element at the specified index

pop_names = names_copy.pop(2)
print(pop_names)
print(names_copy)

# change value of an element at given index

names_copy[1] = "Mercy"
print(names_copy)