# 21.01.28 SWEA 1954 달팽이 숫자
dir_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for test_case in range(1, int(input()) + 1):
    n = int(input())
    #python 2차원 배열
    snail = [[0] * n for _ in range(n)] 
    line = n - 1
    cnt = 1
    dir = 0
    y = 0
    x = 0

    for i in range(line):
        snail[y][x] = cnt
        cnt += 1
        y = y + dir_list[dir][1]
        x = x + dir_list[dir][0]
    dir += 1

    while cnt < n ** 2:
        for i in range(line):
            snail[y][x] = cnt
            cnt += 1
            y = y + dir_list[dir][1]
            x = x + dir_list[dir][0]
        dir += 1
        if dir == 4:
            dir = 0
        
        for i in range(line):
            snail[y][x] = cnt
            cnt += 1
            y = y + dir_list[dir][1]
            x = x + dir_list[dir][0]
        dir += 1
        line -= 1

    snail[y][x] = cnt

    print('#{}'.format(test_case))
    for i in snail:
        for j in i:
            print(j, end = ' ')
        print()
