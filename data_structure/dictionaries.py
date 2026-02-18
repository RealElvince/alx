first_dictionary = {}

print(type(first_dictionary))

# key-value

first_dictionary['first_key'] = 'first_value'

print(first_dictionary)

# update dictionary
extra_dictionary = {"second_key":"second_value","third_key":"third_value"}
first_dictionary.update(extra_dictionary)

print(first_dictionary)

# remove key value pair from a dictionary
del first_dictionary['third_key']

print(first_dictionary)

# create dictionary with dict() fucntion

second_dictionary = dict(first_key="first_key",second_key="second_value",extra_key="extra_value")
print(second_dictionary)