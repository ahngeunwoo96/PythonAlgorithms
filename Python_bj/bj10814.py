# 21.02.01 baekjoon 10814 나이순 정렬

n = int(input())
people = []

for i in range(n):
    age, name = map(str, input().split())
    people.append((i, int(age), name))

result = sorted(people, key = lambda x: (x[1], x[0]))

for i in range(len(result)):
    print(result[i][1], result[i][2])