import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
min_cnt = abs(100-n)

broken = list(map(int, input().split()))

for channel in range(1000001):
  channel = str(channel)
  for j in range(len(channel)):
    if int(channel[j]) in broken:
      break
    elif j == len(channel)-1:
      min_cnt = min(min_cnt, abs(int(channel)-n) + len(str(channel)))
print(min_cnt)

# 문제 풀이
# 초기 min_cnt는 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
# 그 이후 조건문 두 가지 케이스로 나눠서 문제 풀이
# if문 -> 각 숫자가 고장났는지 확인 후, 고장 났으면 break
# elif문 -> 고장난 숫자 없이 마지막 자리까지 왔다면 min_cnt 비교
# min(기존답, 해당 번호로부터 타겟번호까지의 차 + 번호를 누를 횟수)