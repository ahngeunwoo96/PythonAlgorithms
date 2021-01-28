# 21.1.6 SWEA 6320 python 문제풀이

rockScissorPaper = ['가위', '바위', '보']

user1, user2, first, second = input(), input(), input(), input()

for i in range(3):
    if(rockScissorPaper[i] == first):
        firstInt = i
    if(rockScissorPaper[i] == second):
        SecondInt = i

if(firstInt == SecondInt):
    print("비겼습니다.")
elif(firstInt == 0 and SecondInt == 2):
    print("%s가 이겼습니다!" % first)
elif(firstInt == 2 and SecondInt == 0):
    print("%s가 이겼습니다!" % second)
elif(firstInt > SecondInt):
    print("%s가 이겼습니다!" % first)
else:
    print("%s가 이겼습니다!" % second)
