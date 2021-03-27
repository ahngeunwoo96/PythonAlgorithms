def solution(s):
    while len(S) < len(s):
        # s의 마지막 문자열이 'A'
        if s[-1] == 'A':
            s = s[:-1]
        # s의 마지막 문자열이 'B'
        elif s[-1] == 'B':
            s = s[:-1]
            s = s[::-1]

    if S == s:
        return 1
    else:
        return 0


S = input()
T = input()

print(solution(T))