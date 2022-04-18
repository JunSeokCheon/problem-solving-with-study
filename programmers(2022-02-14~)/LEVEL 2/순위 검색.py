# 공백and공백 파싱 후 반복문 돌면서 처리 -> 시간초과(효율성 x)
from itertools import combinations 
from collections import defaultdict 

def solution(info, query):
    answer = []
    people = defaultdict(list)
    
    # 지원자 정보 파싱
    for x in info:
        x = x.split()
        keylist = x[:-1]
        score=int(x[-1])
        
        # 점수 제외한 나머지 정보 combination으로 구하기
        for i in range(5):
            for c in combinations(keylist, i):
                key = ''.join(c)
                people[key].append(score)
    
    # 점수 정렬
    for key in people.keys():
        people[key].sort()
        
    # query 파싱
    for x in query:
        q = []
        x = x.split(' ')
        
        # and와 - 제거
        for y in x:
            if y!='and' and y!='-':
                q.append(y)
    
        key = ''.join(q[:-1])
        score = int(q[-1])
        
        # 이분탐색 사용하여 조건에 맞는 지원자 수 구하기
        count = 0
        
        if key in people.keys(): # 조건 확인
            value = people[key]
            start = 0
            end = len(value)

            while start <= end and start < len(value):
                mid = (start + end) // 2
                
                if value[mid] < score:
                    start = mid + 1
                else:
                    end = mid - 1
            count = len(value) - start

        answer.append(count)
    
    
    return answer