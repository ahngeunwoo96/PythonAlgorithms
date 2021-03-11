N, K = map(int, input().split())
nums = list(range(1, N+1))
ans = []

cnt = 0
while nums:
    cnt = (cnt + K-1) % N
    ans.append(nums.pop(cnt))
    N -= 1

print("<", end="")
print(", ".join(map(str, ans)), end="")
print(">")