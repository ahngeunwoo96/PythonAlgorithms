# 21.01.31 baekjoon 11651 좌표 정렬하기2

n = int(input())
xy_list = []

for i in range(n):
    x, y = map(int, input().split())
    xy_list.append((x, y))

sorted_xy = sorted(xy_list, key= lambda x: (x[1], x[0]))

for i in sorted_xy:
    print('{} {}'.format(i[0], i[1]))

