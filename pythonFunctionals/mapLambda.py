cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    lst = []
    a = 0
    b = 1
    if n == 0:
        return []
    elif n == 1:
        lst.append(a)
    else:
        lst = [0, 1]
        for i in range(2, n):
            c = a + b
            a, b = b, c
            lst.append(b)
    return lst


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
