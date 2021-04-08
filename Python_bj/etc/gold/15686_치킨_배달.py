def DFS(row, col, cnt):
    global ans
    # 치킨집의 개수가 M개가 되었을 때
    if cnt == M:
        # 집과 치킨집과의 거리를 거리를 재기
        dis = 0
        for i in range(N):
            for j in range(N):
                if cities[i][j] == 1:
                    # 치킨집과의 최소 거리
                    temp_dis = 100
                    for r, c in chickens:
                        temp = abs(r-i) + abs(c-j)
                        temp_dis = min(temp, temp_dis)
                    dis += temp_dis

        ans = min(ans, dis)

        return

    for r in range(row, N):
        for c in range(col, N):
            if cities[r][c] == 2:
                cities[r][c] = 0
                chickens.remove((r, c))
                DFS(r, c, cnt-1)
                cities[r][c] = 2
                chickens.append((r, c))
        col = 0

N, M = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]

# 도시의 치킨집의 개수를 세기
cnt = 0
chickens = []
for i in range(N):
    for j in range(N):
        if cities[i][j] == 2:
            chickens.append((i, j))
            cnt += 1

ans = 999999999
# 치킨집의 개수가 M이 될때까지 DFS 방식으로 치킨집의 개수를 줄이기
DFS(0, 0, cnt)
print(ans)