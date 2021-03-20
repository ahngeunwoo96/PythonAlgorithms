user_input = int(input())
time_list = []

for i in range(user_input):
    time = input()
    time_list.append(time)

start, end = [], []
for i in range(user_input):
    start.append([int(time_list[i][0:2]), int(time_list[i][3:5])])
    end.append([int(time_list[i][8:10]), int(time_list[i][11:13])])

max_start_hour, max_start_min, min_end_hour, min_end_min = 0, 0, 24, 60
for i in range(user_input):
    if max_start_hour < start[i][0]:
        max_start_hour = start[i][0]
        max_start_min = start[i][1]
    elif max_start_hour == start[i][0]:
        if max_start_min < start[i][1]:
            max_start_min = start[i][1]

    if min_end_hour > end[i][0]:
        min_end_hour = end[i][0]
        min_end_min = end[i][1]
    elif min_end_hour == end[i][0]:
        if min_end_min > end[i][1]:
            min_end_min = end[i][1]


# 가능한 시간 확인
if max_start_hour > min_end_hour:
    print(-1)
elif max_start_hour == min_end_hour:
    if max_start_min > min_end_min:
        print(-1)
else:
    # 분 출력
    if max_start_min < 10:
        max_start_min = '0' + str(max_start_min)

    if min_end_min < 10:
        min_end_min = '0' + str(min_end_min)

    if max_start_hour < 10:
        max_start_hour = '0' + str(max_start_hour)

    if min_end_hour < 10:
        min_end_hour = '0' + str(min_end_hour)
    print(f"{max_start_hour}:{max_start_min} ~ {min_end_hour}:{min_end_min}")

'''
3
05:00 ~ 14:30
06:40 ~ 18:30
07:20 ~ 18:00
'''