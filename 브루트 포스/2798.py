from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))

big = 0

for i in combinations(nums, 3):
    temp = sum(i)
    if big < temp <= m:
        big = temp
print(big)