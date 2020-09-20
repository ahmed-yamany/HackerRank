import calendar
n = list(map(int, input().split()))

print(calendar.day_name[calendar.weekday(n[2], n[0], n[1])].upper())
