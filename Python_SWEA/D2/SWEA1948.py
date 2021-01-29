# 21.01.29 SWEA 1948 날짜 계산기
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1, int(input()) + 1):
    mon1, day1, mon2, day2 = map(int, input().split())
    
    result = 0
    for i in range(mon1-1, mon2-1):
        result += days[i]

    result = result - day1 + day2 + 1 
    print('#{} {}'.format(test_case, result))