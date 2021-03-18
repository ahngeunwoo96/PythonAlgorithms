X = int(input())

ans = 0
for j in range(7):
    if X & (1<<j):
        ans += 1

print(ans)