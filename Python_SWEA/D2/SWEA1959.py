# 21.01.28 SWEA 1959

for test_case in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max = 0
    if n > m:
        # 작은 블럭은 이동하면서 큰 볼록과 값을 곱함 
        for i in range(abs(n - m) + 1):
            result = 0
            for j in range(min(n, m)):
                result += a[i + j] * b[j]
            if result > max:
                max = result
    else:
        for i in range(abs(n - m) + 1):
            result = 0
            for j in range(min(n, m)):
                result += a[j] * b[i + j]
            if result > max:
                max = result
    
    print('#{} {}'.format(test_case, max))