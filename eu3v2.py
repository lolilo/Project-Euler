import math

"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

given_number = 600851475143

# Sieve of Eratosthenes to calculate prime numbers up to a given N
# http://www.cut-the-knot.org/Curriculum/Arithmetic/Eratosthenes.shtml
def soe(given_number):
    # write all integers from 1 through N in order
    all_num = range(given_number)
    # remove 0 and 1 from the list
    del all_num[0], all_num[0]

    prime_num = []
    inProgress = True

    # The algorithm proceed sequentially in steps. 
    while inProgress: 
        n = all_num[0]
        # print ' '
        # Repeat this step while the least available number does not exceed the square root of N.
        if n > math.sqrt(given_number):
            # print "break!", n, math.sqrt(N)
            # print n > math.sqrt(N)
            prime_num.extend(all_num)
            inProgress = False
            break
        # On every step, find the first number not yet crossed, mark it as prime and 
        prime_num.append(n)
        # cross out all of its remaining multiples. 
        for x in all_num:
            # print "for x", x
            # print "for n", n
            if x % n == 0:
                # print "if", x
                # print all_num
                all_num.remove(x)
                
    return prime_num

# returns lists of all factors of n
def factors(given_number):
    f = []
    range_f = range(given_number + 1)
    del range_f[0]
    for i in range_f:
        if given_number % i == 0:
            f.append(i)
    return f

# factors = factors(given_number)
# primes = soe(given_number)
print list(set(factors(given_number)) & set(soe(given_number)))


# prime_factors = []

# for i in factors and primes: 
#     prime_factors.append(i)

# print prime_factors

# print factors(given_number)
# print soe(13195)