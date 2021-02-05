# 210205 swea 5일차-GNS
number = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for tc in range(1, int(input()) + 1):
    t, num = input().split()
    num = int(num)
    result = [0] * 10

    input_num = []
    input_num += list(map(str, input().split()))

    for i in range(num):
        for j in range(10):
            if input_num[i] == number[j]:
                result[j] += 1
    
    print(f"#{tc}")
    for i in range(10):
        for j in range(result[i]):
            print(number[i], end=" ")


            


