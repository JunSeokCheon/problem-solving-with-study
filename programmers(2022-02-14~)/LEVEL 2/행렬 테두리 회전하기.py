def solution(rows, columns, queries):
    answer = []
    n_list = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    start = 1
    
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            n_list[i][j] = start
            start += 1

    for x1, y1, x2, y2 in queries:
        temp = n_list[x1][y1]
        min_num = temp
        
        for i in range(x1,x2):
            new = n_list[i+1][y1]
            n_list[i][y1] = new
            min_num = min(min_num, new)
        
        for i in range(y1, y2):
            new = n_list[x2][i+1]
            n_list[x2][i] = new
            min_num = min(min_num, new)
        
        for i in range(x2, x1, -1):
            new = n_list[i-1][y2]
            n_list[i][y2] = new
            min_num = min(min_num, new)
        
        for i in range(y2, y1, -1):
            new = n_list[x1][i-1]
            n_list[x1][i] = new
            min_num = min(min_num, new)
        
        n_list[x1][y1+1] = temp
        answer.append(min_num)
    
    return answer