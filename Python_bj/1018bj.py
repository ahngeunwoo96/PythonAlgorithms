# 210204 baekjoon 1018 체스판 다시 칠하기

n, m = map(int, input().split())
chess = []

for i in range(n):
    row = input()
    row_list = []
    for word in row:
        row_list.append(word)
    chess.append(row_list)

result = 65
for start_y in range(n-8+1):
    for start_x in range(m-8+1):
        # 왼쪽 위 칸이 흰색인 경우
        w_cnt = 0
        b_cnt = 0
        for i in range(8):
            for j in range(8):
                # i+j가 짝수인경우 흰색이어야 함
                if (i+j) % 2 == 0:
                    if chess[start_y + j][start_x + i] != 'W':
                        w_cnt += 1
                else:
                    if chess[start_y + j][start_x + i] != 'B':
                        w_cnt += 1
        
        if result > w_cnt:
            result = w_cnt

        # 왼쪽 위 칸이 검은색인 경우
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    if chess[start_y + j][start_x + i] != 'B':
                        b_cnt += 1 
                else:
                    if chess[start_y + j][start_x + i] != 'W':
                        b_cnt +=1

        if result > b_cnt:
            result = b_cnt
    
print(result)

        

