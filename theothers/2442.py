# n = int(input())
# i = n-1; j = 1
# for _ in range(n):
#   print(' ' * i, end='')
#   print('*' * j)
#   i -= 1; j += 2

n = int(input())
for i in range(1,n+1):
  print(" "*(n-i) + "*" * (2*i-1))