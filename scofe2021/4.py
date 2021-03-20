dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def Move(y, x, cnt):
    global ans
    if y == M-1: # 도착
        if ans > cnt:
            ans = cnt
        return

    if ans < cnt:
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < M and 0 <= nx < N:
            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if m[ny][nx] == "." and (i == 1 or i == 3):
                    Move(ny, nx, cnt+1)
                elif m[ny][nx] == "." and (i == 0 or i == 2):
                    Move(ny, nx, cnt)
                visited[ny][nx] = 0


N, M = map(int, input().split())
m = [list(input()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
ans = 20

for i in range(M):
    for j in range(N):
        if m[i][j] == "c":
            visited[i][j] = 1
            Move(i, j, 0)
            visited[i][j] = 0


if ans == 20:
    print(-1)
else:
    print(ans)

'''
4 6
cxxc
.xx.
....
xx.x
...x
.xxx
'''