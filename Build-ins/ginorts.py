string = input()
upper = []
alpha = []
num = []
odd = []
even = []
for i in string:
    if i.isupper():
        upper.append(i)
    elif i.isalpha():
        alpha.append(i)
    elif i.isdigit():
        num.append(i)

for i in num:
    if int(i) % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

upper.sort()
alpha.sort()
odd.sort()
even.sort()
print(''.join(alpha) + ''.join(upper) + ''.join(odd) + ''.join(even))
