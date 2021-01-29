# 21.01.29 baekjoon 1427 소트인사이드 

N = input()
result = []
for word in N:
    result.append(word)
result.sort(reverse=True)
print(''.join(result))