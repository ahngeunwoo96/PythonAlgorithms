N = int(input())
road = list(input())

dis = [1000000] * N

dis[0] = 0
for i in range(1, N):
    for j in range(i):

        if road[i] == 'B':
            if road[j] == 'J':
                if dis[i] > dis[j] + (i-j) ** 2:
                    dis[i] = dis[j] + (i-j) ** 2
        elif road[i] == 'O':
            if road[j] == 'B':
                if dis[i] > dis[j] + (i-j) ** 2:
                    dis[i] = dis[j] + (i-j) ** 2
        else:
            if road[j] == 'O':
                if dis[i] > dis[j] + (i-j) ** 2:
                    dis[i] = dis[j] + (i-j) ** 2

if dis[N-1] == 1000000:
    dis[N-1] = -1   
print(dis[N-1])

