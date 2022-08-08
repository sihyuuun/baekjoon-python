import sys
input = sys.stdin.readline

N = input()
n = list(map(int, input().split()))
n_temp = list(sorted(set(n)))

dict = {n_temp[i]:i for i in range(len(n_temp))}

for i in n:
	print(dict[i], end=' ')