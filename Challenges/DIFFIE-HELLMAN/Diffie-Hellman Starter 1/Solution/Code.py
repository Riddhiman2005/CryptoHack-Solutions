p = 991  # Prime modulus
g = 209  # Element in the finite field Fp

# Calculate the modular multiplicative inverse of g modulo p
d = pow(g, -1, p)

print(d)

