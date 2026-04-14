import math
a, b =input().split()

sum = int(a+b)

ans = math.isqrt(sum)

if ans**2 == sum:
  print("Yes")
else:
  print("No")
