def chinese_remainder_theorem(congruences):
    # Calculate N as the product of all moduli
    N = 1
    for congruence in congruences:
        N *= congruence[1]

    result = 0
    for congruence in congruences:
        ai, ni = congruence  # ai = residue, ni = modulus

        # Calculate the values for Chinese Remainder Theorem
        Ni = N // ni
        xi = pow(Ni, -1, ni)  # Calculate the modular inverse of Ni modulo ni

        result += ai * Ni * xi

    return result % N


# Set of linear congruences: x ≡ 2 mod 5, x ≡ 3 mod 11, x ≡ 5 mod 17
congruences = [(2, 5), (3, 11), (5, 17)]

# Calculate the value of a such that x ≡ a mod 935
a = chinese_remainder_theorem(congruences)
print(a)
