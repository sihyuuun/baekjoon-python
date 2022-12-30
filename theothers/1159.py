n = int(input())
alphabet = [0] * 26
for i in range(n):
  name = input()
  alphabet[ord(name[0])-97] += 1
cnt = 0
for i in range(26):
  if alphabet[i] >= 5:
    print(chr(int(i)+97),end='')
  else:
    cnt += 1
if cnt == 26:
  print("PREDAJA")
