M = int(input())
A = set(map(int, input().split()))
N = int(input())
B = set(map(int, input().split()))
lst = []
for i in A:
    if i not in B:
        lst.append(i)

for i in B:
    if i not in A:
        lst.append(i)

lst.sort()
for i in lst:
    print(i)
