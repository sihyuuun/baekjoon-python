nums = list(map(int, input().split()))
nums = sorted(nums, reverse=False)
for i in nums:
  print(i, end=' ')

# numbers = list(map(int, input().split()))
# numbers.sort()
# print(numbers[0], numbers[1], numbers[2])