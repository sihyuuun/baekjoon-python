import sys
input = sys.stdin.readline

find_chess = list(map(int, input().split()))

chess = [1, 1, 2, 2, 2, 8]

for i in range(len(find_chess)):
		print(chess[i]-find_chess[i], end=' ')