import re
import email.utils

n = int(input())


def check(email):
    m = re.match(r'<[a-z][a-zA-Z0-9\_\.\+\-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>', email)
    return m


for i in range(n):
    x, z = input().split()
    result = check(z)
    if result:
        print(x, z)
