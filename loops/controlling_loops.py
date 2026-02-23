# Exercise 1
endangered_marine_species = ['Hawksbill Turtle', 'Vaquita', 'Blue Whale', 'Staghorn Coral', 'Green Turtle']
endangered_count = 0

for species in endangered_marine_species:
    endangered_count  += 1

print(f"Number of endangered marine species: {endangered_count}")


# Exercise 2
initial_forested_area = 1000  # in square kilometres
deforestation_rate = 20       # square kilometres per year

# Your task: Use a while loop to determine how many years it takes for the forested area to fall below 500 square kilometres
years = 0
while initial_forested_area > 500:
    initial_forested_area -= deforestation_rate
    years += 1

print(f"Years until critical deforestation level: {years}")


# Exercise 3 
animals = ['Tiger', 'Blue Whale', 'African Elephant', 'Koala', 'Panda']
endangered_animals = ['Tiger', 'Blue Whale', 'African Elephant']

# Your task: Use a for loop to print out each animal's name and its endangered status
for animal in animals:
    if animal in endangered_animals:
        print(f"{animal} is endangered!")
    else:
        print(f"{animal} is not endangered!")


ocean_pollution_data = {
    'Pacific Ocean': [3, 5, 2],  # pollution levels
    'Atlantic Ocean': [7, 2, 4],
    'Indian Ocean': [5, 1, 3]
}

# Exercise 4 
# Your task: Use loops to calculate the average pollution level for each ocean and print it
for ocean, pollution_levels in ocean_pollution_data.items():
    total_poluttion = sum(pollution_levels)
    average_pollution = total_poluttion/len(pollution_levels)

    print(f"The average pollution level in {ocean} is {average_pollution:.2f}")

# Exercise 5
current_population = 150  # of a particular endangered species
target_population = 500
years = 0
growth_rate = 1.07  # 7% annual growth due to conservation efforts

# Your task: Use a while loop to calculate how many years it takes to reach the target population
while current_population < target_population:
    current_population *= growth_rate
    years += 1

print(f"Years to reach target population: {years}")

