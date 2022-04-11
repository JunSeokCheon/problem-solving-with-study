def solution(priorities, location):
    answer = 0
    
    priorities_index = list(range(len(priorities)))
    priorities_index[location] = "answer"
    
    while True:
        if priorities[0] == max(priorities):
            answer += 1
            
            if priorities_index[0] == "answer":
                print(answer)
                break
            else:
                priorities.pop(0)
                priorities_index.pop(0)
        else:
            priorities.append(priorities.pop(0))
            priorities_index.append(priorities_index.pop(0))
    return answer