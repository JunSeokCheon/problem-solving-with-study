# 효율성 테스트 오류
# def solution(arr):
#     answer = []
#     idx_list = []

#     for i in range(len(arr)-1):
#         if arr[i] == arr[i+1]:
#             idx_list.append(i+1)
     
#     for i in sorted(idx_list, reverse=True):
#         arr.pop(i)
  
#     return arr

def solution(arr):
    answer = []
    
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
  
    return answer