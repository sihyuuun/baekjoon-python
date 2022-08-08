N, M = map(int, input().split())
strings = set()

for i in range(N):
    string = input()
    strings.add(string)

count = 0

for i in range(M):
    s = input()
    if s in strings:
        count += 1
print(count)