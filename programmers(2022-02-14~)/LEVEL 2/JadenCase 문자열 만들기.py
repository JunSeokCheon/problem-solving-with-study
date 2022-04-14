def solution(s):
    s = s.lower()
    s = s.split(' ')
    s = [s[i].capitalize() for i in range(len(s))]
    return ' '.join(s)