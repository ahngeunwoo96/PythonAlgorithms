n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

answer = []
for i in range(2, min(num) + 1):
    for j in range(len(num)):
        if j == 0:
            rest = num[j] % i

        else:
            if rest != num[j] % i:
                break

    else:
        answer.append(i)

for i in answer:
    print(i, end=" ")