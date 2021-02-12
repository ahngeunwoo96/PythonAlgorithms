# 210210 baekjoon 1932 정수 삼각형

n = int(input())
triangle = []
max_sum = []

for i in range(n):
    triangle.append(list(map(int, input().split())))
    max_sum.append([0] * (i + 1))

for i in range(n-2, -1, -1):
    for j in range(i):
        for k in range(2):
            if max_sum[i][j] < triangle[i][j] + triangle[i+1][j+k]:
                max_sum[i][j] = triangle[i][j] + triangle[i+1][j+k]


print(max_sum[0][0])

