# 9칸을 기준으로 왼쪽상단의 위치를 생각 9사분면!
# 변수를 함수밖에 선언하면 함수 안에서 접근하기가 힘들다.(방법1. 매개변수로 넘겨주거나, global 선언)
# 그러나 리스트나, 딕셔너리 같은 경우는 접근 가능(하지만 각각의 main/paper 함수 일경우는 매개변수로 넘겨주는 방법이 맞다.)
n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]
result = [0,0,0]
# result_dic = {"-1":0, "0":0, "1":0}

def paper(x,y,n):
  num = n_list[x][y]

  for i in range(x, x+n):
    for j in range(y, y+n):
      if num != n_list[i][j]:
        paper(x,y,n//3)
        paper(x+n//3, y, n//3)
        paper(x+(n//3)*2, y, n//3)
        paper(x, y+n//3, n//3)
        paper(x+n//3, y+n//3, n//3)
        paper(x+(n//3)*2, y+n//3, n//3)
        paper(x, y+(n//3)*2, n//3)
        paper(x+n//3, y+(n//3)*2, n//3)
        paper(x+(n//3)*2, y+(n//3)*2, n//3)
        return
  # result_dic[str(num)] += 1
  if num == -1:
    result[0] += 1
    return
  elif num == 0:
    result[1] += 1
    return
  else:
    result[2] += 1
    return
  
paper(0,0,n)
for num in result:
  print(num)