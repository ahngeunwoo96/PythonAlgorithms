numbers = [list(map(int, input().split())) for _ in range(9)]

Max = 0
for i in range(9):
    for j in range(9):
        if Max < numbers[i][j]:
            Max = numbers[i][j]
            col = i+1
            row = j+1

print(Max)
print(col, row)