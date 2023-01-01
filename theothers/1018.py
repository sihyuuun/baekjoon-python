n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
  board.append(input())

# i, j는 칠할 체스판의 시작점을 찾는 것인데, n과 m에 -7을 해주는 이유는 이 지점부터 8x8크기의 체스판을 검사할 것이기 때문에
# 전체 체스판의 인덱스를 벗어나지 않게 하기 위함
for i in range(n-7):
  for j in range(m-7):
    draw1 = 0    # 시작지점이 'B'일 경우
    draw2 = 0    # 시작지점이 'W'일 경우

    # 시작점부터 8x8 크기의 체스판을 탐색하기 위해 i~i+8, j~j+8범위의 for문 작성
    for a in range(i, i+8):
      for b in range(j, j+8):
        # board[a][b] 지점이 2로 나눈 나머지가 0일 때와 1일 때를 이용해 색 결정
        if (a+b)%2 == 0:
          if board[a][b] != 'B':
            draw1 += 1
          if board[a][b] != 'W':
            draw2 += 1
        else:
          if board[a][b] != 'W':
            draw1 += 1
          if board[a][b] != 'B':
            draw2 += 1
    result.append(draw1)
    result.append(draw2)
print(min(result))
