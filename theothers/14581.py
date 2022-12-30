id = input()
fan = "fan"
for i in range(1,10):
  if i == 5:
    print(':'+id+":",end='')
  else:
    print(':'+fan+":",end='')
  if i % 3 == 0:
    print()