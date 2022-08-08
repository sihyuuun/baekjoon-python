import sys
n = int(sys.stdin.readline())

so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key=lambda x:(x[0], x[1]))
for i in so:
    print(i[0], i[1])


#
# lambda를 사용하여 정렬 기준을 정해주는데, 먼저 첫 번째 인자(x[0]) 즉, x줄 부터 정렬을 하고 
# 그 다음 두 번째 인자인(x[1]) y줄을 정렬해줌