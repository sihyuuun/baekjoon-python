import sys
input = sys.stdin.readline

N = int(input())

num = []

for i in range(N):
    x, y = map(int, input().split())
    num.append([x,y])

num.sort(key = lambda x : (x[1], x[0]))

for i in num:
    print(i[0], i[1])




# # 사용 문법
# # split
# split : 문자열 나누기
# input().split()처럼 괄호 안에 아무 값도 넣어주지 않으면 공백(스페이스,엔터,탭 등)을 기준으로 문자열을 나누어 줌.

# # map
# map : 리스트의 요소를 지정된 함수로 처리해주는 함수
# map 은 원본 리스트를 변경하지 않고 새 리스트를 생성함.
# map(int, input().split())

# # append
# append : 리스트에 요소 추가

# # sort
# sort : 정렬, 기본값은 오름차순 정렬

# # 람다함수
# num.sort(key = lambda x : (x[1], x[0])) 
# : key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다.
#   x[1] 즉, y 좌표값을 오름차순으로 정렬하고 x[0] 즉, x 좌표로 정렬함.


