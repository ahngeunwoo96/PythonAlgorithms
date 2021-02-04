# 210204 swea 1216 회문2

for test_case in range(1, 11):
    t = int(input())
    string = []
    for i in range(100):
        string.append(input())

    transposed_string = []
    for i in range(100):
        temp = []
        for j in range(100):
            temp += string[j][i]
        transposed_string.append(temp)

    def find_palindrome(string, n):
        for i in range(100):
            for j in range(100-n+1):
                temp = string[i][j:j+n]
                if temp == temp[::-1]:
                    return n
        
    result = 0
    for n in range(100, -1, -1):
        if find_palindrome(string, n):
            print(f"#{t} {n}")
            break
        if find_palindrome(transposed_string, n):
            print(f"#{t} {n}")
            break
