dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def Move(r, c, cnt, bridge_cnt):
    global ans
    # N번 섬까지 이동한 경우, ans보다 다리의 갯수가 적은 경우 저장
    if cnt == land_cnt:
        ans = min(ans, bridge_cnt)
        return

    # 자신과 같은 땅이라면, 모든 방향으로 탐색 가능
    # 현재 좌표에서 네방향 탐색
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        while 0 <= nr < N and 0 <= nc < M:
            # 바다라면 bridge_cnt를 증가
            if num_m[nr][nc] == 0:

            nr += dr[i]
            nc += dc[i]

def BFS(r, c, cnt):
    q = []
    q.append((r, c))
    num_m[r][c] = cnt

    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if m[nr][nc] == 1 and num_m[nr][nc] == 0:
                    num_m[nr][nc] = cnt
                    q.append((nr, nc))

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)] # 입력받은 map을 저장할 변
num_m = [[0] * M for _ in range(N)] # 땅에 1~N까지 번호를 붙여서 저장할 map

# 1~N번까지의 섬으로 땅을 변경
land_cnt = 1
for i in range(N):
    for j in range(M):
        if m[i][j] == 1 and num_m[i][j] == 0:
            BFS(i, j, land_cnt)
            land_cnt += 1

# 1번 섬부터 시작해서 N번 섬까지 이동
# DFS 방법을 이용
ans = 1000
passed_island = []
for i in range(N):
    for j in range(M):
        if m[i][j] == 1:

            Move(i, j, 1, 1)

print(ans)
