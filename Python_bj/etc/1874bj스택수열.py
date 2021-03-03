# 210218 baekjoon 1874 스택 수열

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

stack = []
answer = []
Max = 0
for i in range(n):
    if Max < num[i]:
        for j in range(Max+1, num[i]+1):
            stack.append(j)
            answer.append("+")
        stack.pop()
        answer.append("-")
        Max = num[i]

    elif stack.pop() == num[i]:
        answer.append("-")

    else:
        answer = ["NO"]
        break

for i in range(len(answer)):
    print(answer[i])



