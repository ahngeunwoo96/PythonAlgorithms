# 21.02.02 swea 1215 3일차-회문1

for test_case in range(1, 11):
    n = int(input())
    words = []
    for i in range(8):
        row = []
        row.extend(input())
        words.append(row)
    result = 0

    # 가로 회문 확인
    for i in range(8):
        for j in range(9-n):
            for k in range(n//2):
                if words[i][j+k]!= words[i][j+n-1-k]:
                    break
            else:
                result += 1

    # 세로 회문 확인
    for i in range(8):
        for j in range(9-n):
            for k in range(n//2):
                if words[j+k][i]!=words[j+n-1-k][i]:
                    break
            else:
                result += 1

    print("#{} {}".format(test_case, result))