while True:
  str = input()
  str_list = list(str)
  str_list.reverse()
  str2 = ''.join(str_list)
  if str == '0':
    break
  elif str == str2:
    print('yes')
  else:
    print('no')