base = [list(map(int, input().split())) for _ in range(10)]

def CP(i, j):
    for d in range(4, 0, -1):
        for xx in range(d):
            for yy in range(d):
                if base[i + yy][j + xx] != 1:



for i in range(10):
    for j in range(10):
        if base[i][j] == 1:
            CP(i, j)


