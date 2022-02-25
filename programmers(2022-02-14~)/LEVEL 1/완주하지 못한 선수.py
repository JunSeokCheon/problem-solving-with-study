def solution(participant, completion):
    dic = {}
    
    for part in participant:
        if part not in dic:
            dic[part] = 1
        else:
            dic[part] += 1
            
    for com in completion:
        if com in dic:
            dic[com] -= 1
    
    for keys, values in dic.items():
        if values == 1:
            return keys