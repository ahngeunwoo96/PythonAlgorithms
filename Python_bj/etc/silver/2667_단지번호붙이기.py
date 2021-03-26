dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def Found(y, x):
    stack.append((y, x))

    cnt = 0
    while stack:
        y, x = stack.pop()
        m[y][x] = complex+1
        cnt += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if m[ny][nx] == 1:
                    if (ny, nx) not in stack:
                        stack.append((ny, nx))

    return cnt

N = int(input())
m = [list(map(int,list(input()))) for _ in range(N)]

complex = 0 # 단지의 수를 저장

ans = [] # 각 단지내 집의 수를 list에 저장
for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            stack = []
            complex += 1
            ans.append(Found(i, j))

ans.sort()
print(complex)
for i in range(len(ans)):
    print(ans[i])