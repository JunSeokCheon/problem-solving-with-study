def solution(s):
    answer = ''
    result = []
    for i in s.split():
        result.append(int(i))
    
    answer = str(min(result)) + ' ' + str(max(result))
    return answer