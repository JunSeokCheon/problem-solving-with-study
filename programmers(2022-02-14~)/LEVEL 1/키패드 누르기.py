def solution(numbers, hand):
    num_dic = {
        1:[0,0], 2:[0,1], 3:[0,2],
        4:[1,0], 5:[1,1], 6:[1,2],
        7:[2,0], 8:[2,1], 9:[2,2],
        "*":[3,0], 0:[3,1], "#":[3,2] 
    }
    answer = ''
    result = ''
    left = "*"
    right = "#"
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            result+="L"
            left = num
        elif num == 3 or num == 6 or num == 9:
            result+="R"
            right = num
        elif num == 2 or num == 5 or num == 8 or num == 0:
            left_1, left_2 = num_dic[left]
            right_1, right_2 = num_dic[right]
            num_1, num_2 = num_dic[num]
            
            left_value = abs(left_1-num_1) + abs(left_2-num_2)
            right_value = abs(right_1-num_1) + abs(right_2-num_2)
            
            if left_value > right_value:
                result+="R"
                right = num
            elif left_value < right_value:
                result+="L"
                left = num
            else:
                if hand == "right":
                    result+="R"
                    right = num
                elif hand == "left":
                    result+="L"
                    left = num
    answer = result
    return answer