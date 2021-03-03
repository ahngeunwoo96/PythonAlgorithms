def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

for tc in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    print(a * b // GCD(a, b))


