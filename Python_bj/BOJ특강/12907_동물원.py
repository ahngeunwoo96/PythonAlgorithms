def solution(n, cat, rabbit, cnt):
    global ans

    # 마지막 번호까지 모두 넣은 경우
    if n == N:
        ans = cnt
        return

    if animals[n] == cat:
        if animals[n] == rabbit:
            # 둘 다 들어갈 수 있는 경우
            solution(n+1, cat+1, rabbit, cnt*2)
        else:
            # cat에만 넣을 수 있는 경우
            solution(n+1, cat+1, rabbit, cnt)
    else:
        if animals[n] == rabbit:
            # rabbit에만 넣을 수 있는 경우
            solution(n+1, cat, rabbit+1, cnt)
        else:
            # 아무곳에도 넣을 수 없는 경우
            return

N = int(input())
animals = list(map(int, input().split()))

animals.sort()

ans = 0
solution(0, 0, 0, 1)
print(ans)
