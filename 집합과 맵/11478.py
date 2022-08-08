string = input()
s = set()

for i in range(len(string)):
    for j in range(i,len(string)):
        s.add(string[i:j+1])

print(len(s))