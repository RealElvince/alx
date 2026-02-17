tree_tuple = (8,"apple","Granny Smith")
print(tree_tuple)

print(type(tree_tuple))

print(len(tree_tuple))

fruit = tree_tuple[1]

print(fruit)

# check tuple immutability
# tree_tuple[1] = "pear"

text_only = tree_tuple[1:3]
print(text_only)

fruit_summer = ("peach","apricot","plum")

fruit_winter = ("lemon","orange","grapefruit")

print(fruit_summer,fruit_winter)

# combine two tuples using concat
all_fruits = fruit_summer + fruit_winter

print(all_fruits)

# count how many times an element appears in a tuple
count_of_plum = all_fruits.count("plum")
print(count_of_plum)


# tuple unpacking

combine_info = ("yellow",5,"lemon")
color, age , tree_type = combine_info

print(color,age,tree_type)