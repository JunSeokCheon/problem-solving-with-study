def solution(progresses, speeds):
    answer = []
    temp = []
    stand = 0
    
    for value, speed in zip(progresses, speeds):
        if (100-value)%speed == 0:
            temp.append((100-value)//speed)
        else:
            temp.append((100-value)//speed+1)
    
    for i in range(len(temp)):
        if temp[i] > temp[stand]:
            answer.append(i - stand)
            stand = i
    answer.append(len(temp) - stand)
    
    return answer