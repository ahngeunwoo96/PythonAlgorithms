for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    ans = 1
    for i in range(max(N, M), max(N, M)-min(N,M), -1):
        ans *= i
    for i in range(1, min(N, M)+1):
        ans //= i
    print(ans)