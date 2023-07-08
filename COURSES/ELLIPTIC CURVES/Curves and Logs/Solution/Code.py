
import hashlib

# Elliptic curve parameters
a = 497
b = 1768
p = 9739
G = (1804, 5368)

# Alice's public key
QA = (815, 3190)

# Bob's secret integer
nB = 1829

# Point addition function
def point_addition(P, Q):
    if P is None:
        return Q
    elif Q is None:
        return P
    elif P[0] == Q[0] and P[1] == Q[1]:
        lam = (3 * P[0]**2 + a) * pow(2 * P[1], p - 2, p) % p
    else:
        lam = (Q[1] - P[1]) * pow(Q[0] - P[0], p - 2, p) % p
    x = (lam**2 - P[0] - Q[0]) % p
    y = (lam * (P[0] - x) - P[1]) % p
    return x, y

# Scalar multiplication function
def scalar_multiplication(P, n):
    Q = None
    for bit in bin(n)[2:]:
        Q = point_addition(Q, Q)
        if bit == '1':
            Q = point_addition(Q, P)
    return Q

# Calculate the shared secret
shared_secret = scalar_multiplication(QA, nB)

# Generate the key using the x-coordinate
x_coordinate = shared_secret[0]
key = hashlib.sha1(str(x_coordinate).encode()).hexdigest()

# Print the flag
print("Flag:", key)
