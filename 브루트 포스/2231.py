N = int(input())
result = 0
for i in range(1, N+1):
    A = list(map(int, str(i)))
    print(A)
    result = i + sum(A)
    print(result)

    if result == N:
        print(i)
        break

    if i == N:
        print(0)