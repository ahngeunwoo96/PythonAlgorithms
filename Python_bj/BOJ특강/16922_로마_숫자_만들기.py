N = int(input())

ans = []
for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            l = N-i-j-k
            tot = i + j * 5 + k * 10 + l * 50
            ans.append(tot)

print(len(set(ans)))