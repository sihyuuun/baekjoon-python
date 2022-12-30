import sys
input = sys.stdin.readline
n = int(input())
plugs = 0
for i in range(n):
  plugs += int(input())
print(plugs-n+1)