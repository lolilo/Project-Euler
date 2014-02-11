n = 13195
all_prime_numbers = [2]
prime_factors = []

potential_prime = 3

while (potential_prime < n / 2):
    prime_check = 2
    isPrime = True

    while prime_check < potential_prime:
        if potential_prime % prime_check != 0:
            prime_check += 1
        else:
            isPrime = False
            break

    if isPrime and n % potential_prime == 0:
        prime_factors.append(potential_prime)
        #all_prime_numbers.append(potential_prime)

    potential_prime += 1

#for x in all_prime_numbers:
 #   if n % x == 0:
  #      prime_factors.append(x)

print max(prime_factors)