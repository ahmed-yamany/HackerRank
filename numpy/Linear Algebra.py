import numpy
n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(float, input().split())))

print(round(numpy.linalg.det(lst), 2))
