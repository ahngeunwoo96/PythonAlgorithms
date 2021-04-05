from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
nm = deepcopy(m)
ans = 5000

# 회전 연산의 배열
rotate = []
for i in range(K):
    rotate.append(list(map(int, input().split())))

ran = list(permutations(range(len(rotate)), len(rotate)))
print(rotate)

for j in range(len(ran)): # 회전 연산의 랜덤 수열의 개수
    order = list(map(int, ran[j]))
    for i in range(len(order)):
        m = deepcopy(nm)
        r, c, s = rotate[order[i]][0], rotate[order[i]][1], rotate[order[i]][2]
        r1, c1, r2, c2 = r-s-1, c-s-1, r+s-1, c+s-1

        for k in range(s): # 회전하는 사각형의 갯수
            temp = m[r1+k][c2-k]
            for col in range(c2-k, c1+k, -1): # 오른쪽으로 이동
                m[r1+k][col] = m[r1+k][col-1]

            temp2 = temp
            temp = m[r2-k][c2-k]
            for row in range(r2-k, r1+k+1, -1): # 아래쪽으로 이동
                m[row][c2-k] = m[row-1][c2-k]
            m[r1+k+1][c2-k] = temp2

            temp2 = temp
            temp = m[r2-k][c1+k]
            for col in range(c1+k, c2-k): # 왼쪽으로 이동
                m[r2-k][col] = m[r2-k][col+1]
            m[r2-k][c2-k-1] = temp2

            temp2 = temp
            temp = m[r1+k][c1+k]
            for row in range(r1+k, r2-k): # 위쪽으로 이동
                m[row][c1+k] = m[row+1][c1+k]
            m[r2-k-1][c1+k] = temp2

    for row in range(N):
        Sum = sum(m[row])
        ans = min(Sum, ans)

print(ans)
'''
5 6 3
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
2 2 1
'''