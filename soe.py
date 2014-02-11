import math
# Sieve of Eratosthenes to calculate prime numbers up to a given N
# http://www.cut-the-knot.org/Curriculum/Arithmetic/Eratosthenes.shtml
N = 100

# write all integers from 1 through N in order

# i = 2
# all_num = []
# while i < N:
#     all_num.append(i)
#     i += 1

all_num = range(N)
# remove 0 and 1 from the list
del all_num[0], all_num[0]

prime_num = []
inProgress = True

# The algorithm proceed sequentially in steps. 
while inProgress: 
    n = all_num[0]
    # print ' '
    # Repeat this step while the least available number does not exceed the square root of N.
    if n > math.sqrt(N):
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
            
# print "all_num", all_num
print "prime_num", prime_num



