def solution(n, cnt):
    global ans

    # 만약 n이 B와 같아지면 B를 만들 수 있는 것이므로
    # 그때까지의 연산이 ans보다 작으면 ans에 저장
    if n == B:
        if ans > cnt:
            ans = cnt
        return

    # 가지치기
    # 숫자가 B보다 크면 컷
    # 연산의 수가 ans보다 크면 컷
    if n > B:
        return

    if cnt > ans:
        return

    # 원래의 숫자에 2를 곱하고, 끝에 1을 더한 경우의 수를 모두 해본다.
    solution(n * 2, cnt+1)
    solution(n * 10 + 1, cnt+1)

A, B = map(int, input().split())
ans =  10000000

solution(A, 1)
# B를 만들 수 없는 경우 ans를 -1로 변경
if ans == 10000000:
    ans = -1
print(ans)