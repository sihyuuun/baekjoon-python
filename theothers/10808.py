s = input()
alphabet = [0] * 26
for i in s:
  alphabet[ord(i)-97]+=1
for i in range(len(alphabet)):
  print(alphabet[i], end=' ')