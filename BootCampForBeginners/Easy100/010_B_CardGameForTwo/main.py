N = int(input())
cards = list(map(int, input().split()))
sum_A = 0
sum_B = 0

cards.sort(reverse=True)

for i in range(0, N-1, 2):
  sum_A += cards[i]
  sum_B += cards[i+1]

if N%2 != 0:
  sum_A += cards[-1]

diff = sum_A - sum_B
print(diff)
