import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    a = list(map(str, input().split()))
    s = str(a[1])
    for j in range(0, len(s)):
        print('{0}'.format(s[j]) * int(a[0]), end='')
    print('')