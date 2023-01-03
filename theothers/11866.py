import sys
input = sys.stdin.readline
queue = []
result = []
n, k = map(int, input().split())
for i in range(1, n+1):
  queue.append(i)

while queue:
  for i in range(k-1):
    queue.append(queue.pop(0))
  result.append(queue.pop(0))

print('<', end='')
for i in range(len(result)-1):
  print(result[i],end=', ')
print(result[-1],end='')
print('>')
