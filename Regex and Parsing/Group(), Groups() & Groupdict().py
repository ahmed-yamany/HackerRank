import re
S = input()
pattern = re.search(r'([a-zA-Z0-9])\1+', S)
if pattern:
    print(pattern.group(1))
else:
    print(-1)
