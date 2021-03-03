import sys

n = int(input())
answer = [0] * 100001

for i in range(n):
    answer[int(sys.stdin.readline())] += 1

for i in range(100001):
    for j in range(answer[i]):
        print(i)

# 처음엔 n만큼 숫자를 입력받아 이를 정렬하여 출력했다.
# 하지만 메모리 부족 결과를 받고 문제의 메모리 제한이 8MB인것을 확인
# 숫자가 들어오면 해당 index의 list의 값을 1 증가시키도록 했다.