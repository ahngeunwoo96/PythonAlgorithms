def NandM(N, cnt, answer):
    if cnt == M:
        print(" ".join(answer))
        return

    for i in range(1, N+1):
        NandM(N, cnt+1, answer + str(i))


N, M = map(int,input().split())
NandM(N, 0, "")