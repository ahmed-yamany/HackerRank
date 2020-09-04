A = int(input())
N = set(map(int, input().split()))
for i in range(int(input())):
    a = input().split()
    n = set(map(int, input().split()))
    eval('N.' + a[0] + '(n)')
print(sum(N))
