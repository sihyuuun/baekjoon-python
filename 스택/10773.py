import sys
input = sys.stdin.readline
K = int(input())
stk = []
for i in range(K):
    n = int(input())
    if n == 0:
        stk.pop()
    else:
        stk.append(n)
print(sum(stk))