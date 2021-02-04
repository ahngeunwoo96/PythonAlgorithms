# 210204 swea 1220 5일차-magnetic

for test_case in range(1, 11):
    n = int(input())
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            # n극 아래로 움직임
            if table[i][j] == 1 and i != 99 and table[i+1][j] != 2:
                table[i][j] = 0
                table[i+1][j] = 1
            # s극 위로 움직임
            elif table[i][j] == 2 and i != 0 and table[i-1][j] != 1:
                table[i][j] = 0
                table[i-1][j] = 2
    
    result = 0
    for i in range(n):
        for j in range(n-1):
            if table[j][i] == 1 and table[j+1][i] == 2:
                result += 1
        
    print(f"#{test_case} {result}")