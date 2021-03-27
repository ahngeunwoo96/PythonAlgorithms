N = int(input())

# N의 제곱근을 구하기
start, end = 0, N

# 이분탐색을 이용
while True:
    mid = (start + end) // 2
    if mid ** 2 > N:
        end = mid
    elif mid ** 2 < N:
        start = mid
    else:
        break

print(mid)