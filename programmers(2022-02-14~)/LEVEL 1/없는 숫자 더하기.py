def solution(numbers):
    answer = -1
    dic = [0,1,2,3,4,5,6,7,8,9]
    
    for num in numbers:
        if num in dic:
            dic.remove(num)
            
    answer = sum(dic)
    return answer