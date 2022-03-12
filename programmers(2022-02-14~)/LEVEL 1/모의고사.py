def solution(answers):
    answer = []
    first = [1,2,3,4,5] 
    second = [2,1,2,3,2,4,2,5] 
    third = [3,3,1,1,2,2,4,4,5,5] 
    count = [0,0,0]
    
    for i, num in enumerate(answers):
        if num == first[i%len(first)]:
            count[0] += 1
        if num == second[i%len(second)]:
            count[1] += 1
        if num == third[i%len(third)]:
            count[2] += 1

    for i, value in enumerate(count):
        if max(count) == value:
            answer.append(i+1)
    return answer