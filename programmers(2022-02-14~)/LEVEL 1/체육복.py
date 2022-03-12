def solution(n, lost, reserve):
    answer = 0
    pure_reserve = set(reserve) - set(lost)
    pure_lost = set(lost) - set(reserve)

    for i in pure_reserve:
        left = i - 1
        right = i + 1
        
        if left in pure_lost:
            pure_lost.remove(left)
        elif right in pure_lost:
            pure_lost.remove(right)
    
    answer = n - len(pure_lost)
    
    return answer