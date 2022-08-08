import sys
n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
lst = list(set(lst))
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)


#
# 1. 길이가 짧은 것부터 = > sort key = len
# 2. 길이가 같으면 사전 순으로 = > sort or sorted
# 3. 중복 제거 = > set

# sys.stdin.readline().strip() 
# = > strip()함수는 문자열 양 끝에 있는 공백을 제거해주고, 공백을 제거한 새로운 문자열을 반환함.
# (문자열.lstrip() = > 문자열 왼쪽에 있는 공백 제거)
# (문자열.rstrip() = > 문자열 오른쪽에 있는 공백 제거)