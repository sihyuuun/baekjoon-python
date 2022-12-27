n = int(input())
i = j = n
for _ in range(i):
  for _ in range(j):
    print('*', end='')
  j-=1
  print()