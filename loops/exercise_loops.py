# Exercise 1

animals = ['Great White Shark', 'Blue Whale', 'African Elephant', 'Bald Eagle', 'Orangutan', 'Tiger', 'Panda', 'Koala']
for animal in animals:
    print(animal)


# Exercise 2 : Use a while loop to print numbers from 0 to 4.

i = 0
while i < 5:
    print(i)
    i += 1


# Exercise 3 : Stop the loop once you find Orangutan in the animals list.
for animal in animals:
    if animal == "Orangutan":
        break
    print(animal)


# Exercise 4 : use of continue

for animal in animals:
    if animal == "Bald Eagle":
        continue

    print(animal)


# Exercise 5 : create a loop that does nothing when 'Panda' is encountered, but prints other animals.
for animal in animals:
    if animal == "Panda":
        pass
    else:
        print(animal)