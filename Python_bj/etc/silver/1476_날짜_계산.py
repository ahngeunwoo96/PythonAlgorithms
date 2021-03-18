E, S, M = map(int, input().split())

# E: 15, S: 28, M: 19
n = 0
ans = 0
while True:
    num = n * 15 + E
    if num % 28 == S % 28:
        if num % 19 == M % 19:
            ans = num
            break
    n += 1

print(ans)
