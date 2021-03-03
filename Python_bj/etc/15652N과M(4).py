def NandM(s, cnt, answer):
    if cnt == M:
        print(" ".join(answer))
        return

    for i in range(s, N+1):
        NandM(i, cnt+1, answer + str(i))

N, M = map(int, input().split())
NandM(1, 0, "")