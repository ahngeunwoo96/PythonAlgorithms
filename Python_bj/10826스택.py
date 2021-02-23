n = int(input())
stack = []
for i in range(n):
    com = list(map(str, input().split()))
    if com[0] == "push":
        stack.append(com[1])

    elif com[0] == "top":
        try:
            print(stack[-1])
        except:
            print(-1)

    elif com[0] == "size":
        print(len(stack))

    elif com[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)

    elif com[0] == "pop":
        try:
            print(stack.pop())
        except:
            print(-1)
