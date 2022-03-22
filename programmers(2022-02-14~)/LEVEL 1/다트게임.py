# 다트게임 - 문자열을 잘라서 숫사형태이면 값을 저장하고 문자라면 연산 후 list에 넣고, 값 초기화| # *, # 일 때는 리스트 인덱스 -1, -2 사용 | 중요한 점 - 10의 처리를 위해 int처리보다 str처리 |
def solution(dartResult):
    num = ''
    resultlist = []
  
    for i in dartResult:
        if i.isdigit():
            num += i
        else:
            if i == "S":
                num = int(num) ** 1
                resultlist.append(num)
                num = ''
            elif i == "D":
                num = int(num) ** 2
                resultlist.append(num)
                num = ''
            elif i == "T":
                num = int(num) ** 3
                resultlist.append(num)
                num = ''
            elif i == "*":
                if len(resultlist) > 1:
                    resultlist[-1] = resultlist[-1] * 2
                    resultlist[-2] = resultlist[-2] * 2
                else:
                    resultlist[-1] = resultlist[-1] * 2
            elif i == "#":
                resultlist[-1] = resultlist[-1] * (-1)
    return sum(resultlist)