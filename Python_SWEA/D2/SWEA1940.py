# 21.01.29 SWEA 1940 가랏! RC카!

for test_case in range(1, int(input()) + 1):
    n = int(input())
    v, a, s = 0, 0, 0
    for i in range(n):
        command = input()
        if command[0] == '1':
            a = int(command[2])
            v += a
            s += v
        elif command[0] == '2':
            a  = int(command[2])
            v -= a
            if v < 0: 
                v = 0
            s += v
        else:
            s += v
    print('#{} {}'.format(test_case, s))
