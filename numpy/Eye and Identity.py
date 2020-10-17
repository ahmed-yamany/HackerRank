import numpy
numpy.set_printoptions(sign=' ')
n, m = list(map(int, input().split()))
print(numpy.eye(n, m))
