import random

N, M = map(int, input().split())
numbers = [input for i in range(1, N+1)]
answer = []

cnt = 1 # 총 갯수
for i in range(N, N-M, -1):
    cnt *= i
for i in range(1, M+1):
    cnt //= i

while len(answer) < cnt:
    tmp = random.sample(numbers, M)
    tmp.sort()
    if tmp not in answer:
        answer.append(tmp)

answer.sort()
for i in range(cnt):
    print(*answer[i])
