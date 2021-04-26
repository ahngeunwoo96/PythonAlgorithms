dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def Sitting(idx, like):
    max_likes, max_empty = 0, 0
    max_r, max_c = 0, 0
    for r in range(N):
        for c in range(N):
            # 비어있는 칸이라면 들어갈 칸인지 비교
            if sit[r][c] == 0:
                likes = 0 # 인접한 칸에서 좋아하는 사람의 수
                empty = 0 # 인접한 칸에서 비어있는 칸의 수
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        if sit[nr][nc] in like:
                            likes += 1
                        if sit[nr][nc] == 0:
                            empty += 1

                if max_likes < likes:
                    max_likes = likes
                    max_empty = empty
                    max_r, max_c = r, c
                if max_likes == likes:
                    if max_empty < empty:
                        max_empty = empty
                        max_r, max_c = r, c

    sit[max_r][max_c] = idx

N = int(input())
like = [[] for _ in range(N ** 2 + 1)]
sit = [[0] * N for _ in range(N)]

# 자리에 앉히기
for i in range(N ** 2):
    data = list(map(int, input().split()))
    Sitting(data[0], data[1:])
    like[data[0]] += data[1:]

# 만족도 구하기
ans = 0
for r in range(N):
    for c in range(N):
        cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if sit[nr][nc] in like[sit[r][c]]:
                    cnt += 1
        if cnt == 0:
            ans += 1
        else:
            ans += 10 ** (cnt-1)

print(ans)