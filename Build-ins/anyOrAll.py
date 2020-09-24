n = int(input())
lst = list(map(int, input().split()))
x = True if all(list(map(lambda x: x > 0, lst))) and any(list(map(lambda x: str(x) == str(x)[::-1], lst))) else False
print(x)
