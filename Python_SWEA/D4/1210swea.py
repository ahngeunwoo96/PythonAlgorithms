# 210214 swea 1210 Ladder
def LadderGame(arrive):
    row = 99
    col = arrive

    while row > 0:
        # 왼쪽으로 이동
        if col != 0 and col != 99:
            if ladder[row][col - 1] == 1:
                while col - 1 >= 0 and ladder[row][col - 1] == 1:
                    col -= 1
                row -= 1
            # 오른쪽으로 이동
            elif ladder[row][col + 1] == 1:
                while col + 1 <= 99 and ladder[row][col + 1] == 1:
                    col += 1
                row -= 1
            # 위로 올라감
            else:
                row -= 1
        elif col == 0:
            if ladder[row][col + 1] == 1:
                while col + 1 <= 99 and ladder[row][col + 1] == 1:
                    col += 1
                row -= 1
            # 위로 올라감
            else:
                row -= 1
        else:
            # 왼쪽으로 이동
            if ladder[row][col - 1] == 1:
                while col - 1 >= 0 and ladder[row][col - 1] == 1:
                    col -= 1
                row -= 1
            else:
                row -= 1
    return col




for _ in range(1, 11):
    tc = int(input())
    ladder = []
    for i in range(100):
        row = list(map(int, input().split()))
        ladder.append(row)

    for i in range(100):
        if ladder[99][i] == 2:
            arrive = i

    print(f"#{tc} " + str(LadderGame(arrive)))
