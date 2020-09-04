k = int(input())
s = list(map(int, input().split()))
S = set(s)
print(((sum(S)*k)-(sum(s)))//(k-1))

