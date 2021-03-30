N, K = map(int, input().split())
# f[N]은 N명일 때, 살아남는 사람을 저장하는 리스트

# 만약 K가 홀수일때는 2명일 때, 2가 살아남음
# 그리고 짝수일때는 2명일 때, 1이 살아남음

if K%2:
    f = 2
else:
    f = 1

for i in range(3, N+1):
    f = (K + f) % i
    if f == 0:
        f = i

if N == 1:
    f = 1

print(f)