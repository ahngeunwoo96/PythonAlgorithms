# 210210 baekjoon 13305 주유소

n = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))
oils = []

result = 0
for i in range(len(roads)):
    if i == 0:
        oils.append(cities[0])
        result += oils[0] * roads[0]
    else:
        oils.append(min(cities[i], oils[i-1]))
        result += oils[i] * roads[i]


print(result)