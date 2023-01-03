# 허접한 풀이..
# import sys
# input = sys.stdin.readline

# T = int(input())
# cnt = [0,0,0]
# while T > 0:
#   if T >= 300 :
#     cnt[0] += T // 300
#     T %= 300
#   if T >=60:
#     cnt[1] += T // 60
#     T %= 60
#   if T >=10 :
#     cnt[2] += T // 10
#     T %= 10
#   if 0 < T and T < 10:
#     print(-1)
#     exit()

# for i in range(len(cnt)):
#   print(cnt[i], end= ' ')

# 개선된 코드
T = int(input())

if T % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = T // 300
    B = (T % 300) // 60
    C = (T % 300) % 60 // 10
    print(A, B, C)