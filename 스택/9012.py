import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    stk = []
    s = input()
    for j in s:
        if j == '(':
            stk.append(j)
        elif j == ')' :
            if len(stk) != 0 and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(")")
                break
    if len(stk) == 0:
        print("YES")
    else:
        print("NO")