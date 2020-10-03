import re
n = int(input())
for i in range(n):
    phone_num = input()
    m = re.match(r'^[987]\d\d\d\d\d\d\d\d\d', phone_num)
    if m and len(phone_num) == 10:
        print('YES')
    else:
        print('NO')
