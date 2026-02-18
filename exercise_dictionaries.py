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
