def average(array):
    # your code goes here
    print(sum(array))
    return sum(set(array)) / len(set(array))


if __name__ == '__main__':
    # n = int(input())
    # arr = list(map(int, input().split()))
    result = average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174])
    print(result)
