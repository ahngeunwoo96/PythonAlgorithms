# # 21.02.02 baekjoon 2231 분해합 

n = int(input())
result = 0

for i in range(n):
    sum = i
    for a in str(i):
        sum += int(a)
    if sum == n:
        result = i
        break
else:
    sum = 0

print(result)
