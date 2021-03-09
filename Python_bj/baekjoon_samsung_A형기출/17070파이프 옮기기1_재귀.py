
def MovePipe(y, x, dir):
    global ans

    if y == N-1 and x == N-1:
        ans += 1
        return

    if dir != 1: # 퍼이프의 모양이 세로가 아니면 가로로 이동
        if x+1 < N:
            if m[y][x+1] == 0:
                MovePipe(y, x+1, 0)

    if dir != 0: # 파이프의 모양이 가로가 아니면 세로로 이동
        if y+1 < N:
            if m[y+1][x] == 0:
                MovePipe(y+1, x, 1)

    if y+1 < N and x+1 < N: # 대각선으로 이동
        if m[y+1][x] == m[y][x+1] == m[y+1][x+1] == 0:
            MovePipe(y+1, x+1, 2)

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
ans = 0
MovePipe(0, 1, 0)
print(ans)