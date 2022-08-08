import sys
input = sys.stdin.readline

N, M = map(int, input().split())

NoSee = set()
NoListen = set()

for i in range(N):
    NoSee.add(input())

for i in range(M):
    NoListen.add(input())

result = sorted(list(NoSee & NoListen))

print(len(result))
for i in result:
    print(i, end='')