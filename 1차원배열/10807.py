n = int(input())
list = list(map(int, input().split()))
find_num = int(input())
cnt = 0

for i in range(len(list)):
   if (list[i] == find_num):
       cnt += 1

print(cnt)