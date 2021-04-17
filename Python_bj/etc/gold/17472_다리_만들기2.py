dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 1. 각 섬을 labeling
# 2. 각 섬을 연결하는 최소거리를 구함
# 3. 각 섬끼리의 최소거리를 토대로 섬과 섬을 연결해서, 모든 섬이 연결되면 최소거리의 합을 반환하고 연결되지 않으면 -1을 반환

# 섬정보를 변경하기
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

# 다른 섬과의 최소 거리를 구하기
def get_distance(r, c, idx):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        count = 0
        while True:
            # 범위 밖으로 나가면
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                break
            # 자기 자신과 만나도
            if num_m[nr][nc] == idx:
                break
            # 바다인 경우에는 해당 방향으로 계속 움직이기
            if num_m[nr][nc] == 0:
                nr += dr[i]
                nc += dc[i]
                count += 1
                continue

            # 만약 거리가 2보다 짧은 경우
            if count < 2:
                break

            # 섬끼리의 거리가 없었던 경우
            if distances[idx-1][num_m[nr][nc]-1] == 0:
                distances[idx-1][num_m[nr][nc]-1] = count
            # 이전에 섬까지의 거리가 있었던 경우
            else:
                if distances[idx-1][num_m[nr][nc]-1] > count:
                    distances[idx-1][num_m[nr][nc]-1] = count
            break

# 부모의 정보를 가져오기
def getParent(idx):
    if parent[idx] == idx:
        return idx
    parent[idx] = getParent(parent[idx])
    return parent[idx]

# 부모를 병합
def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 부모가 같은지 확인
def find(a, b):
    a = getParent(a)
    b = getParent(b)
    return a == b

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)] # 입력받은 map을 저장할 변수
num_m = [[0] * M for _ in range(N)] # 땅에 1~N까지 번호를 붙여서 저장할 map

# 1~N번까지 섬을 labeling 하기
land_cnt = 1
for i in range(N):
    for j in range(M):
        if m[i][j] == 1 and num_m[i][j] == 0:
            BFS(i, j, land_cnt)
            land_cnt += 1

distances = [[0] * (land_cnt-1) for _ in range(land_cnt-1)] # 섬끼리의 이동거리를 저장할 배열
parent = [i for i in range(land_cnt-1)] # 부모 노드 확인

# 섬끼리의 최소 거리를 구하기
for i in range(N):
    for j in range(M):
        if num_m[i][j]:
            get_distance(i, j, num_m[i][j])

costs = [] # 노드 연결
# 데이터 구조 변경
for i in range(land_cnt-1):
    for j in range(land_cnt-1):
        if distances[i][j] and [i, j, distances[i][j]] not in costs:
            costs.append([i, j, distances[i][j]])

costs.sort(key= lambda x: x[2])

ans = 0 # 최단 거리
# 거리를 계산하고 부모노드 병합
for cost in costs:
    if not find(cost[0], cost[1]):
        ans += cost[2]
        unionParent(cost[0], cost[1])

# 모든 섬이 연결되었는지 확인
for i in range(land_cnt-1):
    if getParent(i) != 0:
        ans = -1
        break

print(ans)


'''
8 8
0 0 0 1 1 1 1 0
0 1 1 1 1 0 1 0
0 1 0 1 1 1 0 0
0 1 0 0 0 1 0 0
0 0 0 1 0 0 1 0
0 0 0 0 0 1 0 0
0 1 1 1 0 0 0 0
0 1 0 0 0 1 0 0
'''