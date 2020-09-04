 
import itertools 

A = input().split()

b = list(itertools.combinations(A,2))
E = 0
for i in b:
    if 'a' in i:
        E += 1

sample_space = len(b)
probabilty = E / sample_space
print(probabilty)
