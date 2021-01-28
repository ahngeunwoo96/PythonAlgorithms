# 21.01.26 SWEA 1961 숫자 배열 회전
for test_case in range(1, int(input()) + 1):
    N = int(input())
    inputMap = []

    # N * N 맵을 입력받음
    for i in range(N):
        row = list(map(int, input().split()))
        inputMap.append(row)

    result = []
    for i in range(N):
        row1, row2, row3 = [], [], []
        for j in range(N):
            # 회전하고 가로줄마다 입력을 받음 
            # 90도 회전 
            # 90도 회전을 하면 (x, y) = (0, 2) -> (0, 1) -> (0, 0) -> (1, 2) -> ...
            # 이런식으로 순서가 되기 때문에 이를 표현
            row1.append(str(inputMap[N - 1 - j][i]))
            # 180도 회전 
            row2.append(str(inputMap[N - 1 - i][N - 1 - j]))
            # 270도 회전
            row3.append(str(inputMap[j][N - 1 - i]))
        result += [''.join(row1), ''.join(row2), ''.join(row3)]

    print('#{}'.format(test_case))
    for i in range(N):
        for j in range(3):
            print(result[i * 3 + j], end = ' ')
        print()
    
    

                        

        

