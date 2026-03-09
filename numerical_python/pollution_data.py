import numpy as np

pollution_data = np.array([[45, 65, 70], [55, 60, 50], [60, 58, 67]])

most_polluted_day_index = np.argmax(pollution_data.mean(axis=1))

print(pollution_data[most_polluted_day_index])