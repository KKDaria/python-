list_cubes = []

for i in range(1, 1000, 2 ):
    list_cubes.append(i**3)
def sum_numbers(value):
    res = 0

    while value != 0:
        res += value % 10
        value //= 10
    return res
res = 0
for i in list_cubes:
    if sum_numbers(i) % 7 == 0:
        res += i
print(res)


def sum_numbers(value):
    res_1 = 0
    while value != 0:
        res_1 += value % 10
        value //= 10
    return res_1
res_1 = 0

for x in list_cubes:
    if sum_numbers(x+17) % 7 == 0:
        res_1 += x
        print(res_1)
