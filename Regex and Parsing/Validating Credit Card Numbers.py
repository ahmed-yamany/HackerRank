import re


def repeated(s):
    try:
        for m in range(len(s)):
            a = s[m]
            n = 1
            for j in range(m + 1, m + 4):
                if a == s[j]:
                    a = s[j]
                    n += 1
            if n == 4:
                return False
                break

        else:
            return True
    except IndexError:
        return True


N = int(input())
for i in range(N):
    string = input()
    repl = string.replace('-', '')
    matches = re.match(r'(^(4|5|6)[0-9]{3})(-?[0-9]{4}){3}', string)
    if matches and len(repl) == 16 and repeated(repl):
        print('Valid')
    else:
        print('Invalid')
