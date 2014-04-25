n = 13195

# determines the largest prime factor of the input integer

# largest_factor represents our current largest factor
# smallest_divisor will help calculate whether the current largest factor is prime
# if largest_factor is equal to smallest_divisor, it is a prime number
def lpf(largest_factor):

    # the smallest possible non-trivial divisor is 2
    smallest_divisor = 2

    while largest_factor != smallest_divisor:
        if largest_factor % smallest_divisor == 0:
            print 'largest_factor %d is evenly divisible by smallest_divisor %d' % (largest_factor, smallest_divisor)
            largest_factor = largest_factor / smallest_divisor
            print 'largest_factor/smallest_divisor = ', largest_factor
            smallest_divisor = 2
            # print 'Set smallest_divisor to %d' % smallest_divisor
            print ''
        else: 
            # print 'largest_factor = %d, not evenly divisible by the current smallest_divisor = %d' % (largest_factor, smallest_divisor)
            smallest_divisor += 1
            # print 'Set smallest_divisor to %d' % smallest_divisor
            # print ''

    print 'largest_factor %d is equal to smallest_divisor %d, so largest_factor is prime' %(largest_factor, smallest_divisor)
    return largest_factor

def main():
    # n = int(raw_input("This script will calculate the largest prime factor of n. n = ? "))
    print lpf(n)

if __name__ == '__main__':
    main()