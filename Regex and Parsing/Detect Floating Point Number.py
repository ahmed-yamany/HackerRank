import re
T = int(input())
lst = list()
for i in range(T):
    n = input()
    pattern = re.match(r'^[-+]?[0-9]*\.[0-9]+$', n)
    print(bool(pattern))


