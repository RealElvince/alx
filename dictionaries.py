first_dictionary = {}

print(type(first_dictionary))

# key-value

first_dictionary['first_key'] = 'first_value'

print(first_dictionary)

# update dictionary
extra_dictionary = {"second_key":"second_value","third_key":"third_value"}
first_dictionary.update(extra_dictionary)

print(first_dictionary)