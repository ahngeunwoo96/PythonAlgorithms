score = {}
for i in range(8):
    score[i+1] = int(input())

sorted_score = sorted(score.items(), key=lambda x : x[1], reverse=True)

Sum = 0
answer_idx = []
for i in range(5):
    Sum += sorted_score[i][1]
    answer_idx.append(sorted_score[i][0])
    answer_idx.sort()

print(Sum)
print(*answer_idx)