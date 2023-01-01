n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(input())
a, b = 0, 0
for i in range(n):
  if "X" not in board[i]:
    a+=1
for j in range(m):
  if "X" not in [board[i][j] for i in range(n)]:
    b += 1

print(max(a, b))

# 문제 풀이
# 각 행과 열마다 X가 안들어있는 행, 열의 개수를 구한 다음 그 중 큰 값을 출력해주면 됨
