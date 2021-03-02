'''
처음에는 큰 색종이부터 채우면 최소의 갯수르 채울 수 있지 않을까 생각했으나 그 방법으로는 예외 케이스가 존재함
예외케이스)
111
11111
11111
 11111
 11111
   111
위와 같은 경우 4*4 색종이를 채우는것보다 3*3 색종이를 2개와 2*2 색종이 2개를 사용하는것이 더 최소의 갯수임

결국 모든 Map을 돌며 1을 만나면 가능하다면 색종이를 5 * 5부터 1 * 1까지 다 넣어보며 dfs 방법을 사용해서
최소의 값을 찾아야 함
'''
def ColorPaper(y, x):
    # 모든 맵을 돌며
    global answer
    if answer == -1:
        return

    for i in range(y, 10):
        for j in range(x, 10):
            # 1을 발견한 경우
            # 가능한 모든 색종이를 넣어
            if i == 9 and j == 9:
                return

            if Map[i][j] == 1:
                for k in range(5, 0, -1):
                    # 범위를 나가지 않도록 조정
                    if i + k <= 10 and j + k <= 10:
                        # 색종이의 크기만큼 모든 Map이 1인지 확인
                        isSizeOk = True
                        for yy in range(i):
                            for xx in range(i):
                                # Map에 1이 아닌 부분이 있는 경우
                                # 붙일 수 없는 사이즈의 색종이이므로 빠져나감
                                if Map[i + yy][j + xx] != 1:
                                    isSizeOk = False
                                    break
                            if isSizeOk == False:
                                break
                else:
                    for yy in range(k):
                        for xx in range(k):
                            Map[i+yy][j+xx] = 0
                    if paper_cnt != 0:
                        paper_cnt[k] -= 1
                    # 같은 사이즈의 색종이를 5개 이상 사용한 경우
                    else:
                        answer = -1
                        return
                    ColorPaper(i, 0)
                    for yy in range(k):
                        for xx in range(k):
                            Map[i+yy][j+xx] = 1
                    paper_cnt[k] += 1

paper_cnt = [5] * 6
Map = [list(map(int, input().split())) for _ in range(10)]
answer = 0
ColorPaper(0, 0)
print(answer)



