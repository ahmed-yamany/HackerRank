from collections import deque
d = deque()
T = int(input())
lst = []
for i in range(T):
    n = int(input())
    sideLengths = list(map(d.append, input().split()))
    side_lst = []
    for j in range(int(n/2)):
        if d.pop() == d.popleft():
            side_lst.append('Yes')
        else:
            side_lst.append('No')

    lst.append(side_lst)

for i in lst:
    result = 'Yes' if i.count('Yes') >= i.count('No') else 'No'
    print(result)
