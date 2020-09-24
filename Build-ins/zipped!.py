from collections import defaultdict
d = defaultdict(list)
lst = list()
n = list(map(int, input().split()))
for i in range(n[1]):
    student = list(map(float, input().split()))
    for j, f in enumerate(student):
        d[j].append(f)

for i in d.values():
    print(sum(i)/len(i))



