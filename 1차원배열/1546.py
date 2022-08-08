n = int(input())
list = list(map(int, input().split()))
max = max(list)
new_list = []
for score in list:
    new_list.append(score/max*100)
avg = sum(new_list)/n
print(avg)
