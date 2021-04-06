import sys

N = int(input()) # 수식의 길이
input_data = list(input()) # 수식
ans = -3000000000 # 값이 2^-31까지 가능하므로

# 괄호를 할 수 있는 경우의 수 계산
# 연산자의 개수만큼 괄호를 넣을 수 있는 부분이 있음
# 그러나 중첩된 괄호는 사용할 수 없으므로 연속된 1이 있으면 안됨
l = len(input_data)//2
# 비트마스크
for i in range(1<<l):
    bracket = [0] * l
    for j in range(l):
        if i & (1<<j):
            bracket[j] = 1

    cont = 0 # 계속되는지 확인하기 위한 변수
    for j in range(l):
        if bracket[j] == 1:
            cnt += 1
            if cont == 1:
                break
            else:
                cont = 1
        else:
            cont = 0
    else:
        # 가능한 괄호의 경우이므로 연산을 계산해야함
        data = input_data[::]
        cnt = 0 # 괄호의 개수
        for j in range(l):
            # 만약 괄호가 포함된 부분이라면 먼저 계산
            if bracket[j] == 1:
                n1, oper, n2 = data.pop(2*j-2*cnt), data.pop(2*j-2*cnt), data.pop(2*j-2*cnt)
                if oper == '+': data.insert(2*j-2*cnt,int(n1)+int(n2))
                elif oper == '-': data.insert(2*j-2*cnt,int(n1)-int(n2))
                else: data.insert(2*j-2*cnt,int(n1)*int(n2))
                cnt += 1

        # 남은 연산을 계산
        while len(data) > 1:
            n1, oper, n2 = data.pop(0), data.pop(0), data.pop(0)
            if oper == '+':
                data.insert(0, int(n1) + int(n2))
            elif oper == '-':
                data.insert(0, int(n1) - int(n2))
            else:
                data.insert(0, int(n1) * int(n2))

        # N = 1인 경우, data[0]가 str 형이기 때문에 int 형으로 변환 필요!
        if ans < int(data[0]):
            ans = int(data[0])

print(ans)