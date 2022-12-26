n = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(n):
    n, m = map(int, input().split())
    for i in range(n, n+10):
        for j in range(m, m+10):
            paper[i][j] = 1

area = 0
for row in paper:
    area += row.count(1)

print(area)