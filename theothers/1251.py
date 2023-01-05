word = list(input())
answer = []
tmp = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word) ):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(a + b + c)
for a in tmp:
    answer.append(''.join(a))

print(sorted(answer)[0])

# 문제 풀이
# 임의의 두 부분을 골라 단어를 쪼갠 후 세 단어로 만듦 -> 세 단어를 각각 뒤집은 다음 합쳐서 한 문자열을 만들고 만든 문자열 중 사전순으로 가장 앞서는 단어를 출력
# 이중 for문을 활용하여 단어를 세 단어로 나눔. i와 j가 단어의 경계선이 됨
# 뒤집은 세 단어를 합쳐 tmp 리스트에 저장하고 tmp 리스트에는 세 단어가 저장되어 있으므로 이 세 단어를 join()으로 하나의 단어로 만들어줌
# 문자열들이 저장되어 있는 answer 리스트를 sort한 다음 가장 첫번째 있는 단어가 정답