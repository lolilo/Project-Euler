"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def sum_digits(n):
    out = 0
    while n > 0:
        digit = n % 10
        if digit != 0:
            out += digit
        n /= 10
    return out

n = 2**1000
print sum_digits(n)
