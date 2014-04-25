n1 = 1
n2 = 2
n3 = 0

n_list = [1,2]
even_n_list = []

while n3 < 4000000:
    n3 = n1 + n2
    if n3 < 4000000:
        n_list.append(n3)
        n1 = n2
        n2 = n3

for n in n_list:
    if n % 2 == 0:
        even_n_list.append(n)

print sum(even_n_list)