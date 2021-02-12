# 210208 baekjoon 10870 피보나치 수5

def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    if n == 0:
        return 0

    return Fibonacci(n-1) + Fibonacci(n-2)

n = int(input())
result = Fibonacci(n)
print(result)
