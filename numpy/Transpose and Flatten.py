import numpy
n, m = numpy.array(input().split(), int)
lst = []
for i in range(n):
    array = numpy.array(input().split(), int)
    lst.append(array)
s = numpy.array(lst)
print(numpy.transpose(s))
print(s.flatten())
