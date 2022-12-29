burgers = list()
sides = list()
for i in range(3):
  burgers.append(int(input()))
for i in range(2):
  sides.append(int(input()))
print(min(burgers)+min(sides)-50)