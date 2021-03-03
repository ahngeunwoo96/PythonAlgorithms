n = int(input())
nums = list(map(int, input().split()))

stack = []
answer = []

stack.append(nums[n-1])
answer.append(-1)

i = n-2 # 뒤에서부터 순회
while i >= 0:
    # 현재의 수가 stack에 들어가있는 수보다 큰 경우
    if stack:
        pass
    else: # stack이 비어있는 경우
        answer.append(-1)
        stack.append(nums[i])
        i -= 1
        continue

    if nums[i] >= stack[-1]:
        stack.pop() # stack의 마지막 수를 제거
        continue
    else:
        answer.append(stack[-1])
        stack.append(nums[i])
        i -= 1

answer = reversed(answer)
print(*answer)


