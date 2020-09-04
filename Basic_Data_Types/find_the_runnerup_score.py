if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    arr = list(arr)
    arr.remove(max(arr))
    print(max(arr))