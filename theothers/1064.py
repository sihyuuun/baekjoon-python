XA, YA, XB, YB, XC, YC = map(int, input().split())
ans = 0.0
if (XA-XB)*(YA-YC) == (YA-YB)*(XA-XC):
  ans = -1.0
else:
  dAB = ((XA-XB)**2 + (YA-YB)**2)**0.5
  dBC = ((XB-XC)**2 + (YB-YC)**2)**0.5
  dCA = ((XC-XA)**2 + (YC-YA)**2)**0.5

  ans = ((max(dAB, dBC, dCA)-min(dAB,dBC,dCA))*2)
print(ans)

# 문제 풀이
# 길이가 다른 선분 두 개를 활용하여 둘레를 구할 수 있음
# 평행사변형의 둘레 길이가 가장 길 때는 가장 긴 변과 중간변을 더한 다음 *2를 해주면 되고
# 둘레 길이가 가장 짧을 때는 가장 짧은 변과 중간변을 더한 다음 *2를 하면 됨
# 따라서 이 둘의 차는 (가장 긴 변 - 가장 짧은 변)*2
# 평행사변형이 안 될 조건은 세 점이 한 선분 위에 있으면 사각형을 만들 수 없음
# 즉, 점 3개가 이루는 선분의 기울기가 같으면 사각형 형성 불가
# 3개의 기울기를 비교하는 것보다 한 개의 기준점을 갖고 다른 두 점과의 기울기를 비교하여 두 기울기가 같으면 세 점은 한 선분 위에 있는 것
# 나눗셈은 런타임에러를 발생시킬 수 있기 때문에 등식을 이항하여 곱셈으로 나타냄