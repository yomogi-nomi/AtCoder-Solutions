N = int(input())
B = int(input())
x = map(int, input().split())

ans = 0
for i in x:
  ans+=min(i, abs(B-i))
  
print(ans*2)
