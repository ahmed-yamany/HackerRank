A = set(map(int, input().split()))
n = int(input())


def check_subset(sub):
    if sub in A:
        return True
    else:
        return False


s = []
for i in range(n):
    N = set(map(int, input().split()))

    H = list(map(check_subset, N))
    for j in H:
        s.append(j)

if False in s:
    print(False)
else:
    print(True)
