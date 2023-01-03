for i in range(3):
  bars = list(map(int, input().split()))
  if bars.count(0) == 1:
    print('A')
  elif bars.count(0)== 2:
    print('B')
  elif bars.count(0) == 3:
    print('C')
  elif bars.count(0) == 4:
    print('D')
  else:
    print('E')
