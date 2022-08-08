import sys
input = sys.stdin.readline

N = int(input())

num_list = [0] * 100001

for _ in range(N):
    temp = int(input())
    num_list[temp] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)