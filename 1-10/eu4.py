max_num = 999
first_number = max_num
second_number = max_num
boolean = True
possible = []

while second_number > 0 and boolean:
    first_number = max_num
    while first_number > 0 and boolean:

        product = first_number * second_number
        converted_product = str(product)
        reverse_product = converted_product[::-1]

        if converted_product == reverse_product:
            possible.append(product)
            #print first_number, second_number
            #print converted_product
            #boolean = False

        first_number -= 1

    second_number -= 1

#print possible
print max(possible)