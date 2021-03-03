def Attach(x, y, cnt):
    global ans
    # 만약 x가 10이 된 경우 줄바꿈
    if x >= 10:
        Attach(0, y+1, cnt)
        return

    # 끝까지 탐색한 경우 색종이의 갯수가 최솟값이면 ans에 저장
    if y >= 10:
        if ans > cnt:
            ans = cnt
        return

    # 색종이를 붙일경우
    if M[y][x] == 1:
        # n: 색종이의 크기
        for n in range(5, 0, -1):
            if paper[n] == 5:
                continue
            isPossible = True
            if y + n <= 10 and x + n <= 10:
                for yy in range(n):
                    for xx in range(n):
                        if M[y+yy][x+xx] != 1:
                            isPossible = False
                            break
                    if isPossible == False:
                        break
                # 색종이를 붙이는게 가능한 경우
                if isPossible == True:
                    for yy in range(n):
                        for xx in range(n):
                            M[y+yy][x+xx] = 0
                    paper[n] += 1
                    Attach(x+n,y,cnt+1)
                    paper[n] -= 1
                    for yy in range(n):
                        for xx in range(n):
                            M[y+yy][x+xx] = 1
    else:
        Attach(x+1, y, cnt)


M = [list(map(int, input().split())) for _ in range(10)]
paper = [0] * 6
ans = 100
Attach(0, 0, 0)
if ans == 100:
    ans = -1
print(ans)
