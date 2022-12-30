import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
  a, b = map(int, input().split())
  aa = a%10

  if aa == 0:
    print(10)
  elif aa in [1,5,6]:
    print(aa)
  elif aa in [4,9]:
    bb = b%2
    if bb == 0:
      print(aa*aa%10)
    else:
      print(aa)
  else:
    bb = b%4
    if bb == 0:
      print(aa**4%10)
    else:
      print(aa**bb%10)

# 단순히 a**b%10을 통해 문제를 풀면 시간초과가 발생함
# 1~10까지 각각 거듭제곱했을 때의 패턴을 분석해서 4가지 케이스로 나누어 문제를 풀어야함