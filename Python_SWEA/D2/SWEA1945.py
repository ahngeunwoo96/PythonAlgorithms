# 21.01.29 SWEA 1945 간단한 소인수분해

for test_case in range(1, int(input()) + 1):
    n = int(input())
    result = [0] * 5
    while n % 2 == 0:
        n //= 2
        print
        result[0] += 1

    while n % 3 == 0:
        n //= 3
        result[1] += 1

    while n % 5 == 0:
        n //= 5
        result[2] += 1

    while n % 7 == 0:
        n //= 7
        result[3] += 1

    while n % 11 == 0:
        n //= 11
        result[4] += 1
    
    string = ''
    for num in result:
        string += str(num) + ' '
    
    print('#{} {}'.format(test_case, string[:-1]))