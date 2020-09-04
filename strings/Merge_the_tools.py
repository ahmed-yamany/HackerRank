def merge_the_tools(string, k):

    n = len(string)
    i = 0
    t = []
    while i < n:
        t.append(string[i:i + k])
        i += k

    print(t)
    for i in t:
        print("".join(dict.fromkeys(i)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
