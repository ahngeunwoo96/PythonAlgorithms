# 210208 baekjoon 9663 N-Queen

n = int(input())
chess = [[0] * n for i in range(n)]
ck_col = [0] * n
ck_dig = [0] * (2 * n - 1)
ck_dig2 = [0] * (2 * n - 1)

# N * N에 N개의 queen을 놓는 방법
# 가로, 세로, 대각선에 퀸이 1개씩만 놓여있어야 함
def IsOkayQueen(row, col):
    if ck_col[col] == 1:
        return False
    if ck_dig[row+col] == 1:
        return False
    if ck_dig[n-1-row+col] == 1:
        return False

    return True


def Queen(row):
    global result

    if row == n:
        return 1

    result = 0
    for i in range(n):
        if IsOkayQueen(row, i):
            ck_col[i] = 1
            ck_dig[row+i] = 1
            ck_dig2[n-1-row+i] = 1
            result += Queen(row + 1)
            ck_col[i] = 0
            ck_dig[row+i] = 0
            ck_dig2[n-1-row+i] = 0

    return result


print(Queen(0))