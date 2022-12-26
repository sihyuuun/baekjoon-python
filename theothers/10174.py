n = int(input())
for i in range(n):
  temp = ''
  str = input()
  str = str.upper()
  for i in str:
    temp = i + temp
  if str == temp:
    print("Yes")
  else:
    print("No")

