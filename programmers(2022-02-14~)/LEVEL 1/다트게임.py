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