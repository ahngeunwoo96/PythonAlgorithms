# 21.1.4 SWEA 6230 python 문제풀이

student = [88, 30, 61, 55, 95]

for i in range(5):
    if(student[i] >= 60):
        print("%d번 학생은 %d점으로 합격입니다." %(i + 1, student[i]))
    else:
        print("%d번 학생은 %d점으로 불합격입니다." %(i + 1, student[i]))
    