def solution(seoul):
    answer = ''
    for i, kim in enumerate(seoul):
        if kim == "Kim":
            return f'김서방은 {i}에 있다'