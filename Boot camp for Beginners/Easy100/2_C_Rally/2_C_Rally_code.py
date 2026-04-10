N = int(input())
X = list(map(int, input().split()))

avg = sum(X) // N
p = [avg, avg+1]
ans = float('inf')

for i in p:
    tmp = 0
    for x in X:
        tmp += (x - i) ** 2
    ans = min(ans, tmp)



print(ans)
