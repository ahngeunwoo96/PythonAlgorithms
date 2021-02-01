# 21.02.01 baekjoon 2798 블랙잭

n, m = map(int, input().split())
cards = list(map(int, input().split()))

max = 0
for x in range(len(cards)):
    for y in range(x + 1, len(cards)):
        for z in range(y + 1, len(cards)):
            sum = cards[x] + cards[y] + cards[z]
            if m >= sum > max:
                max = sum
print(max)