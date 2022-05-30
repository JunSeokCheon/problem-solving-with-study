def solution(n):
    answer = []
    temp_list = [[0 for j in range(i+1)] for i in range(n)]
    
    num = 1
    i = -1
    j = 0
    
    for dire in range(n):
        for corr in range(dire, n):
            if dire % 3 == 0: # 밑 방향
                i += 1
            elif dire % 3 == 1: # 오른쪽 방향
                j += 1
            else: # 위쪽 대각선 방향
                i -= 1
                j -= 1
            temp_list[i][j] = num
            num += 1
    
    result = sum(temp_list, [])
    return result