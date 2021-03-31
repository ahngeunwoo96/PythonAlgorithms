def Score(array):
    # 게임을 진행해서 점수를 출력
    base = [0] * 4
    out = 0
    score = 0
    start = 0
    for inning in range(N):
        for i in range(start, 9):
            if out == 3:
                start = i
                break

            if hitters[inning][array[i]] == 0: # 아웃
                out += 1

            elif hitters[inning][array[i]] == 1: # 1루타
                # 주자들을 1칸씩 이동
                for j in range(2, -1, -1):
                    if base[j] == 1:
                        base[j+1] = 1 # 한 칸 전진
                        base[j] = 0
                # 타자 진루
                base[0] = 1
                # 점수계산
                if base[3] == 1:
                    score += 1
                    base[3] = 0

            elif hitters[inning][array[i]] == 2: # 2루타
                # 주자들을 2칸씩 이동
                for j in range(1, -1, -1):
                    if base[j] == 1:
                        base[j+2] = 1
                        base[j] = 0

                base[1] = 1

                for j in range(2, 4):
                    if base[j] == 1:
                        score += 1
                        base[j] = 0

            elif hitters[inning][array[i]] == 3: # 3루타

                for j in range(0, 3):
                    if base[j] == 1:
                        score += 1
                        base[j] = 0

                base[2] = 1

            else: # 홈런
                for j in range(0, 3):
                    if base[j] == 1:
                        score += 1
                        base[j] = 0

                score += 1

    return score

def Recur(n, array):
    global ans
    # 네번째 선수
    if n == 3:
        array.append(0)
        Recur(n+1, array)
        array.remove(0)
        return

    if n == 9:
        temp = Score(array)
        if ans < temp:
            ans = temp
        return

    for i in range(1, 9):
        if visited[i] == 0:
            visited[i] = 1
            array.append(i)
            Recur(n+1, array)
            visited[i] = 0
            array.remove(i)


N = int(input()) # N: 이닝 수
hitters = []
num = 0 # 쳐야하는 타자의 번호

for i in range(N):
    hitters.append(list(map(int, input().split())))

# hitters를 배열화고 점수를 알아냄
# 배열하는 방법 -> 재귀를 이용해서 배열
visited = [0] * 9
visited[0] = 1
ans = 0
Recur(0, [])
print(ans)