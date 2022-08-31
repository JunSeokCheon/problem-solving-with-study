def solution(s):
    answer = ''
    for words in s.split(' '):
        for i, word in enumerate(words):
            if i % 2 == 0:
                answer += word.upper()
            else:
                answer += word.lower()
        answer += ' '
    
    return answer[:-1]