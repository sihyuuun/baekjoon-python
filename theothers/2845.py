L, P = map(int, input().split())
counts = list(map(int, input().split()))
count = L*P
for i in counts:
  print(i-count, end=' ')