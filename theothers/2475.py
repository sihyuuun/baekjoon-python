# def square(list):
#   return [i * i for i in list]

# nums = list()
# nums = map(int, input().split())
# nums = square(nums)

# print((sum(nums))%10)

ans = 0
for n in list(map(int, input().split())):
    ans += n**2
print(ans%10)