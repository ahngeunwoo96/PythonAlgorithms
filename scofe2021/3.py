N = int(input())
m = [list(map(int, list(input()))) for _ in range(N)]

tot = 0
size = [0] * (N+1)

for s in range(1, N+1):
    for i in range(N-s+1):
        for j in range(N-s+1):
            flag = 0
            for yy in range(s):
                for xx in range(s):
                    if m[i+yy][j+xx] == 0:
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                size[s] += 1
                tot += 1

print(f"total: {tot}")
for i in range(1, N+1):
    if size[i] != 0:
        print(f"size[{i}]: {size[i]} ")

'''
4
1111
1111
1111
1111
'''
