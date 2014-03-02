import math
# Sieve of Eratosthenes to calculate prime numbers up to a given N
# http://www.cut-the-knot.org/Curriculum/Arithmetic/Eratosthenes.shtml
N = 2000000

# write all integers from 1 through N in order
# remove 0 and 1 from the list

all_num_boolean_list = [True] * N
# index 0 is "1"
all_num_boolean_list[0] = False

inProgress = True
counter = 2
# list_of_primes = []

# The algorithm proceed sequentially in steps. 
while inProgress: 
    # start at 2
    # n = counter


    # print ' '
    # Repeat this step while the least available number does not exceed the square root of N.
    if counter > math.sqrt(N):
        # print "break!", n, math.sqrt(N)
        # print n > math.sqrt(N)
        inProgress = False
        break
    # On every step, find the first number not yet crossed, mark it as prime and 
    # prime_num.append(n)

    # print counter
    # print ''
    # cross out all of its remaining multiples. 
    for x in xrange(counter + 1, N + 1):
        # print "for x", x
        # print "for n", n

        if x % counter == 0:
            # print "if", x
            # print all_num
            all_num_boolean_list[x - 1] = False
    
    counter += 1

sum_of_primes = 0

for i in xrange(len(all_num_boolean_list)):
    if all_num_boolean_list[i]:
        sum_of_primes += i + 1

print sum_of_primes


