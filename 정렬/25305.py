N, k = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort()
scores.reverse()

print(scores[k-1])