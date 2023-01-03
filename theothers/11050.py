# 허접한 풀이
# n, k = map(int, input().split())
# choose = 1
# for i in range(k):
#   choose *= n
#   n -= 1
# for i in range(k,0,-1):
#   choose /= i
# print(int(choose))

# 재귀
# import sys
# input = sys.stdin.readline
# def factorial(n):
#   if n==0:
#     return 1
#   return n * factorial(n-1)

# n, k = map(int, input().split())
# print(factorial(n)//(factorial(k) * factorial(n-k)))

# 반복문
import sys
input = sys.stdin.readline
def factorial(n):
  if n==0:
    return 1
  result = 1
  for i in range(1, n+1):
    result *= i
  return result
n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n-k)))