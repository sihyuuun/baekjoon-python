day = 0
arrlist = [31,28,31,30,31,30,31,31,30,31,30,31]
weeklist = ["SUN", "MON","TUE","WED","THU","FRI","SAT"]

x, y = map(int, input().split())
for i in range(x-1):
  day += arrlist[i]
day = (day + y)%7
print(weeklist[day])