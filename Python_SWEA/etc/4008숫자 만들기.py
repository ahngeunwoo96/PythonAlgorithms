import math

def Recur(tot, cnt):
    global min_ans, max_ans

    if cnt == N-1:
        if min_ans > tot:
            min_ans = tot
        if max_ans < tot:
            max_ans = tot
        return

    for i in range(4):
        if operator[i] != 0:
            operator[i] -= 1
            if i == 0: # '+'
                Recur(tot + num[cnt+1], cnt+1)
            elif i == 1: # '-'
                Recur(tot - num[cnt+1], cnt+1)
            elif i == 2: # '*'
                Recur(tot * num[cnt+1], cnt+1)
            elif i == 3: # '//'
                Recur(int(tot / num[cnt+1]), cnt+1)
            operator[i] += 1


for tc in range(1, int(input()) + 1):
    N = int(input())
    operator = list(map(int, input().split()))
    num = list(map(int, input().split()))

    min_ans, max_ans = 100000000, -100000000
    Recur(num[0], 0)
    print(f"#{tc} {max_ans - min_ans}")