# 21.01.26 SWEA 1966 숫자를 정렬하자 

for test_case in range(1, int(input()) + 1):
    N = int(input())
    num = list(map(int, input().split()))
    # sorted() 함수를 통해 list형 num을 오름차순으로 정렬
    result = sorted(num)
    print('#{} {}'.format(test_case, ' '.join(map(str, result))))