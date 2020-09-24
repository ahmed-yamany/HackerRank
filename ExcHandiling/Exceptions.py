t = int(input())
for i in range(t):
    x, y = input().split()
    try:
        print(int(x) // int(y))
    except Exception as e:
        print('Error Code:', str(e))
