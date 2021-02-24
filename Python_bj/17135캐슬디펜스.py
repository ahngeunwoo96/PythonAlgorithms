import copy

n, m, d = map(int, input().split())
Map = []
for i in range(n):
    Map.append(list(map(int, input().split())))
nMap = []
answer = 0

# 공격할 적의 위치를 반환하는 함수
def FindEnemy(y, x, nMap):
    for dd in range(d):
        for xx in range(-dd, dd + 1):
            if 0 <= y-dd+abs(xx) and 0 <= x+xx < m:
                if nMap[y - dd + abs(xx)][x + xx] == 1:
                    return [y-dd+abs(xx), x+xx]

    return -1

def CastleGame():
    nMap = copy.deepcopy(Map)
    kill = 0

    # 적 공격
    for round in range(n): # 한 라운드마다 궁수가 한칸씩 위로 이동한다고 가정
        round_kill_pos = []
        for i in range(m):
            if nMap[n][i] == 1: # 궁수가 있을때
                # 공격으로 제거할 수 있는 적을 찾아서 공격
                y, x = n-1-round, i # 궁수 앞의 위치
                try:
                    enemy_pos = FindEnemy(y, x, nMap)
                    if enemy_pos != -1 and enemy_pos not in round_kill_pos:
                        kill += 1
                        round_kill_pos.append(enemy_pos)
                except:
                    pass

        # 죽인 적을 제거
        for i in range(len(round_kill_pos)):
            nMap[round_kill_pos[i][0]][round_kill_pos[i][1]] = 0


    return kill

# 궁수 배치
for i in range(1<<m):
    cnt = 0
    archer = []
    for j in range(m):
        if i & (1<<j):
            cnt += 1
            archer.append(1)
        else:
            archer.append(0)
    if cnt == 3:
        Map.append(archer)
        tmp = CastleGame()
        if answer < tmp:
            answer = tmp
        del(Map[n])

print(answer)

'''
반례
10 10 8
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
ans: 30 
'''