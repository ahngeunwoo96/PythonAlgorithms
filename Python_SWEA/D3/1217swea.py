def recur(n, m):
    if m == 0:
        return 1
    
    return recur(n, m-1) * n


for _ in range(1, 11):
    t = int(input())

    n, m = map(int, input().split())

    result = recur(n, m)
    print(f"#{t} {result}")
