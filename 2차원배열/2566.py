max_n = max_row = max_col = 0

for i in range(9):
    li = list(map(int, input().split()))
    if max_n < max(li):
        max_n = max(li)
        max_row = i
        max_col = li.index(max(li))
print(max_n)
print(max_row+1, max_col+1)