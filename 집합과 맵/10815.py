import sys
input = sys.stdin.readline

_ = input()
n = set(map(int, input().split()))
_ = input()
m = list(map(int, input().split()))

for i in m:
    if i in n:
        print('1', end=' ')
    else:
        print('0', end=' ')