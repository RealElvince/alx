tree = {
    'tree_type':'Pepper-bark tree',
    'age':15,
    'family':'canellaceae'
}

# print value associated with key age

age_value = tree['age']
print(age_value)

# update tree dictionary 

kingdom = {'kingdom':'Plantae'}
tree.update(kingdom)
print(tree)


# remove family key-pair from tree dictionary

del tree['family']
print(tree)

# update tree type to Wild Cinamon

tree['tree_type'] = 'Wild Cinamon'

print(tree)

#Extract the keys and values from our tree dictionary, and store the values in two separate lists, key_list and value_list.
key_list = list(tree.keys())
value_list = list(tree.values())
print(key_list,value_list)