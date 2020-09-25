n, m = list(map(int, input().split()))

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())
arr.sort(key=lambda x: x[k])    #
for i in arr:
    print(*i, sep=' ')
