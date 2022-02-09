# 핵심
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.

# 1. 1~n까지 수를 스택에 넣는다(오름차순)
# 2. push 1회 = + 1회
# 3. 입력은 어디에 쓸까 ? -> 입력은 테스트용이다, 수열이 만들어지는지 안되는지, 
# 끊는 용도(입력은 다른 구역이라고 생각)
# 스택의 맨 위의 수와 입력 수를 비교해서 같다면 -, pop 해준다
# 4. 같지 않다면 수열을 만들 수 없다는 의미

# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1

# cnt 
# stack 
# result  


# 1
# 2
# 5
# 3
# 4

# cnt 
# stack  
# result  
import sys
input = sys.stdin.readline
n = int(input())
stack = []
result = []
cnt = 1
flag = 1

for _ in range(n):
  num = int(input())
  
  while cnt <= num:
    stack.append(cnt)
    result.append("+")
    cnt += 1

  if num == stack[-1]:
    stack.pop()
    result.append("-")
  else:
    flag = 0
    break
  
if flag == 0:
  print("NO")
else:
  for i in result:
    print(i)