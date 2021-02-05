# 210205 swea 1230 8일차-암호문3

for tc in range(1, 11):
    n = int(input())
    code = list(map(int, input().split()))
    command_n = int(input())
    command = list(input().split())
    j = 0

    while j != len(command):
        if command[j] == 'I':
            input_idx = int(command[j + 1])
            num = int(command[j + 2])
            j += 3
            for i in range(num + j - 1, j - 1, -1):
                code.insert(input_idx, command[i])
            j += num
        elif command[j] == 'D':
            delete_idx = int(command[j + 1])
            num = int(command[j + 2])
            j += 3
            for i in range(num):
                code.pop(delete_idx)
        else:
            num = int(command[j + 1])
            for i in range(num):
                code.append(command[j + 2 + i])
            j += num + 2
            

    print(f"#{tc}", end=" ")
    for i in range(10):
        print(code[i], end=" ")
    print()