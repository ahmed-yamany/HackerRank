import re

n = int(input())
lst = []
for i in range(n):
    text = input()
    lst.append(text)

for text in lst:
    m = re.sub(r'\s\|\|(?= )', ' or', text)
    print(re.sub(r'\s&&(?= )', ' and', m))
