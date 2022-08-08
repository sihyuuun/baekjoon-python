# N = int(input())
# member_list = []
# for i in range(N):
#     age, name = map(str, input().split())
#     age = int(age)
#     member_list.append((age, name))

# member_list.sort(key=lambda x : x[0])   #나이만 비교.  이름은 입력한 순으로 받기 때문.

# for i in member_list:
#     print(i[0], i[1])

import sys
N = int(sys.stdin.readline())
member = []
for i in range(N):
    member.append(list(sys.stdin.readline().split()))
member.sort(key=lambda x:int(x[0]))

for i in member:
    print(i[0], i[1])