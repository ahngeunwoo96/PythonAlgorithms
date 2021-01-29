# 21.01.29 SWEA 1946 간단한 압축 풀기

for test_case in range(1, int(input()) + 1):
    N = int(input())
    result = ''
    for i in range(N):
        alp, cnt = map(str, input().split())
        result += alp * (int(cnt))
    print('#{}'.format(test_case))
    
    for i in range(len(result)):
        if i % 10 == 0 and i != 0:
            print()
        print(result[i], end ='')
    print()
    