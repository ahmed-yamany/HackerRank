def no_idea(array, setA, setB):
    happiness = 0
    for i in array:
        if i in setA:
            happiness += 1
        elif i in setB:
            happiness -= 1
    print(happiness)


if __name__ == '__name__':
    m = list(map(int, input().split()))
    n = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    no_idea(n, a, b)
