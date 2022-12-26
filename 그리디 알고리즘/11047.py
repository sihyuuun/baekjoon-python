n, k = map(int, input().split())
coins = list()
for i in range(n):
  coins.append(int(input()))
count = 0
for i in reversed(coins):
  if i <= k:
    count += k//i
    k = k%i
print(count)