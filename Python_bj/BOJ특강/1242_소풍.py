N, K, M = map(int, input().split())

# 차례대로 숫자를 말하고 K에 해당하는 숫자를 말한 사람이 퇴장당하는 게임
out_cnt = 0
num = -1
M -= 1 # 동호의 위치는 실제 번호보다 1 작으므로
tot_num = N
nM = 0

while True:
    # 매 라운드마다 동호의 위치와 퇴장당하는 위치를 계산
    num = (num+K)
    if num < N:
        out_cnt += 1
    elif num >= N:
        num = num % N
        N -= out_cnt
        out_cnt = 1
        if num >= N:
            num %= N
            N -= out_cnt
        M -= nM
        nM = 0

    if N == 1:
        break

    if num < M:
        nM += 1 # 동호의 위치 변화
    elif num == M:
        break

print(tot_num - N + out_cnt)

