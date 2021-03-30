f = [0] * 2501
f[0], f[1], f[2] = 1, 1, 2

for i in range(3, 2501):
    for j in range(i):
        f[i] += (f[j] * f[i-j-1])
        f[i] %= 1000000007

for tc in range(1, int(input())+1):
    L = int(input())

    if L%2:
        print(0)
    else:
        print(f[L//2]) 