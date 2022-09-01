def solution(arr, divisor):
    answer = []
    
    for element in arr:
        if element % divisor == 0:
            answer.append(element)
    
    answer.sort()
    
    if len(answer) == 0:
        return [-1]
    else:
        return answer