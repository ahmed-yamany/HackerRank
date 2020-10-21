def wrapper(f):
    def fun(l):
        lst = []
        for i in l:
            if len(i) >= 10:
                m = i[::-1]
                m = m[:10]
                m = m[::-1]
                lst.append('+91 ' + m[:5] + ' ' + m[5:])

        return f(lst)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
