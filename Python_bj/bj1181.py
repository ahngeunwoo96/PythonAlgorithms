# 21.01.31 baekjoon 1181 단어정렬

n = int(input())
result = []

for i in range(n):
    result.append(input())

result = list(set(result))

sorted_result = sorted(result, key = lambda x : (len(x), x))

for word in sorted_result:
    print(word)