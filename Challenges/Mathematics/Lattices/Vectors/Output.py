
# Define the vectors v, w, and u
v = (2, 6, 3)
w = (1, 0, 0)
u = (7, 7, 2)

# Calculate the expression 3*(2*v - w) ∙ 2*u

# Step 1: Calculate the vector 2*v - w
vector_1 = (2 * v[0] - w[0], 2 * v[1] - w[1], 2 * v[2] - w[2])

# Step 2: Multiply each component of vector_1 by 3
vector_2 = (3 * vector_1[0], 3 * vector_1[1], 3 * vector_1[2])

# Step 3: Multiply each component of vector_2 by 2*u and calculate the dot product
result = vector_2[0] * 2 * u[0] + vector_2[1] * 2 * u[1] + vector_2[2] * 2 * u[2]

# Print the result
print("The result of the expression is:", result)
