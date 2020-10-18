import numpy
numpy.set_printoptions(legacy='1.13')
n, m = list(map(int, input().split()))
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

lst = numpy.array(lst)
print(numpy.mean(lst, axis=1))
print(numpy.var(lst, axis=0))
print(numpy.std(lst))