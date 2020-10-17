import numpy
n, m = list(map(int, input().split()))
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

lst = numpy.array(lst)
array = numpy.min(lst, axis=1)
print(numpy.max(array))