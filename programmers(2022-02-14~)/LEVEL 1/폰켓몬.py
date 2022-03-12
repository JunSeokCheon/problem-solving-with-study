def solution(nums):
    answer = 0
    dic = {}
    n = len(nums)//2
    result = 0
    
    for i in set(nums):
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for key, values in dic.items():
        result += values
    
    if result >= n:
        answer = n
    else:
        answer = result
        
    return answer