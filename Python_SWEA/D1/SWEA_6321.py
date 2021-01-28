# 21.1.6 SWEA 6321 python 문제풀이

num = int(input())
cnt = 0

for i in range(1, num):
    if num % i == 0:
        cnt+=1

if(cnt == 1):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")