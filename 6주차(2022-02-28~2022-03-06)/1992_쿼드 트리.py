n = int(input())
n_list = [list(map(int,input())) for _ in range(n)]

def quad(x,y,n):
  check = n_list[x][y]

  for i in range(x,x+n):
    for j in range(y,y+n):
      if check != n_list[i][j]:
        print("(", end="")
        quad(x,y,n//2)  # 1사분
        quad(x,y+n//2,n//2) # 2사분
        quad(x+n//2,y,n//2) # 3사분
        quad(x+n//2,y+n//2,n//2) # 4사분
        print(")", end="")
        return
  if check == 1:
    print("1", end="")
    return
  else:
    print("0", end="")
    return

quad(0,0,n)