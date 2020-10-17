import numpy
n, m = list(map(int, input().split()))
lst1 = []
for i in range(n):
    array = numpy.array(input().split(), int)
    lst1.append(array)

lst1 = numpy.array(lst1, int)

lst2 = []
for i in range(n):
    array = numpy.array(input().split(), int)
    lst2.append(array)

lst2 = numpy.array(lst2, int)

print(lst1 + lst2)
print(lst1 - lst2)
print(lst1 * lst2)
lst = lst1 / lst2
print(numpy.int_(lst))
print(lst1 % lst2)
print(lst1 ** lst2)
