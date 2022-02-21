def solution(lottos, win_nums):
    answer = []
    dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    one_count = lottos.count(0)
    lottos_count = 0
    for i in lottos:
        if i in win_nums:
            lottos_count+=1
    
    min_count = lottos_count
    max_count = lottos_count + one_count
    answer.append(dic[max_count])
    answer.append(dic[min_count])
    return answer