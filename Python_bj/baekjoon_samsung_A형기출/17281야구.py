import sys
from itertools import permutations

def game(line_ups):
    hitter = 0
    score = 0
    for i in range(N): # inning
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3: # out이 3이 될때까지 게임 진행
            if hitters[i][line_ups[hitter]] == 0: # 아웃
                out += 1
            elif hitters[i][line_ups[hitter]] == 1: # 1루타
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif hitters[i][line_ups[hitter]] == 2: # 2루타
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif hitters[i][line_ups[hitter]] == 3: # 3루타
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else: # 홈런
                score += 1 + b1 + b2 + b3
                b1, b2, b3 = 0, 0, 0
            hitter = (hitter + 1) % 9

    return score


N = int(sys.stdin.readline()) # N: 이닝 수
hitters = []

for i in range(N):
    hitters.append(list(map(int, sys.stdin.readline().split())))

ans = 0
for line_ups in permutations(range(1, 9), 8):
    line_ups = list(line_ups[:3]) + [0] + list(line_ups[3:])
    ans = max(ans, game(line_ups))
print(ans)