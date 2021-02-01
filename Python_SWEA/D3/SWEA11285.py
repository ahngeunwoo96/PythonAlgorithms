#21.02.01 SWEA 11285 다트 게임
import math

for test_case in range(1, int(input()) + 1):
    n = int(input())
    darts = []
    
    for i in range(n):
        x, y = map(int, input().split())
        darts.append((x, y))
    result = 0

    for dart in darts:
        dis = math.sqrt(dart[0] ** 2 + dart[1] ** 2)
        result += (220-dis) // 20

    print("#{} {:d}".format(test_case, int(result)))