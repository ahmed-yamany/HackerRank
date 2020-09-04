# one line of input containing 0 < N < 27, the size of the rangoli
# size 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

def Rangoli(size):
    string = ''
    for i in range(1, size + 1):
        x = 65 + (size - 1)
        string = string + '-' * (size - i) * 2
        for j in range(i):
            string = string + str(chr(x).lower())
            string = string + '-'
            x = x - 1

        if i >= 2:
            x = 66 + (size - i)
            for j in range(i - 1):
                string = string + str(chr(x).lower())
                string = string + '-'
                x = x + 1

        string = string[:-1]

        string = string + '-' * ((size - i) * 2)
        string = string + '\n'

    # print(string)
    # string = ''
    for i in range(1, size):
        x = 66 + (size - 2)
        string += '-' * (i * 2)
        for j in range(size - i):
            string += str(chr(x).lower())
            string += '-'
            x = x - 1
        x = 66 + i
        for j in range(size - i):
            string = string + str(chr(x).lower())
            string = string + '-'
            x = x + 1

        string = string[:-2]
        string = string + '-' * (i * 2 - 1)

        string += '\n'

    print(string)


if __name__ == '__main__':
    number = int(input())
    Rangoli(number)
