list = []
for i in range(10):
    n = int(input())
    list.append(n % 42)
list = set(list)       # 중복을 제거하기 위해 set으로 집합 자료형으로 만들어줌.
print(len(list))