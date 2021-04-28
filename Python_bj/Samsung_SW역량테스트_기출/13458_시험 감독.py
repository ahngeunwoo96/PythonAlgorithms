N = int(input())
nums = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0
for num in nums:
    # 총감독관
    num -= B
    if num < 0:
        num = 0
    ans += 1
    # 부감독관
    ans += num // C
    if num % C:
        ans += 1

print(ans)
