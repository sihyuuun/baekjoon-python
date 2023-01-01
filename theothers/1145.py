a = list(map(int, input().split()))
n = min(a)
while True:
  cnt = 0
  for i in range(5):
    if n % a[i] == 0:
      cnt += 1
  if cnt > 2:
    print(n)
    break
  n+=1

# 문제 풀이
# 주어진 다섯 개의 자연수 중 최소 3개로 나누어 떨어지는 숫자 중 최솟값을 구하는 문제
# 1부터 시작할 필요 없이 5개의 숫자 중 가장 작은 수부터 1씩 증가시켜 주어진 다섯 개의 수로 나누어 떨어지면 cnt 증가
# cnt가 3이상이 되면 해당 숫자가 정답