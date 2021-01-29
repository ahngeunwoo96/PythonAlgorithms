# 21.01.29 SWEA 1285 아름이의 돌 던지기

for test_case in range(1, int(input()) + 1):
    n = int(input())
    result = list(map(int, input().split()))
    cnt = 0
    min = 100001
    for dis in result:
        if min > abs(dis):
            min = abs(dis)
            cnt = 1
        elif min == abs(dis):
            cnt += 1
    print('#{} {} {}'.format(test_case, min, cnt))