import math
n = int(input())
phones = list(map(int, input().split()))
sum_Y = 0
sum_M = 0
for i in phones:
  sum_Y += math.ceil(i//30) * 10 + 10
  sum_M += math.ceil(i//60) * 15 + 15
if (sum_Y < sum_M):
  print('Y', sum_Y)
elif (sum_Y > sum_M):
  print('M', sum_M)
else:
  print('Y M', sum_Y)