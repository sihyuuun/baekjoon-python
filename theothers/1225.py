import sys
input = sys.stdin.readline
a, b = map(list, input().split())
a = list(map(int, a))
b = list(map(int, b))
print(sum(a)*sum(b))

# 123 45 -> 1 * 4 + 2 * 4 + 3 * 4 + 1 * 5 + 2 * 5 + 3 * 5 = 54
# (1 + 2 + 3) * 4 + (1 + 2 + 3) * 5
# (1 + 2 + 3) * (4 + 5)