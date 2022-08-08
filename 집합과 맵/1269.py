#import sys
#input = sys.stdin.readline

#_, _ = map(int, input().split())

#a = set(map(int, input().split()))
#b = set(map(int, input().split()))

#c = set(a & b)

#a.difference_update(c)
#b.difference_update(c)

#print(len(a) + len(b))

import sys
input = sys.stdin.readline

_, _ = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

a.symmetric_difference_update(b)
print(len(a))