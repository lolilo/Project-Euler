#Sieve of Eratosthenes to calculate prime numbers up to a given N

import math

i = 2
N = 100
all_num = []

while i < N:
    all_num.append(i)
    i += 1

prime_num = []
inProgress = True

while inProgress: 

    n = all_num[0]
    print ' '
    if n > math.sqrt(N):
        print "break!", n, math.sqrt(N)
        print n > math.sqrt(N)
        prime_num.extend(all_num)
        inProgress = False
        break

    #mark first number as prime
    prime_num.append(n)

    for x in all_num:
        print "for x", x
        print "for n", n
        if x % n == 0:
            print "if", x
            print all_num
            all_num.remove(x)




            
print "all_num", all_num
print "prime_num", prime_num