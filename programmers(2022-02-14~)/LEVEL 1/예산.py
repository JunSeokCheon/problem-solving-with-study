def solution(d, budget):
    answer = 0
    d.sort()
    
    for money in d:
        budget -= money
        if budget < 0:
            break
        answer += 1
    
    return answer