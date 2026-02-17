# create a set
carnivorous = {"Lion","Leopard","Hyena","Bear"}

print(carnivorous)
print(type(carnivorous))

# create a set from a list using set constructor

herbivorous = set(["Buffalo","Zebra","Antelope","Wildbeast"])

print(herbivorous)


# modify sets using add() and update()

herbivorous.add("Sheep")
print(herbivorous)

# update(): This adds elements from an iterable, such as lists and other sets, to the set.

carnivorous.update(["Fox","Vulture"])
print(carnivorous)