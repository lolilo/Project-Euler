
i=1
sum = 0
square_of_num = 0
sum_of_squares = 0

while i < 101:
    sum += i
    square_of_num = i*i
    sum_of_squares += square_of_num
    i += 1

square_of_sum = sum*sum

difference = square_of_sum - sum_of_squares
print difference