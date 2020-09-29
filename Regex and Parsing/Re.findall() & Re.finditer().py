import re
pattern = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])+([aeoui]{2,})+(?=[qwrtypsdfghjklzxcvbnm])', input(), re.IGNORECASE)
if len(pattern) > 0:
    for i in pattern:
        print(i)
else:
    print(-1)
