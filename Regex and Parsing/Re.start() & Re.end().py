import re
S = input()
K = input()
pattern = re.compile(K)
matches = pattern.search(S)
if not matches:
    print((-1, -1))

while matches:
    print((matches.start(), matches.end()-1))
    matches = pattern.search(S, matches.start()+1)

