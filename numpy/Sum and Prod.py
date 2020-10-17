import numpy
n, m = list(map(int, input().split()))
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

lst = numpy.array(lst)
array = numpy.sum(lst, axis=0)
print(numpy.prod(array))
