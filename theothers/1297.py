import math
D, H, W = map(int, input().split())
ans = (D**2/(H**2 + W**2))**0.5
print(math.floor(H * ans), math.floor(W * ans))