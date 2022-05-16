def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        temp_num = numbers[i]
        for j in range(i+1, len(numbers)):
            answer.append(temp_num + numbers[j])
    
    return sorted(list(set(answer)))