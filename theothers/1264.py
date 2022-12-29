vowels = ['a', 'e', 'i', 'o', 'u']
while True:
  cnt = 0
  s = input()
  if s == '#' : break
  else:
    s = s.lower()
    for i in range(len(s)):
      if s[i] in vowels:
        cnt += 1
    print(cnt)
