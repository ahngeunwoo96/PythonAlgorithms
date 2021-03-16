M = int(input())
N = int(input())

ans = []
for i in range(M, N+1):
    for a in range(2, i // 2 + 1):
        if i % a == 0:
            break
    else:
        if i != 1:
            ans.append(i)
if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)