zero = [1, 0, 1]
one = [0, 1, 1]

def fibo(n):
  length = len(zero)
  if n >= length:
    for i in range(length, n+1):
      zero.append(zero[i-1]+zero[i-2])
      one.append(one[i-1]+one[i-2])
  print(zero[n], one[n])

T = int(input())
for _ in range(T):
  fibo(int(input()))


# 문제 풀이
# fibo(n)을 호출했을 때, 실행되는 fibo(0)과 fibo(1)은
# fibo(n-1)의 0과 1 호출 횟수 + fibo(n-2)의 0과 1 호출 횟수와 동일
# zero는 순서대로 피보나치(해당 인덱스)를 실행했을 때 호출되는 0의 횟수를 추가하는 배열
# 코드에서 for문 (length, n+1)을 직접 손계산해보면 이해하기 쉬움