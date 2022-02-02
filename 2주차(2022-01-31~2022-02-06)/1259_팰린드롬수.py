# 1 method : 문자열 슬라이싱 이용하는 방법
while(True):
  n = input()
  if n == "0":
    break;
  n_reverse = n[::-1]
  if n == n_reverse:
    print("yes")
  else:
    print("no")

# 2 method : 직접 인덱스로 접근하는 방법
while(True):
  flag = 1
  n = input()
  if n == "0":
    break;
  
  for i in range(len(n)):
    if n[i] != n[len(n)-1-i]:
      print("no")
      flag = 0
      break
  
  if flag == 1:
    print("yes")