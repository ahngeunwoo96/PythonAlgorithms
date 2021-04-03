answer = 100

def DFS(n, N, ok_numbers, check, numbers, K):
    global answer

    if n == N:
        # ok_numbers가 조건을 만족하는지 확인

        for i in range(N):
            for j in range(2):
                if i+j < N and i+j-1 >= 0:
                    if abs(ok_numbers[i+j] - ok_numbers[i+j-1]) > K:
                        return

        # ok_numbers와 numsbers와 비교해서 swap이 얼마나 필요할지 계산
        swap = 0
        for i in range(N):
            for j in range(i+1, N):
                if ok_numbers[i] == numbers[j]:
                    swap += 1
                    ok_numbers[i], ok_numbers[j] = ok_numbers[j], ok_numbers[i]

        if numbers == ok_numbers:
            if answer > swap:
                answer = swap
                return

    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            ok_numbers.append(numbers[i])
            DFS(n + 1, N, ok_numbers, check, numbers, K)
            check[i] = 0
            ok_numbers.remove(numbers[i])


def solution(numbers, K):
    global answer
    N = len(numbers)

    # 모든 numbers를 정렬해서 조건을 만족하는 numbers를 찾기
    # 그리고 원래의 numbers에서 몇번을 swap해야 조건을 만족하는 numbers가 되는지 최소의 swap 수를 찾기

    check = [0] * N
    DFS(0, N, [], check, numbers, K)

    return answer
