import math

H, W = map(int, input().split())
if H == 1 or W == 1:
  print(1)

else:
  
  n = H // 2
  mod = 0 

  if H % 2 == 1:
    mod = math.ceil(W / 2)  

  print(W * n + mod)
