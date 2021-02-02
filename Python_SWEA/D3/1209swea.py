# 21.02.02 swea 1209 2일차 - Sum

for test_case in range(1, 11):
    tc = int(input())
    array = []
    for i in range(100):
        row = list(map(int, input().split()))
        array.append(row)

    max = 0
    rd_sum, ld_sum = 0, 0
    for i in range(100):
        row_sum, col_sum = 0, 0
        for j in range(100):
            row_sum += array[i][j]
            col_sum += array[j][i]
        
        if row_sum > max:
            max = row_sum
        
        if col_sum > max:
            max = col_sum

        rd_sum += array[i][i]
        ld_sum += array[99 - i][i]
    
    if rd_sum > max:
        max = rd_sum

    if ld_sum > max:
        max = ld_sum

    print("#{} {}".format(test_case, max))

        