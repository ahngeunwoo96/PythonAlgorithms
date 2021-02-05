# 210205 baekjoon 1436 영화감독 숌

n = int(input())
result = 0
num = 0

while(result < n):
    num += 1
    if '666' in str(num):
        result += 1

print(num)