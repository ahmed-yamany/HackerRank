from collections import defaultdict

d = defaultdict(list)
n = int(input())
for i in range(n):
    text = input()
    d[text].append(1)
print(len(d))
for i in d.values():
    print(sum(i), end=' ')
