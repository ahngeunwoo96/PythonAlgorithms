def Connect(a, b):
    # bfs방식을 통해서 모든 지역구가 연결되어 있는지 확인
    # 만약 하나의 지역구만 포함되있다면 무조건 연결되어있음

    # a, b 선거구 중 아무 지역구도 없는 경우 False를 반환
    if not len(a) or not len(b):
        return False

    visited = [0] * (N+1)
    if len(a) == 1:
        visited[a[0]] = 1
    else:
        q = [] # queue
        q.append(a[0])
        visited[a[0]] = 1

        while q:
            n = q.pop()
            for region in edge[n-1]:
                if region in a:
                    if visited[region] == 0:
                        q.append(region)
                        visited[region] = 1

    if len(b) == 1:
        visited[b[0]] = 1
    else:
        q = []
        q.append(b[0])
        visited[b[0]] = 1

        while q:
            n = q.pop()
            for region in edge[n-1]:
                if region in b:
                    if visited[region] == 0:
                        q.append(region)
                        visited[region] = 1

    # 방문하지 않은 지역이 있다면 False를 반환
    for i in range(1, N+1):
        if visited[i] == 0:
            return False
    return True


def divide_region(cnt):
    global ans

    if cnt == N+1:
        # 모든 선거구를 나눈 경우
        # 가능한 경우인지 판단

        # 빈 선거구 제거
        if not a or not b:
            return

        # bfs 방식을 통해 모든 지역구와 연결되어 있는지 확인
        if not Connect(a, b):
            return

        # 두 선거구로 나뉘어져서 가능한 경우만 남음
        # 두 선거구의 인구 수를 비교하여 가장 최솟값을 구하기
        population_a, population_b = 0, 0
        for region in a:
            population_a += population[region-1]
        for region in b:
            population_b += population[region-1]

        ans = min(ans, abs(population_a - population_b))
        return

    a.append(cnt)
    # cnt가 선거구 a에 포함되는 경우
    divide_region(cnt+1)
    a.remove(cnt)
    b.append(cnt)
    # cnt가 선거구 b에 포함되는 경우
    divide_region(cnt+1)
    b.remove(cnt)

N = int(input())
population = list(map(int, input().split()))
edge = []
for i in range(N):
    temp = list(map(int, input().split()))
    edge.append(temp[1:])

# 구역을 두 선거구로 나눔
a, b = [], [] # 두 선거구 a, b
ans = 1000 # 두 선거구의 인구 차이의 최솟값을 저장할 변수
divide_region(1)
if ans == 1000:
    ans = -1
print(ans)

'''
5
5 2 3 4 1
1 2
4 1 3 5 4
1 2 
1 2
1 2
'''

'''
3
1 2 1
1 2
2 1 3
1 2
'''

'''
6
2 2 2 2 2 2
1 3
1 4
1 1
1 2
1 6
1 5
'''