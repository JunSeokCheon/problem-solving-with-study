 # len(stack)!=0 이 필요한 이유 -> (())()) 마지막 )에서 stack[-1]에 list index range 오류 발생
n = int(input())
for _ in range(n):
  vps = input()
  stack = []
  for i in vps:
    if i == "(":
      stack.append(i)
    elif i == ")" and len(stack)!=0:
      if stack[-1] == "(":
        stack.pop()
      else:
        stack.append(i)
        break # stack에 )쌓여있으면 처리 불가(=no)하기 때문에 바로 break
    else: # i == ")" and len(stack)==0 일때 처리 ex) (()))))
      stack.append(i)
    
  if len(stack) == 0:
    print("YES")
  else:
    print("NO")