from sets import carnivorous,herbivorous

# set union
all_animals = carnivorous.union(herbivorous)
print(all_animals)

# set intersection
intersect_animals = carnivorous.intersection(herbivorous)
print(intersect_animals)

# set difference

carnivorous_only = carnivorous.difference(herbivorous)
print(carnivorous_only)

# issubet() 
herbivorous_subset = herbivorous.issubset(all_animals)
print(herbivorous_subset)