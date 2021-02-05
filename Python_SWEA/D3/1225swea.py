# 210205 swea 7일차 암호생성기 

for _ in range(1, 11):
    tc = int(input())
    input_num = list(map(int, input().split()))

    cnt = 1 
    while input_num[7] != 0:
        temp = input_num[1::]
        changed_num = input_num[0] - cnt
        if changed_num < 0:
            changed_num = 0
        temp.append(changed_num)
        cnt += 1
        input_num = temp[:]
        if cnt == 6:
            cnt = 1

    print(f"#{tc} ", end="")
    for i in range(8):
        print(input_num[i], end=" ")
    print()