# 21.01.26 SWEA 1970 쉬운 거스름돈
# 지페의 단위를 money에 저장
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for test_case in range(1, int(input()) + 1):

    N = int(input())

    result = [0, 0, 0, 0, 0, 0, 0, 0]

    
    for i in range(len(money)):
        # 만약 남은 잔액이 i번째 화폐로 나눠지면
        if N // money[i] > 0:
            # 화폐의 개수를 세는 result 리스트에 개수를 저장
            result[i] += N // money[i]
            # N은 화폐의 단위로 나눈 나머지값을 저장
            N %= money[i]

    print('#{}'.format(test_case))
    print('{}'.format(' '.join(map(str, result))))
    

        
                