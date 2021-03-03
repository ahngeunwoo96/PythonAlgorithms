while True:
    string = input()
    if string == ".":
        break

    stack = []
    answer = "yes"
    for word in string:
        if word == "(":
            stack.append(word)
        elif word == ")":
            try:
                if stack.pop() == "(":
                    pass
                else:
                    answer = "no"
                    break
            except:
                answer = "no"
                break

        if word == "[":
            stack.append(word)
        elif word == "]":
            try:
                if stack.pop() == "[":
                    pass
                else:
                    answer = "no"
                    break
            except:
                answer = "no"
                break

    if stack:
        answer = "no"

    print(answer)
