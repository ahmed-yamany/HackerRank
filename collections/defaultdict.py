from collections import defaultdict
n, m = list(map(int, input().split()))
d = defaultdict(list)

for i in range(n):
    A = input()
    d[A].append(str(i+1))

for i in range(m):
    B = input()
    print(' '.join(d[B]) or -1)



