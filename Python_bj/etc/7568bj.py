# 210203 baekjoon 7568 덩치

n = int(input())
people = []

for i in range(n):
    key, weight = map(int, input().split())
    people.append((key, weight))

for person in people:
    result = 0
    for another_person in people:
        if person[0] < another_person[0] and  person[1] < another_person[1]:
            result += 1
    
    print(result + 1, end=" ")
print()