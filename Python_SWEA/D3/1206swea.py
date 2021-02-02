# 21.02.02 swea 1206 1일차 view

for test_case in range(1, 11):
    n = int(input())
    apart = list(map(int, input().split()))
    result = 0
    for i in range(2, n-2):
        light_floor = 256
        for j in range(-2, 3):
            if j == 0:
                continue

            if apart[i + j] >= apart[i]:
                light_floor = 0
                break
            if 0 < (apart[i] - apart[i+j]) < light_floor:
                light_floor = apart[i] - apart[i+j]
            
        result += light_floor
    print("#{} {}".format(test_case, result))
                
             
