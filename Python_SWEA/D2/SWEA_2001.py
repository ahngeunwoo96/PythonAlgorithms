# 21.1.22 python 2001 파리 퇴치 

TC = int(input())

for test_case in range(1, TC + 1):

    N, M = map(int, input().split())
    fly = []

    for i in range(N):
        inputNum = map(int, input().split())
        temp_list = []
        for j in inputNum:
            temp_list += [j]
        fly += [temp_list]
    
    answer = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum = 0
            for a in range(M):
                for b in range(M):
                    sum += fly[i + a][j + b]
            if sum > answer:
                answer = sum

    print('#{} {}'.format(test_case, answer))
    