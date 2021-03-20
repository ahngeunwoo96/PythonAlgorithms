def DFS(cnt):
    global ans

    if road[cnt] == '0':
        return

    if cnt == n-1:
        ans += 1
        return

    DFS(cnt+1)
    if cnt < n-2:
        DFS(cnt+2)


n = int(input())
road = list(input())
ans = 0
DFS(0)
print(ans)