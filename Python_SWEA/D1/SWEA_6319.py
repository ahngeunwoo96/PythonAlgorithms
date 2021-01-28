# 21.1.6 SWEA 6319 문제풀이

text = input()
isPalind = True

for i in range(len(text)):
    print(text[len(text) - 1 - i], end = "")
    if(text[i] != text[len(text) - 1 - i]):
        isPalind = False
        continue

print()
if isPalind == True:
    print("입력하신 단어는 회문(Palindrome)입니다.")


