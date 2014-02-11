prime_list = [2]
potential_prime = 3
counter = 1
final_number = 0

while counter != 6:
    
    prime_check = 2
    isPrime = True

    while prime_check < potential_prime:
        if potential_prime % prime_check != 0:
            prime_check += 1
        else:
            isPrime = False
            break


    if isPrime:
        counter += 1
        #print counter
        #print potential_prime
        final_number = potential_prime
    potential_prime += 1

print final_number 