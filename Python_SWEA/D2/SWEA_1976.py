# 21.01.25 SWEA 1976 시각 덧셈

TC = int(input())

for test_case in range(1, TC + 1):

    f_hour, f_minute, s_hour, s_minute = map(int, input().split())

    minute = f_minute + s_minute

    if minute >= 60:
        minute -= 60
        hour = 1
    else:
        hour = 0
    
    hour += f_hour + s_hour
    if hour >= 12:
        hour -= 12
        
    print("#{} {} {}".format(test_case, hour, minute))