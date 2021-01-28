# -*- coding: utf-8 -*- 
# 21.1.21 SWEA 1983 조교의 성적 매기기
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

TC = int(input())

for test_case in range(1, TC + 1):

    N, K = map(int, input().split())
    total_list = []
    
    for i in range(N):
        mid, fin, hom = map(int, input().split())
        total = mid * 0.35 + fin * 0.45 + hom * 0.20
        total_list += [total] 
    
    print(total_list)
    sorted_total_list = sorted(total_list, reverse=True)
    K_tot = total_list[K - 1]
    print(K_tot)
    K_pos = total_list.index(K_tot)
    print(K_pos, N // 10)
    K_grade = grade[K_pos // (N // 10)]
    print("#{} {}".format(test_case, K_grade))