# concatenation
string_one = "Hello"
string_two = "World"

concat_string = string_one + " " + string_two

print(concat_string)

# string repliaction
original_string = "Amazing"

replicated_string = original_string*4
print(replicated_string)

# slicing positive indexing
text = "Python is amazing"
sub_string = text[0:6]
print(sub_string)

# slicing negative indexing
substring_two = text[-7:-1]
print(substring_two)


# upper() func

original_one = 'Hello, world'

upper_string = original_one.upper()

print(upper_string)

# lower() function

lower_string = original_one.lower()
print(lower_string)

# capitalize() string,capitalizes first letter of  string
capitalize_string = original_one.capitalize()
print(capitalize_string)

# strip() remove leading nd trailing white spaces

normal_string = '   This is a normal sentence.  '

strip_sentence = normal_string.strip()
print(strip_sentence)


# replace()

original_txt = 'Python is a powerful programming lanaguge.'

modified_txt = original_txt.replace('Python','Java')
print(modified_txt)