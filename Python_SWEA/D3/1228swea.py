# 210205 swea 1228 8일차-암호문1

for tc in range(1, 11):
    n = int(input())
    code = list(map(int, input().split()))
    command_n = int(input())
    command = list(input().split())
    j = 0

    while j != len(command):
        input_idx = int(command[j + 1])
        num = int(command[j + 2])
        j += 3
        for i in range(num + j - 1, j - 1, -1):
            code.insert(input_idx, command[i])
        j += num

    print(f"#{tc}", end=" ")
    for i in range(10):
        print(code[i], end=" ")
    print()