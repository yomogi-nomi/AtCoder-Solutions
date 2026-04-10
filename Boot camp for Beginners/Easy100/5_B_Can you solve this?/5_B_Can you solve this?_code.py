n, m, c = map(int, input().split())

b = list(map(int, input().split()))

count = 0

for i in range(n):
  a = list(map(int, input().split()))
  count += (sum(a[i]*b[i]for i in range(m)) + c) > 0
  
print(count)
