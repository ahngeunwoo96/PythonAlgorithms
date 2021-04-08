from copy import deepcopy

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def SpreadBirus(r, c, m, birus_m):
    q = []
    q.append((r, c))

    while q:
        r, c = q.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if birus_m[nr][nc] == 0:
                    birus_m[nr][nc] = 2
                    q.append((nr, nc))

    return birus_m

def BuildWall(row, col, cnt):
    global ans
    if cnt == 3:
        # DFS 방법으로 3개의 벽을 세움
        # 바이러스를 퍼트리기
        birus_m = deepcopy(m)
        for r in range(N):
            for c in range(M):
                if m[r][c] == 2:
                    birus_m = SpreadBirus(r, c, m, birus_m)

        temp = 0
        for i in range(N):
            for j in range(M):
                if birus_m[i][j] == 0:
                    temp += 1
        ans = max(temp, ans)

        return

    for r in range(row, N):
        for c in range(col, M):
            if m[r][c] == 0:
                m[r][c] = 1
                BuildWall(r, c+1, cnt+1)
                m[r][c] = 0
        col = 0

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]

ans = 0
BuildWall(0, 0, 0)
print(ans)