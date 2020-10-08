import re


def check(text):
    upper = []
    digit = []
    for i in text:
        if text.count(i) > 1:
            return False

        if i.isupper():
            upper.append(i)
        elif i.isdecimal():
            digit.append(i)

    matches = re.search(r'[a-zA-Z0-9]', text)
    if matches and len(text) == 10 and len(upper) >=2 and len(digit)>=3:
        return True

N = int(input())
for i in range(N):
    S = input()
    if check(S):
        print('Valid')
    else:
        print('Invalid')
