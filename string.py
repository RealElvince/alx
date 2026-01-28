my_string = "Hello, World"

# access character using positive indexing
first_character = my_string[0]
second_character = my_string[1]
third_character = my_string[2]



print("The first character is",":",first_character)
print("The second character is",":",second_character)
print("The third character is",":",third_character)
print(my_string[1:4])

# access characters using negative indexing 
last_char = my_string[-1]
second_char = my_string[-2]
first_char = my_string[-12]

print("The last character",":",last_char)
print("The second last character",":",second_char)
print("The first character",":",first_char)

# Creating new string through concatenation

original_string = "Hello"
new_string = original_string + ", World!"
print(new_string)