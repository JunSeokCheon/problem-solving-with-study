t = int(input())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(t):
  com = input()
  x = 0
  y = 0
  position = [(x,y)]
  position_dir = 0
  for j in com:
    if j == "F":
      x += dx[position_dir]
      y += dy[position_dir]
    elif j == "B":
      x -= dx[position_dir]
      y -= dy[position_dir]
    elif j == "L":
      if position_dir == 3:
        position_dir = 0
      else:
        position_dir += 1
    elif j == "R":
      if position_dir == 0:
        position_dir = 3
      else:
        position_dir -= 1
    position.append((x,y))
  width = sorted(position, key = lambda x : -x[0])[0][0] - sorted(position, key = lambda x : x[0])[0][0]
  height = sorted(position, key = lambda x : -x[1])[0][1] - sorted(position, key = lambda x : x[1])[0][1]
  print(width * height)