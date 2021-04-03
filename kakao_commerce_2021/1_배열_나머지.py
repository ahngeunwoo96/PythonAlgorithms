def solution(n, p, c):
    answer = []

    # 0~n-1을 원소로 하는 배열 i
    # 원소의 개수가 c개인 0~n-1을 원소로 하는 배열 a
    # a[0]^p + ... a[c-1]^p를 n으로 나눈 나머지가 i랑 같음

    # 0~n-1의 p승의 나머지를 저장하는 배열
    n_rest = []
    for i in range(n):
        n_rest.append((i ** p) % n)

    for i in range(n):  # i: 나머지
        m = 0
        cnt = 0 # 나머지 i를 만들 수 있는 경우의 수

        # 나머지이기 때문에 가능한 나머지는 i, n+i, 2*n+i ...
        while (m * n + i) <= c * (n - 1):
            rest = m * n + i
            # 나머지를 rest로 만들 수 있는 a배열 경우의 수 찾기
            m += 1

        answer.append(cnt)

    return answer

n, p, c = 2, 3, 4
solution(n, p, c)