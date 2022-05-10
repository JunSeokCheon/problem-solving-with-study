from collections import defaultdict
import math

def solution(fees, records):
    park_dic = {}
    total_dic = defaultdict(int)
    answer = []

    for record in records:
        Info = record.split()
        hour, minute = map(int, Info[0].split(":"))
        total_minute = hour*60 + minute
        
        if Info[1] in park_dic:
            total_dic[Info[1]] += total_minute - park_dic[Info[1]]
            del park_dic[Info[1]]
        else:
            park_dic[Info[1]] = total_minute
    
    end_time = 23*60 + 59
    for num, time in park_dic.items():
        total_dic[num] += (end_time - time)
    
    stand_time, stand_price, part_time, part_price = fees
    for num, time in total_dic.items():
        inital = stand_price
        if time > stand_time:
            inital += math.ceil((time-stand_time) / part_time) * part_price
        answer.append((num, inital))
    
    answer.sort()

    return [ans[1] for ans in answer]