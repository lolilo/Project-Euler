# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# set a to 500 and count down
# set b to 0 and count upwards
# c will be 1000 - a - b, calculate c from a and b
# check if a^2 + b^2 = c^2

# a = 500
# b = 0

def Pythagorean_triplet_product():
    for a in range(500):
        for b in range(500):
            c = 1000 - a - b
            print a, b, c
            if a**2 + b**2 == c**2:
                return a*b*c
            b -= 1
        a += 1

print Pythagorean_triplet_product()

