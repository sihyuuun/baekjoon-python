def gcd(a, b):
    while b != 0 :
        a, b = b, a%b
    return a

n = int(input())
r = list(map(int, input().split()))

for i in range(1, n):
    g = gcd(r[0], r[i])
    print('{0}/{1}' .format(r[0]//g, r[i]//g))

# 기약분수는 분자와 분모를 분자와 분모의 최대공약수로 나누면 만들어진다.
