# 허접한 풀이
# lst = list(map(int, input().split()))
# a = 0
# d = 0
# for i in range(0, 8):
#   if lst[i] == i+1:
#     a += 1
# for i in range(8, 0, -1):
#   if lst[8-i] == i:
#     d += 1
# if a == 8:
#   print('ascending')
# elif d == 8:
#   print('descending')
# else:
#   print('mixed')

# 개선 코드
lst = list(map(int, input().split()))

if lst == sorted(lst):
  print('ascending')
elif lst == sorted(lst, reverse=True):
  print('descending')
else:
  print('mixed')