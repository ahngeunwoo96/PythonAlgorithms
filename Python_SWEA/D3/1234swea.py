# 210205 swea 1234 10일차-비밀번호

for tc in range(1, 11):
    len_num, num = map(str, input().split())
    len_num = int(len_num)
    i = 0

    while i != len_num - 1:
        if num[i] == num[i+1]:
            temp = num[i+2:]
            num = num[:i]
            num += temp
            i = i - 2
            len_num = len_num -2
        i += 1

    print(f"#{tc} {num}")