for tc in range(1, int(input()) + 1):
    string = input()
    stack = []

    result = "YES"
    for i in string:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                result = "NO"
                break
            else:
                stack.pop()

    if len(stack) != 0:
        result = "NO"
    print(result)

