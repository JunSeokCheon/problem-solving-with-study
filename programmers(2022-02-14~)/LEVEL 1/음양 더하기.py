def solution(absolutes, signs):
    answer = 0
    n_len = len(signs)
    for i in range(n_len):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
        
    return answer