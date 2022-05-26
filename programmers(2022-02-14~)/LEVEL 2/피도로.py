from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for permut in permutations(dungeons, len(dungeons)):
        piro = k
        count = 0
        for per in permut:
            if piro >= per[0]:
                piro -= per[1]
                count += 1
        
        if count > answer:
            answer = count
    
    return answer