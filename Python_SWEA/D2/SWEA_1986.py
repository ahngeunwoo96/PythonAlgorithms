# 21.01.22 python 1986 지그재그 숫자 문제풀이

TC = int(input())

for test_case in range(1, TC + 1):

    N = int(input())
    sum = 0

    # N이 짝수라면
    if N % 2 == 0:
        for i in range(1, N + 1, 2):
            sum -= 1
    else:
        for i in range(1, N, 2):
            sum -= 1
        sum += N
    
    print('#{} {}'.format(test_case, sum))