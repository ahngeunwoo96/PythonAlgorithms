n = int(input())
num = []
num2 = []
for i in range(n):
    num.append(int(input()))

for i in range(n-1):
    num2.append(abs(num[i] - num[i+1]))

def GCD(a, b):
    if b == 0:
        return a

    return GCD(b, b%a)

for i in range(n-1):
    

