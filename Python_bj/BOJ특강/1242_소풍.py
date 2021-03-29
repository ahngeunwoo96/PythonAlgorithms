N, K, M = map(int,input().split())
result = 0
tmp_m = M

while result < N:
    result += 1
    # 남아있는 수보다 K가 큰 경우 동호가 수가 지워지는 경우
    if K % (N - result + 1) == tmp_m % (N - result + 1):
        break

    # 동호의 수가 지워지는 경우
    if K == tmp_m:
        break

    # m의 위치가 K만큼 이동
    # N, K, M = 5, 2, 3 일때
    # 1, 2, 3, 4, 5 에서 2가 지워지고 3, 4, 5, 1 이렇게 수의 배열이 변화하는 것으로 생각
    # 다음은 K 번째인 4가 지워지고 5, 1, 3 이렇게 수의 배열이 됨 -> 3, 5 -> 3
    else:
        tmp_m -= K
        while tmp_m <= 0:
            tmp_m += (N - result + 1)

print(result)