import numpy

n, m, p = numpy.array(input().split(), int)
lst1 = numpy.array([list(map(int, input().split())) for i in range(n)])
lst2 = numpy.array([list(map(int, input().split())) for j in range(m)])


print(numpy.concatenate((lst1, lst2), axis=0))
