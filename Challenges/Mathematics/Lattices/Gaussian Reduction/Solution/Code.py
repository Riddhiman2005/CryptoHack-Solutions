import math

def gaussian_lattice_reduction(v1, v2):
    while True:
        # Step (a): Swap vectors if ||v2|| < ||v1||
        if math.sqrt(v2[0]**2 + v2[1]**2) < math.sqrt(v1[0]**2 + v1[1]**2):
            v1, v2 = v2, v1
        
        # Step (b): Compute m = ⌊ v1∙v2 / v1∙v1 ⌉
        m = math.floor((v1[0]*v2[0] + v1[1]*v2[1]) / (v1[0]**2 + v1[1]**2))
        
        # Step (c): If m = 0, return v1, v2
        if m == 0:
            return v1, v2
        
        # Step (d): v2 = v2 - m*v1
        v2 = (v2[0] - m*v1[0], v2[1] - m*v1[1])

# Define the initial vectors
v = (846835985, 9834798552)
u = (87502093, 123094980)

# Apply Gaussian lattice reduction
v1, v2 = gaussian_lattice_reduction(v, u)

# Calculate the inner product of the new basis vectors
inner_product = v1[0]*v2[0] + v1[1]*v2[1]

# Print the inner product (the flag)
print("Inner product of the new basis vectors:", inner_product)
