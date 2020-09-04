import itertools

K , M = list(map(int, input().split()))
lst = []
for i in range(K):
    l = list(map(int, input().split()))
    n = l[0]
    lst.append(l[1:])
    assert len(lst[i]) == n


S_max = 0
L_max = None

for l in itertools.product(*L):
    s = sum([x**2 for x in l]) % N

    if s > S_max:
        S_max = s
        L_max = l

print S_max
