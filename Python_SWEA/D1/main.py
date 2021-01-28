a = "파이썬"
b = "프로그래밍"
c = "기본"

print(a)
print(b)
print(c)  

# Dictionary 
Dogs = {1 : '골든리트리버', 2 : '닥스훈트'}
Dogs[1]
Dogs[2]

# None
obj = None # 아무것도 저장하고 싶지 않은 경우
if obj:
    print("obj는 None이 아닙니다")
else:
    print("obj는 None입니다")

# 변수의 제거
# Garbage collector에 의해 알아서 메모리를 정리

a, b = 3, 2
print("{} + {} = {}".format(a, b, a+b))

# 대입 연산자
# **= : 좌변의 변수를 우변의 값으로 제곱해서 좌변의 값에 대입

a = 10
a += 5
print(a)

a -= 5
print(a)

a *= 5
print(a)

a /= 5
print(a)

a //= 5
print(a)

a %= 5
print(a)

a **= 2
print(a)

# 관계 연산자(비교 연산자)
# ==, !=, >, <, >=, <= 
# 수학에서 사용하는 8 < a < 10 과 같은 연산자 사용 가능 

# 논리 연산자
# and, or, not 
# True and False : False
# True or False : True
# not True : False 

# 비트 연산자
# &, |, ^, ~, <<, >> : and, or, xor, not, 왼쪽으로 시프트, 오른쪽으로 시프트
# 연산자의 우선순위 () > ** > 부호, 비트 부정 > 곱하기,나누기,몫,나머지 > 등 등..

#if문 true or false 
# if 조건식:
#   명령문
#   명령문

score = 80
if score <= 60:
    print("실패입니다.")
    print("%d 점 입니다." % score)
elif score <= 80:
    print("합격입니다.")
else:
    print("높은 점수입니다.")


operand1, operator, operand2 = 0, "", 0

operand1 = int(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /): ")
operand2 = int(input("두 번쨰 숫자를 입력하세요: "))

if operator == "+":
    print("%d + %d = %d" %(operand1, operand2, operand1 + operand2)) 
elif operator == "-":
    print("%d - %d = %d" %(operand1, operand2, operand1 - operand2)) 
elif operator == "*":
    print("%d * %d = %d" %(operand1, operand2, operand1 * operand2)) 
elif operator == "/":
    print("%d / %d = %d" %(operand1, operand2, operand1 / operand2)) 
else:
    print("본 프로그램에서는 지원하지 않는 연산자입니다. ")

for i in range(1, 5):
    print("*" * i)