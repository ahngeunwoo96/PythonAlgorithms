N = int(input())
P = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    max = 0
    for j in range(i+1):
        if max < P[i-j] + dp[j-1]:
            max = P[i-j] + dp[j-1]
    dp[i] = max

print(dp[N-1])