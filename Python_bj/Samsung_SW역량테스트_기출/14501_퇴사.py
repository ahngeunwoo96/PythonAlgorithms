def DFS(idx, income):
    global ans

    if idx == N:
        if ans < income:
            ans = income
        return

    T = counselings[idx][0]
    P = counselings[idx][1]
    # 해당 날짜의 상담을 받지 않는 경우
    DFS(idx+1, income)
    # 해당 날짜의 상담을 받는 경우
    if idx+T <= N:
        DFS(idx+T, income+P)


N = int(input())
counselings = [list(map(int, input().split())) for _ in range(N)]

ans = 0
DFS(0, 0)
print(ans)