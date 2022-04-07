# 상어 초등학교
n = int(input())

students = {}
for i in range(1,(n**2)+1):
    students[i]=0

input_students = [list(map(int,input().split())) for _ in range(n**2)]

for i in input_students:
    students[i[0]] = i[1:]

dr = [1,0,0,-1]
dc = [0,-1,1,0]

maps = [[0]*n for _ in range(n)]

def go(s):
    global maps,students,dr,dc,n
    max_friends =-1
    max_empty = -1
    cur_r=-1
    cur_c =-1
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            cur_empty=0
            cur_friends =0
            if(maps[i][j]==0):
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if(nr>=n or nc>=n or nc<0 or nr<0):
                        continue
                    if(maps[nr][nc]==0):
                        cur_empty+=1
                    elif(maps[nr][nc] in students[s]):
                        cur_friends+=1

                if(max_friends <= cur_friends):
                    if(max_friends ==cur_friends):
                        if(max_empty <= cur_empty):
                            cur_r = i
                            cur_c = j
                            max_friends = cur_friends
                            max_empty = cur_empty
                    else:
                        cur_r = i
                        cur_c = j
                        max_friends = cur_friends
                        max_empty = cur_empty

    return  cur_r,cur_c

for i in input_students:
    s_r,s_c = go(i[0])
    maps[s_r][s_c] = i[0]

ans =0
for i in range(n):
    for j in range(n):
        cur_num =0
        for k in range(4):
            nr = i+dr[k]
            nc = j+dc[k]
            if(nr<n and nc<n and nc>=0 and nr>=0):
                if(maps[nr][nc] in students[maps[i][j]]):
                    cur_num+=1
        if(cur_num==1):
            ans+=1
        elif(cur_num==2):
            ans+=10
        elif(cur_num==3):
            ans+=100
        elif(cur_num==4):
            ans+=1000
print(ans)