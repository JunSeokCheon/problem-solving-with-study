def solution(x):
    answer = True
    str_x = str(x)
    x_num = 0
    
    for num in str_x:
        x_num += int(num)
    
    if x%x_num == 0:
        answer = True
    else:
        answer = False
    
    return answer