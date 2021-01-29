# 21.01.29 SWEA 1284 수도 요금 경쟁

for test_case in range(1, int(input()) + 1):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    if W <= R:
        B = Q
    else:
        B = Q + (W - R) * S
    
    print('#{} {}'.format(test_case, min(A, B)))