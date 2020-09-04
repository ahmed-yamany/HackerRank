def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if string[i] not in vowels:
            stuart += len(string) - i
        else:
            kevin += len(string) - i

    if stuart > kevin:
        print("Stuart {}".format(stuart))
    elif stuart < kevin:
        print("Kevin {}".format(kevin))
    else:
        print("Draw")


if __name__ == '__main__':
    # s = input()
    minion_game('BANANA')
