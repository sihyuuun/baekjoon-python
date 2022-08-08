h, m = map(int, input().split())
if h > 0:
    if m >= 45:
        print(h, m-45, sep=' ')
    elif m < 45:
        print(h-1, 15+m, sep=' ')
elif h == 0:
    if m >= 45:
        print(h, m-45, sep=" ")
    elif m < 45:
        print("23", 15+m, sep=' ')