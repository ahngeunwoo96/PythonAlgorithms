# 210205 baekjoon 15649 N과 M
from itertools import permutations

n, m = map(int, input().split())
words = permutations(range(1, n + 1), m)
for i in words:
    print(' '.join(map(str, i)))
