
message = 12
exponent = 65537
p = 17
q = 23

modulus = p * q
ciphertext = pow(message, exponent, modulus)

print(ciphertext)
