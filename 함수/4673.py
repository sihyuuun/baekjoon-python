num = set(range(1, 10001))
rmv = set()        #셀프 넘버가 아닌 수들을 지울 집합
for i in num:
    for j in str(i):    
        i += int(j)        #이렇게 하게 되면 예를 들어 i가 13이라면 i에 1, 3을 더함. 13+1+3 
    rmv.add(i)
num = num - rmv
for k in sorted(num):
    print(k)