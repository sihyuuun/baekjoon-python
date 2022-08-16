s = input()
n = ord('a')

for i in range(26):
    if s.count(chr(n)) != 0:
        print(s.index(chr(n)), end=' ')
    else:
        print('-1', end=' ')
    n+=1