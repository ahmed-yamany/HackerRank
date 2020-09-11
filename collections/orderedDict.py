from collections import OrderedDict
N = int(input())
dct = OrderedDict()
for i in range(N):
    name_price = input().split()
    string = ' '.join(name_price[:-1])

    if string not in dct:
        dct[string] = int(name_price[-1])
    else:
        dct[string] += int(name_price[-1])
for i, j in dct.items():
    print(i, j)
