fs = input()
ft = input()

# 두 문자열을 같은 개수까지 만든다음에
# 비교하여 같은지 틀린지 비교

# 개수의 최소공배수를 찾기
# 먼저 최대공약수를 찾아야 함

def GCD(a, b):
    if b == 0:
        return a

    return GCD(b, a % b)

gcd = GCD(max(len(fs), len(ft)), min(len(fs), len(ft)))
lcm = (len(fs) // gcd * len(ft) // gcd * gcd)

nfs = fs
while len(nfs) < lcm:
    nfs += fs

nft = ft
while len(nft) < lcm:
    nft += ft

if nfs == nft:
    print(1)
else:
    print(0)
