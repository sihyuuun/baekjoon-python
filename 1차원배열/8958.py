n = int(input())
for i in range(n):
    quiz = input()
    score = 0
    sumScore= 0
    for j in quiz:
        if j == 'O':
            score += 1;
        else:
            score = 0;
        sumScore += score;
    print(sumScore)
    