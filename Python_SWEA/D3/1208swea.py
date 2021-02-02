# 21.02.02 swea 1208 1일차-Flatten

for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()
    for i in range(dump):
        boxes[-1] -= 1
        boxes[0] += 1
        boxes.sort()
    print("#{} {}".format(test_case, boxes[-1] - boxes[0]))
