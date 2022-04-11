def solution(grid):
    answer = []
    visited = [[[0 for k in range(4)] for j in range(len(grid[0]))] for i in range(len(grid))]
    dx = [1,0,-1,0]  # 아래, 왼, 위, 오른쪽
    dy = [0,-1,0,1]
    
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for d in range(4):  
                nx, ny, nd = x, y, d
                count = 0
        
                while True:
                    if visited[nx][ny][nd] != 0:
                        break

                    count += 1
                    visited[nx][ny][nd] = count

                    nx = (nx + dx[nd]) % len(grid)
                    ny = (ny + dy[nd]) % len(grid[0])

                    if grid[nx][ny] == 'R':
                        nd = (nd+1)%4
                    elif grid[nx][ny] == 'L':
                        nd = (nd-1)%4

                    if (nx, ny, nd) == (x, y, d):
                        answer.append(count)
                        break

    return sorted(answer)