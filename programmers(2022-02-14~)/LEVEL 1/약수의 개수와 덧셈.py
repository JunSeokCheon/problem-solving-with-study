def solution(left, right):
    answer = 0
    dic = {}
    
    for num in range(left, right+1):
        count = 0
        for i in range(1, int(num**0.5)+1):
            if num%i == 0:
                if i*i == num:
                    count += 1 
                else:
                    count += 2
        dic[num] = count
        
    for key, values in dic.items():
        if values%2 == 0:
            answer += key
        else:
            answer -= key

    return answer