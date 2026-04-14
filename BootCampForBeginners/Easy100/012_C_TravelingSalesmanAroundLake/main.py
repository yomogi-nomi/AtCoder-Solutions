# 読み込み
k, N = map(int, input().split())
a = list(map(int, input().split()))

b = []

# 0時から近い家から差を取る(最後を除く)
for i in range(N-1):
  b.append(a[i+1]- a[i])
  
# 湖の大きさに注意し0時を跨ぐ距離を別途計算
b.append(k+a[0]-a[-1])

# 開始地点は最長の距離を除けばよい
b.sort()
print(sum(b)- b[-1])
