# 210213 baekjoon 1037 약수

n = int(input())
div = list(map(int, input().split()))
a = min(div) * max(div)
print(a)