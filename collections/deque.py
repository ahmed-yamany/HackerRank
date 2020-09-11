from collections import deque
d = deque()
N = int(input())
for i in range(N):
    names = input().split()
    string = names[0]
    if len(names) > 1:
        eval('d.'+string+'(names[1])')
    else:
        eval('d.'+string+'()')

for i in d:
    print(i, end=' ')
