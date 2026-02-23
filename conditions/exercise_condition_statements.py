
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