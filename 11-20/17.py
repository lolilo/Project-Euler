"""
If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?


NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

d = {
    1: 'one', 
    2: 'two', 
    3: 'three', 
    4: 'four', 
    5: 'five', 
    6: 'six', 
    7: 'seven',
    8: 'eight', 
    9: 'nine', 
    10: 'ten', 
    11: 'eleven', 
    12: 'twelve', 
    13: 'thirteen',
    15: 'fifteen',
    18: 'eighteen'
}

def number_in_words(n):
    if n == 0:
        return ''
    if 1 <= n <= 13 or n == 15 or n == 18: 
        return d[n]
    if 14 <= n <= 19:
        return number_in_words(n%10) + 'teen' 
    if 20 <= n <= 29:
        return 'twenty' + number_in_words(n%10)
    if 30 <= n <= 39:
        return 'thirty' + number_in_words(n%10)
    if 40 <= n <= 49:
        return 'forty' + number_in_words(n%10)
    if 50 <= n <= 59:
        return 'fifty' + number_in_words(n%10)
    if 60 <= n <= 69:
        return 'sixty' + number_in_words(n%10)
    if 70 <= n <= 79:
        return 'seventy' + number_in_words(n%10)
    if 80 <= n <= 89:
        return 'eighty' + number_in_words(n%10)
    if 90 <= n <= 99:
        return 'ninety' + number_in_words(n%10)
    if n % 100 == 0 and n < 1000: 
        return number_in_words(n/100) + 'hundred' 
    if 100 <= n <= 999:
        return number_in_words(n/100) + 'hundredand' + number_in_words(n%100)
    if n == 1000: 
        return 'onethousand'
    return 'Not valid input.'

def letter_count(s):
    count = 0
    for char in s: # instead of checking for spaces or hyphens, when I product the strings, just don't include them
        if char == ' ' or char == '-':
            continue
        count += 1
    return count

def one_to_one_thousand(n):
    count = 0
    for num in xrange(1, n+1):
        
        num_in_words = number_in_words(num)
        # print num
        # print num_in_words
        count += letter_count(num_in_words)
    return count

test1 = "three hundred and forty-two"
test2 = "one hundred and fifteen"

# print letter_count(test1)
# print letter_count(number_in_words(20))
# print number_in_words(1)
# print number_in_words(13)
# print number_in_words(19)
# print number_in_words(29)
# print number_in_words(39)
# print number_in_words(115)
# print number_in_words(239)
# print number_in_words(1000)
# print one_to_one_thousand(5)
# print one_to_one_thousand(19) #okay
# print one_to_one_thousand(99) # fourty vs forty. Wow. That was bullshit. 
print one_to_one_thousand(1000)
