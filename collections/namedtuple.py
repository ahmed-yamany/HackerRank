N = int(input())
columns = input().split()
marks = 0
for i in range(N):
    S = input().split()
    marks += eval(S[columns.index("MARKS")])

print(marks/N)
