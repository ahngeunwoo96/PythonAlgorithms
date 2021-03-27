# 최대공약수를 구하는 함수
def GCD(a, b):
    if b == 0:
        return a

    return GCD(b, a%b)

# 약수의 개수를 튜플 형태로 리스트에 담아서 저장하는 함수
def FindDiv(n):
    result = []
    if n == 1:
        result.append((1, 1))
        return result

    for i in range(2, n+1):
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1

        if cnt != 0:
            result.append((i, cnt))

    return result

N, K = map(int, input().split())
A = list(map(int, input().split()))

# A의 숫자를 K와의 최대공약수로 변경
# 최대공약수를 약수의 개수를 담는 튜플형태의 리스트로 변경
for i in range(N):
    A[i] = GCD(max(A[i], K), min(A[i], K))
    A[i] = FindDiv(A[i])

# K의 약수 # 약수의 개수 구하기
K_div = FindDiv(K)

print(A)
print(K_div)
# 약수별로 채울 수 있는 경우의 수를 구하기
# 어떻게 약수별로 채울 수 있는 경우의 수를 구할까
# 여러개의 약수를 갖고있는 경우 어떻게 할지..



