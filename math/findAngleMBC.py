import math

AB = int(input())
BC = int(input())
AC = math.sqrt((AB**2) + (BC**2))
MB = AC / 2
BE = BC / 2
MBC = BE / MB
print(str(int(round(math.degrees(math.acos(MBC))))) + str(chr(176)))

