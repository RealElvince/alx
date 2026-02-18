variable_a = 4.57
variable_b = "1233"

variable_a = float(variable_a)
variable_b = int(variable_b)

result = variable_a + variable_b
print("result",":",type(result))

# Perform a casting on mixed_variable to obtain a float and an integer version. Print both results along with their data types.
mixed_variable = 56.78

float_version = float(mixed_variable)
integer_version = int(float_version)

print("float_version",":",type(float_version))
print("integer_version",":",type(integer_version))