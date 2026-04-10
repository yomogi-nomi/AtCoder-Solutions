N, A, B = map(int, input().split())
S = input()

count_A = 0
count_B = 0

for i in range(N):
    if (A+B > count_A+count_B):
        if S[i] == 'a':
            count_A += 1
            print('Yes')
        elif S[i] == 'b' and (count_B < B):
            count_B += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')
        
        
