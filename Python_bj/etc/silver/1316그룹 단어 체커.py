N = int(input())
ans = 0

for _ in range(N):
    stack = []
    flag = 1
    s = input()
    for word in s:
        if word not in stack:
            stack.append(word)
        else:
            if word != stack[-1]:
                flag = 0
                break

    if flag == 1:
        ans += 1

print(ans)