import itertools 

A = input()
groups = [[], []]
for k, g in itertools.groupby(A):
    groups[1].append(eval(k))      # Store group iterator as a list
    groups[0].append(len(list(g)))      # Store group iterator as a list

result = list(zip(groups[0], groups[1]))


for i in result:
    print(i, end=' ') 
