import math

# Define the vector
v = (4, 6, 2, 5)

# Calculate the size (norm) of the vector
size = math.sqrt(sum(component ** 2 for component in v))

# Print the size of the vector
print("The size of the vector is:", size)
