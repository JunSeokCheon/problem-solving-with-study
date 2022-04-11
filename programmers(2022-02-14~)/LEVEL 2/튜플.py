def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s = sorted(s, key = lambda x : len(x))
    
    for i in s:
        for j in i.split(","):
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer