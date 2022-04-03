def solution(record):
    answer = []
    dic = {}
    for rec in record:
        com = rec.split()
        if com[0] == "Enter":
            dic[com[1]] = com[2]
        elif com[0] == "Change":
            dic[com[1]] = com[2]
    
    for rec in record:
        com = rec.split()
        if com[0] == "Enter":
            answer.append(f"{dic[com[1]]}님이 들어왔습니다.")  
        elif com[0] == "Leave":
            answer.append(f"{dic[com[1]]}님이 나갔습니다.")  
    return answer