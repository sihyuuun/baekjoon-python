# deque 이용
from collections import deque
N = int(input())
deque = deque([i for i in range(1, N+1)])

while len(deque) > 1:
  deque.popleft()
  move = deque.popleft()
  deque.append(move)
print(deque[0])

# 패턴 분석 [N- 2**(N>2의 제곱)]* 2
N = int(input())
square = 2
while True:
  if (N == 1 or N == 2):
    print(N)
    break
  square *= 2
  if (square >= N):
    print((N - square//2)*2)
    break
  