T = int(input())
for i in range(T):
    a, A = int(input()), set(map(int, input().split()))
    b, B = int(input()), set(map(int, input().split()))

    def check_subset(sub):
        if sub in B:
            return True
        else:
            return False


    H = list(map(check_subset, A))
    if False in H:
        print(False)
    else:
        print(True)
