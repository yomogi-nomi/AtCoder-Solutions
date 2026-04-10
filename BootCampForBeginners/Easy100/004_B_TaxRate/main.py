x = int(input())

a = int(x // 1.08)

p = [a, a+1]

for i in p:
  if int(i*1.08) == x:
    print(i)
    exit()
  
print(":(")
  
