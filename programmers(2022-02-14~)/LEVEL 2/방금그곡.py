import math

def solution(m, musicinfos):
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    answer = []
    
    for infos in musicinfos:
        start, end, name, info = infos.split(",")
        
        hour, minute = map(int, start.split(":"))
        start = hour * 60 + minute
        
        hour, minute = map(int, end.split(":"))
        end = hour * 60 + minute
        
        total_time = end - start
        
        info = info.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        info *= math.ceil(total_time / len(info))
        info = info[:total_time]
        
        if m in info:
            answer.append([total_time, name])
    
    if not answer:
        return "(None)"
    elif len(answer) == 1:
        return answer[0][1]
    else:
        answer = sorted(answer, key = lambda x : -x[0])
        return answer[0][1]