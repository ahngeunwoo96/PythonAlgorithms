# 21.01.29 SWEA 11315 오목 판정 

for test_case in range(1, int(input()) + 1):
    n = int(input())
    pan = [[0] * n for i in range(n)]
    result = 'NO'

    for i in range(n):
        row = input()
        for j in range(len(row)):
            pan[i][j] = row[j]

    for i in range(n):
        cnt = 0
        for j in range(n):
            if pan[i][j] == '.':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 5:
                    result = 'YES'
                    break

    for i in range(n):
        cnt = 0
        for j in range(n):
            if pan[j][i] == '.':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 5:
                    result = 'YES'
                    break
        
    cnt = 0
    for i in range(n):
        if pan[i][i] == '.':
            cnt = 0
        else:
            cnt += 1
            if cnt >= 5:
                result = 'YES'
                break

    cnt = 0
    for i in range(n):
        if pan[i][n-1-i] == '.':
            cnt = 0
        else:
            cnt += 1
            if cnt >= 5:
                result = 'YES'
                break

    print('#{} {}'.format(test_case, result))