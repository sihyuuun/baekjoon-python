list = [i for i in range(1, 31)]
for _ in range(28):
    n = int(input())
    list.remove(n)

print(min(list))
print(max(list))