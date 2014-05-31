"""
Find the sum of the digits in the number 100!
"""

def factorial(n): 
    if n < 2:
        return 1
    return n * factorial(n-1)

def sum_digits(n):
    out = 0
    while n > 0:
        digit = n % 10
        if digit != 0:
            out += digit
        n /= 10
    return out

def digit_sum_with_string(n):
    n = str(n)
    out = 0
    for digit in n:
        out += int(digit)
    return out

n = factorial(100)
print sum_digits(n)
print digit_sum_with_string(n)
