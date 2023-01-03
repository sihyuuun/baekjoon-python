import sys
input = sys.stdin.readline
N = int(input())

d = [0] * (N+1)

for i in range(2, N+1):
  # 2와 3으로 나누어 떨어지지 않는 경우는 무조건 1을 빼야 하기 때문에 +1을 해줌
  d[i] = d[i-1] + 1
  # d[i]가 3 또는 2로 나누어 떨어지는 경우에는 1을 빼는 것보다 나누어 떨어지는게 훨씬 이득이기 때문에 min을 통해 최솟값 선택
  # (d[i//3]+1, d[i//2]+1에서 +1은 3 또는 2로 나누어 주는 연산을 더해주는 것)
  if i % 3 == 0:
    d[i] = min(d[i], d[i//3]+1)
  if i % 2 == 0:
    d[i] = min(d[i], d[i//2]+1)
print(d[N])