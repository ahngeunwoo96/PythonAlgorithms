# 21.1.6 SWEA 6323 문제풀이

num = int(input())
Pibo = []

Pibo += [1]
Pibo += [1]
    
for i in range(2, num):
    Pibo += [Pibo[i - 1] + Pibo[i - 2]]

print(Pibo)