import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dict = {}

for i in range(1, N+1):
	a = input().rstrip()
	dict[i] = a
	dict[a] = i

for i in range(M):
	s = input().rstrip()
	if s.isdigit():
		print(dict[int(s)])
	else:
		print(dict[s])