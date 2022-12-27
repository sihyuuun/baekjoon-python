# a = input()
# print(a.swapcase())

str = ""
for i in input():
    if i.islower():
        str += i.upper()
    else:
        str += i.lower()
print(str)