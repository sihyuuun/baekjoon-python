n = int(input())
times = list(map(int, input().split()))

times.sort()
sum = 0
for i in range(n):
  for j in range(i+1):
    sum += times[j]
print(sum)