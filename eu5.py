d_list = []
n = 1
s = 1
boolean = True
issmallest = False

while n < 11:
    d_list.append(n)
    n += 1

print d_list


while boolean:
    for n in d_list:
        if s % n != 0:
            issmallest = False
            break
        else:
            issmallest = True

    if issmallest:
        print s
        boolean = False
    s += 1
    