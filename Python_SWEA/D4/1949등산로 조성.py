dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def DFS(y, x, cnt, cut):
    global ans

    flag = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                # 더 낮은 등산로로 이동
                if m[y][x] > m[ny][nx]:
                    DFS(ny, nx, cnt+1, cut)
                # 깍아서 이동
                elif m[ny][nx] - m[y][x] < K and cut == 1:
                    tmp = m[ny][nx]
                    m[ny][nx] = m[y][x] - 1
                    DFS(ny, nx, cnt+1, 0)
                    m[ny][nx] = tmp
                else:
                    flag += 1
                visited[ny][nx] = 0
            else:
                flag += 1
        else:
            flag += 1

    if flag == 4:
        if ans < cnt:
            ans = cnt
        return


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = 0

    Max = 0
    for i in range(N):
        for j in range(N):
            if Max < m[i][j]:
                Max = m[i][j]

    for i in range(N):
        for j in range(N):
            if Max == m[i][j]:
                visited[i][j] = 1
                DFS(i, j, 1, 1)
                visited[i][j] = 0

    print(f"#{tc} {ans}")