from collections import Counter

S = input()
d = Counter(S).most_common()
d = sorted(d, key=lambda x: (x[1] * -1, x[0]))  # it arranges it alphabetically
for i in range(3):
    print(d[i][0], d[i][1])

