p = 29
ints = [14, 6, 11]

def find_quadratic_residue(p, ints):
    quadratic_residue = None
    for a in range(1, p):
        if (a**2) % p in ints:
            quadratic_residue = (a**2) % p
            break
    return quadratic_residue

def calculate_square_root(p, quadratic_residue):
    a = 1
    while (a**2) % p != quadratic_residue:
        a += 1
    return a

quadratic_residue = find_quadratic_residue(p, ints)
square_root = calculate_square_root(p, quadratic_residue)

print(square_root)
