import sys
N = int(input())
M = []
for i in range(N):
    M.append(int(sys.stdin.readline()))
for i in sorted(M):
    sys.stdout.write(str(i)+'\n')