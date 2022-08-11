import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
nums.sort()
nums_mode = Counter(nums).most_common()
print(round(sum(nums)/N))
print(nums[N//2])

if len(nums_mode) > 1:
    if nums_mode[0][1] == nums_mode[1][1]:
        print(nums_mode[1][0])
    else:
        print(nums_mode[0][0])
else:
    print(nums_mode[0][0])
print(nums[-1]-nums[0])