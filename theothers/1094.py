a = int(input())
cnt = 0
while a != 0:
  if a % 2 == 1:
    cnt += 1
  a //= 2
print(cnt)

# 문제 풀이
# 64cm부터 시작해서 막대기의 길이는 점차 반으로 줄어들어 32, 16, 8, 4, 2, 1cm가 될 것
# 이때 이 막대들을 최소 몇 개 붙여야 목표로 한 막대의 길이가 되냐는 문제
# 즉, 이진법으로 나타냈을 때 1이 몇 개 있냐는 말
# 23의 경우 10111이므로 1이 4개 있어 답은 4