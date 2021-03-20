N = int(input())
m = [[0] * 100 for _ in range(100)]
for i in range(N):
    x, y = map(int, input().split())
    for yy in range(10):
        for xx in range(10):
            m[y+yy][x+xx] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if m[i][j] == 1:
            ans += 1

print(ans)