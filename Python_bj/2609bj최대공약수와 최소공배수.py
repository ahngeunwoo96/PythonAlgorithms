# 210214 baekjoon 2609 최대공약수와 최소공배수

num1, num2 = map(int, input().split())

# 최대공약수: gcd, 최소공배수: lcm
for i in range(min(num1, num2), 0, -1):
    if num1 % i == 0:
        if num2 % i == 0:
            gcd = i
            break
i = 1
num1_list=[]
num2_list=[]

while True:
    num1_list.append(i * num1)
    if i * num1 in num2_list:
        lcm = i * num1
        break
    num2_list.append(i * num2)
    if i * num2 in num1_list:
        lcm = i * num2
        break
    i += 1

print(gcd)
print(lcm)
