def solution(N, stages):
    answer = []
    fail = {}
    len_stage = len(stages)
    
    # n = 8 , stages = 	[2, 1, 2, 6, 2, 4, 3, 3] -> 7/8스테이지 0 처리 (해주지 않으면 0으로 나누는 상황 발생)
    for i in range(1,N+1):
        if len_stage != 0:
            fail[i] = stages.count(i)/len_stage
            len_stage -= stages.count(i)
        else:
            fail[i] = 0
        
    sorted_fail = sorted(fail.items(), key = lambda x : (-x[1],x[0]))
    for i in sorted_fail:
        answer.append(i[0])
    return answer