
X = int(input())
shoe_size = list(map(int, input().split()))

lst = []

for i in range(int(input())):
    lst.append(tuple(map(int, input().split())))
N = 0
for i, s in lst:
    if i in shoe_size:
        N += s
        shoe_size.remove(i)

print(N)
