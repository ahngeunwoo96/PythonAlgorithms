# 21.01.22 python 1984 중간 평균값 구하기 문제풀이

TC = int(input())

for test_case in range(1, TC + 1):

    num = list(map(int, input().split()))
    sorted_num = sorted(num)

    sum = 0
    for i in range(1, len(sorted_num) - 1):
        sum += sorted_num[i]
    
    print('#{} {:.0f}'.format(test_case, sum / (len(num) - 2)))
