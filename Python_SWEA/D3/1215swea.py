# 21.02.02 swea 1215 3일차-회문1

for test_case in range(1, 2):
    n = int(input())
    words = []
    for i in range(8):
        row = []
        row.extend(input())
        words.append(row)
    
    for i in range(8):
        for j in range(9-n):
            for k in range(n):
                if words[i][j + k] 