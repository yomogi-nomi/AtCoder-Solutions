card = list()
for _ in range(3):
  raw = list(map(int, input().split()))
  card.append(raw)

check = list([False] * 3 for _ in range(3))

N = int(input())

for _ in range(N):
  num = int(input())
  for i in range(3):
    for j in range(3):
      if card[i][j] == num:
        check[i][j] = True

for i in range(3):
  if check[i][0] == True and check[i][1] == True and check[i][2] == True:
    print("Yes")
    exit()
for i in range(3):
  if check[0][i] == True and check[1][i] == True and check[2][i] == True:
    print("Yes")
    exit()
if check[0][0] == True and check[1][1] == True and check[2][2] == True:
  print("Yes")
  exit()
if check[0][2] == True and check[1][1] == True and check[2][0] == True:
  print("Yes")
  exit()
print("No")
