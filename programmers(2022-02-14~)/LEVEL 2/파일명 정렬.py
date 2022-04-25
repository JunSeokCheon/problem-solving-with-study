def solution(files):
    answer = []
    head = ''
    number = ''
    tail = ''
    
    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                break
        for j in range(len(number)):
            if not number[j].isdigit():
                tail = number[j:]  # tail, number 순서 주의 -> number가 먼저 올시 tail이 출력 안됨(number가 덮음)
                number = number[:j]
                break
        
        answer.append((head, number, tail))
        head = ''
        number = ''
        tail = ''
    
    result = sorted(answer, key = lambda x : (x[0].upper(), int(x[1])))
    temp = ["".join(i) for i in result]
    return temp