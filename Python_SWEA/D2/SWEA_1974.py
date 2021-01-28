# 21.01.26 SWEA 1974 스도쿠 검증 

for test_case in range(1, int(input()) + 1):

    answer = 1
    sudoku = []
    # 2차원 배열로 sudoku를 입력받음
    for i in range(9):
        sudoku += [list(map(int, input().split()))]

    # 3 * 3 격자 확인
    for yy in range(3):
        for xx in range(3):
            result = 45
            for y in range(3):
                for x in range(3):
                    result -= sudoku[yy * 3 + y][xx * 3 + x]
            
            if not result == 0:
                answer = 0
                break
    
    for y in range(9):
        result = 45
        for x in range(9):
            result -= sudoku[y][x]
        
        if not result == 0:
            answer = 0
            break
    
    for x in range(9):
        result = 45
        for y in range(9):
            result -= sudoku[y][x]
        
        if not result == 0:
            answer = 0
            break

    print('#{} {}'.format(test_case, answer))

