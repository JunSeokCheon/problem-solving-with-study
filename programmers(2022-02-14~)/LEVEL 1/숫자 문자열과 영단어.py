def solution(s):
    answer = 0
    dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    for keys, values in dic.items():
        if keys in s:
            s = s.replace(keys, dic[keys])
    answer = int(s)
    return answer