N, M = map(int, input().split())
board = []
new = []
for i in range(N):
  board.append(input())

for i in range(N-7):
  for j in range(M-7):
    w = 0 # w로 시작했을 때 다시 칠해야 하는 개수
    b = 0 # b로 시작했을 때 다시 칠해야 하는 개수
    for k in range(i, i+8):
      for l in range(j, j+8):
        if (k + l) % 2 == 0: # 행+열 인덱스로 접근
          if board[k][l] != "W": # w로 시작 -> 첫번째 w가 아니야 -> 다시 칠
            w+=1
          if board[k][l] != "B":
            b+=1
        else: 
          if board[k][l] != "B": # w로 시작 -> 두번 째 칸이 b가 아니야 -> 다시 칠
            w+=1
          if board[k][l] != "W":
            b+=1
    new.append(w)
    new.append(b)

print(min(new))