# 21.01.28 baekjoon 2108 통계학
import sys

N = int(input())

result = []
for i in range(N):
    result.append(int(sys.stdin.readline()))

print('{:.0f}'.format(sum(result) / len(result)))

sorted_result = sorted(result)
print(sorted_result[len(result) // 2])

num_dict = {}
for num in result:
    if not num in num_dict:
        num_dict[num] = 1
    else:
        num_dict[num] += 1
sorted_dict = sorted(num_dict.items(), key = lambda x : x[1])

result = []
for i in range(len(sorted_dict) - 1, -1, -1):
    if i == len(sorted_dict) - 1:
        max_cnt = sorted_dict[i][1]
        result.append(sorted_dict[i][0])
    else:
        if sorted_dict[i][1] == max_cnt:
            result.append(sorted_dict[i][0])
if len(result) == 1:
    print(result[0])
else:
    result.sort()
    print(result[1])
    

print(max(result) - min(result))

