for i in range(3):
  H1, M1, S1, H2, M2, S2 = map(int, input().split())
  if S1 > S2 :
    M2 -= 1
    S = S2 + 60 - S1
  else:
    S = S2 - S1
  if M1 > M2 :
    H2 -= 1
    M = M2 + 60 - M1
  else:
    M = M2 - M1
  H = H2-H1
  print(H,M,S)