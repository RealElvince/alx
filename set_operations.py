from sets import carnivorous,herbivorous

# set union
all_animals = carnivorous.union(herbivorous)
print(all_animals)

# set intersection
intersect_animals = carnivorous.intersection(herbivorous)
print(intersect_animals)