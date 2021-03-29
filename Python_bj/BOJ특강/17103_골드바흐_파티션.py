n = 1000000

prime_num = [1 for _ in range(n+1)]

# 에스토스테네스의 체 방법
# 소수인지를 판별하는 방법으로 먼저 구하고자하는 수 n의 제곱근까지만 구하면 됨 -> n을 나눌 수 있는 수는 n의 제곱근까지
# 2부터 시작해서 그의 배수들을 소수에서 지우는 방법
for i in range(2, int(n ** 0.5) + 1):
    if prime_num[i] == 1:
        j = 2
        while i * j <= n:
            prime_num[i*j] = 0
            j += 1

def solution(N):
    result = 0

    for i in range(2, N//2+1):
        if prime_num[i] and prime_num[N-i]:
            result += 1

    return result

for tc in range(1, int(input())+1):
    N = int(input())
    ans = solution(N)
    print(ans)