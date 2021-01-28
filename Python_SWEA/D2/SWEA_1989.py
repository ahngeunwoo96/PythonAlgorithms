# 21.01.22 python 1989 초심자의 회문검사 문제풀이

TC = int(input())

for test_case in range(1, TC + 1):

    inputText = input()

    for i in range(len(inputText)):
        if inputText[i] != inputText[-1-i]:
            answer = 0
            break
    else:
        answer = 1
    
    print('#{} {}'.format(test_case, answer))