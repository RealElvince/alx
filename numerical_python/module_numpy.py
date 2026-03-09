import numpy as np

# Create an array by passing in a list of lists.
ratings = np.array([[94, 89, 63, 45], [93, 92, 48, 23], [92, 94, 56, 98]])

print(ratings)

print(ratings.shape)

# create array of ones
array_ones = np.ones((2,2))

print(array_ones)

# Create an array of random values – pass in shape as a tuple.
random_array = np.random.random((3, 3))

print(random_array)


# numpy slicing
top_left_element = ratings[0,0]
print(top_left_element)