import sys
input = sys.stdin.readline

X = int(input())
N = int(input())
hap = 0

for i in range(N):
    a, b= map(int, input().split())
    hap += a * b

if hap == X:
    print("Yes")
else:
    print("No")