# Python 3으로 하면 시간초과 나서 PyPy로 해줌
from math import inf
import sys
input = sys.stdin.readline

N, M, B= map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

ans = inf   # 걸리는 시간 우선 최대로 둠
height = 0   # 층수(높이)

for i in range(257):    # 0~256층까지 탐색
  max, min = 0, 0
  for j in range(N):
    for k in range(M):
      if ground[j][k] < i:    # 블록이 현재 높이보다 작다면
        min += (i-ground[j][k])      # 현재 높이가 블록 높이보다 높을 때 (min만큼 인벤토리에서 꺼내서 채워야함)
      else:
        max += (ground[j][k]-i)    # 블록 높이가 현재 높이보다 높을 때 (max 만큼 블록이 제거된 후 인벤토리에 추가됨)
  inventory = max + B  # 인벤토리에 있는 총 블록수 = max(블록높이가 현재 높이보다 높아 제거한 블록 개수) + 현재 인벤토리에 있는 블록 개수

  # 현재 인벤토리에 있는 블록 개수가 min(채워야하는 블록의 개수)보다 커야 층을 만들 수 있음
  if inventory >= min:
    if min + (max * 2) <= ans:    # 시간 구하기 (min은 블록 채우는 데 걸리는 시간 1초, max는 블록 제거하는데 걸리는 시간 2초를 곱해줌 -> min + max * 2가 현재 최저시간인 ans보다 작거나 같아야 ans 갱신됨)
      # 0부터 256층까지 비교하므로 갱신 될수록 고층의 최저시간 (문제에서 최저 시간이 같다면 가장 높은 층을 출력하라고 했으므로 ans 갱신될 때마다 height도 갱신)
      ans = min + max * 2
      height = i    # 현재 층수
print(ans, height)