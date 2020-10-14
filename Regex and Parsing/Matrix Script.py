import re
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

string = ''
for i in range(m):
    for j in range(n):
        string += matrix[j][i]

matches = re.sub(r'(?<=\w)\W+(?=\w)', ' ', string)
print(matches)
