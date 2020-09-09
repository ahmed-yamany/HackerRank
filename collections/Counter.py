#
# X = int(input())
# shoe_size = list(map(int, input().split()))
# N = int(input())
# A = []
# for i in range(N):
#     x = list(map(int, input().split()))
#     if x[0] in shoe_size:
#         A.append(x[1])
#
#
# A = list(set(A))
#
# print(sum(A))
from collections import Counter
X = int(input())
shoe_size = list(map(int, input().split()))

lst = []

for i in range(int(input())):
    lst.append(tuple(map(int, input().split())))
N = 0
for i, s in lst:
    if i in shoe_size:
        N += s
        shoe_size.remove(i)

print(N)
