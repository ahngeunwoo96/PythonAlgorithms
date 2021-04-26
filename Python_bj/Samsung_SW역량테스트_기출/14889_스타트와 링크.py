def DivideTeam(idx, Team):
    global ans
    if idx == N:
        # 두 팀의 능력치 차이 구하기
        diff = 0
        for i in range(N//2-1):
            for j in range(i+1, N//2):
                diff += S[Team[0][i]][Team[0][j]] + S[Team[0][j]][Team[0][i]]

        for i in range(N//2-1):
            for j in range(i+1, N//2):
                diff -= S[Team[1][i]][Team[1][j]] + S[Team[1][j]][Team[1][i]]

        diff = abs(diff)
        if ans > diff:
            ans = diff
        return

    if len(Team[0]) < N//2:
        Team[0].append(idx)
        DivideTeam(idx+1, Team)
        Team[0].remove(idx)

    if len(Team[1]) < N//2:
        Team[1].append(idx)
        DivideTeam(idx+1, Team)
        Team[1].remove(idx)

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

ans = 10000
# 두 팀으로 나누기
DivideTeam(0, [[], []])
print(ans)