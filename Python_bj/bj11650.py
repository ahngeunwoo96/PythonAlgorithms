# 21.01.29 baekjoon 11650 

N = int(input())
result = []

for i in range(N):
    input_x, input_y = map(int, input().split())
    result.append((input_x, input_y))

sorted_result = sorted(result, key = lambda x: (x[0], x[1]))

for i in range(N):
    print('{} {}'.format(sorted_result[i][0], sorted_result[i][1]))
