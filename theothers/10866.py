# 리스트 이용
# import sys
# input = sys.stdin.readline
# N = int(input())
# deque = []

# for i in range(N):
#   order = input().split()
#   if order[0] == 'push_front':
#     deque.insert(0, order[1])
#   elif order[0] == 'push_back': 
#     deque.append(order[1])
#   elif order[0] == 'pop_front':
#     if deque: print(deque.pop(0))
#     else:
#       print(-1)
#   elif order[0] == 'pop_back':
#     if deque: print(deque.pop(-1))
#     else:
#       print(-1)
#   elif order[0] == 'size':
#     print(len(deque))
#   elif order[0] == 'empty':
#     if len(deque) == 0: print(1)
#     else: print(0)
#   elif order[0] == 'front':
#     if len(deque) == 0: print(-1)
#     else:
#       print(deque[0])
#   elif order[0] == 'back':
#     if len(deque) == 0: print(-1)
#     else: print(deque[-1])

# deque 라이브러리 이용
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
deque = deque()
for _ in range(N):
  order = input().split()
  if order[0] == 'push_front':
    deque.appendleft(order[1])
  elif order[0] == 'push_back': 
    deque.append(order[1])
  elif order[0] == 'pop_front':
    if len(deque) == 0: print(-1)
    else:
      print(deque.popleft())
  elif order[0] == 'pop_back':
    if len(deque) == 0:
      print(-1)
    else:
      print(deque.pop())
  elif order[0] == 'size':
    print(len(deque))
  elif order[0] == 'empty':
    if len(deque) == 0: print(1)
    else: print(0)
  elif order[0] == 'front':
    if len(deque) == 0: print(-1)
    else:
      print(deque[0])
  elif order[0] == 'back':
    if len(deque) == 0: print(-1)
    else: print(deque[-1])