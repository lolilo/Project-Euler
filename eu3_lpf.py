n = 13195

# determines the largest prime factor of x
def lpf(x):
    # the smallest prime factor is 2
    # set the potential largest prime factor to 2 and start the algorithm
    lpf = 2

    # x represents our current largest factor
    # lpf will help calculate whether the current largest factor is prime
    # if x is equal to lpf, we will have found our prime
    while x > lpf:
        if x % lpf == 0:
            print '1. x is ', x
            print '1. lpf is ', lpf
            x = x / lpf
            print '2. x/lpf is ', x
            lpf = 2
            print 'Set lpf to %d' % lpf
            print ''
        else: 
            print 'x = %d, not evenly divisible by the current lpf = %d' % (x, lpf)
            lpf += 1
            print 'Set lpf to %d' % lpf
            print ''

    print '%d is not larger than %d' %(x, lpf)
    print 'Largest Prime Factor: %d' % lpf

def main():
    # n = int(raw_input("This script will calculate the largest prime factor of n. n = ? "))
    lpf(n)

if __name__ == '__main__':
    main()