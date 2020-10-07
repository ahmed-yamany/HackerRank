import re

N = int(input())
true = False
for i in range(N):
    S = input()
    if '{' in S:
        true = True
    elif '}' in S:
        true = False
    elif true:
        matches = re.finditer(r'#[a-fA-F0-9]{3,6}', S)
        for mate in matches:
            print(mate.group())
