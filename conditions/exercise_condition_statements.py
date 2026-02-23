
 # Exercise 1
individuals_in_wild = 5500

if individuals_in_wild < 1000:
    print("Critically Endangered")

elif individuals_in_wild <= 5000:
    print("Endangered")

elif individuals_in_wild <= 20000:
    print("Vulnerable")

else:
    print("Safe")


# Exercise 2
rainfall = 205
population_density = 448

if rainfall < 500 and population_density > 500:
    print("Severe Scarcity")

elif (500 <= rainfall <= 1000) and (200 <= population_density <= 500):
    print("Moderate Scarcity")

else:
    print("No Scarcity")


# Exercise 3

material = "metal"
size = "medium"

if size == "large" and (material == "metal" or material == "glass"):
    print("Special Handling")

elif size == "medium" or ( size =="small" and (material == "metal" or material == "glass")):
    print("Standard Recycling")

elif size == "small" and material == "paper":
    print("Composting")

else:
    print("Landfill")