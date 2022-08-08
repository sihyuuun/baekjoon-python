n = int(input())
Prime = list(map(int, input().split()))

Prime.sort()

if len(Prime) == 1:
    print(Prime[0] ** 2)
elif len(Prime) == 2:
    print(Prime[0] * Prime[1])
else:
    print(Prime[0] * Prime[-1])



#다른 사람 풀이
n = int(input())
a = list(map(int, input().split()))
a_max = max(a)
a_min = min(a)
print(a_max * a_min)