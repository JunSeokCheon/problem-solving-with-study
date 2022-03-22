# def solution(n, arr1, arr2):
#     answer = []
#     arr1_list = []
#     arr2_list = []
    
#     for i, num in enumerate(arr1):
#         ssap = []
#         while num != 0:
#             ssap.append(int(num%2))
#             num //= 2
#         while len(ssap) != n:
#             ssap.append(0)
#         ssap.reverse()
        
#         ssap_str = ''
#         for j in ssap:
#             if j == 0:
#                 ssap_str += " "
#             else:
#                 ssap_str += "#"
#         arr1_list.append(ssap_str)
#     print(arr1_list)
    
#     for i, num in enumerate(arr2):
#         ssap = []
#         while num != 0:
#             ssap.append(int(num%2))
#             num //= 2
#         while len(ssap) != n:
#             ssap.append(0)
#         ssap.reverse()
        
#         ssap_str = ''
#         for j in ssap:
#             if j == 0:
#                 ssap_str += " "
#             else:
#                 ssap_str += "#"
#         arr2_list.append(ssap_str)
#     print(arr2_list)

#     for i in range(n):
#         temp_str = ''
#         for j in range(n):
#             if arr1_list[i][j] == "#" or arr2_list[i][j] == "#":
#                 temp_str += "#"
#             else:
#                 temp_str += " "
#         print(temp_str)
#         answer.append(temp_str)

#     return answer

def solution(n, arr1, arr2):
    answer = []
    arr1_list = []
    arr2_list = []
    
    for num1, num2 in zip(arr1, arr2):
        result = num1|num2
        
        ssap = ''
        while result != 0:
            ssap += str(result%2)
            result //= 2
        while len(ssap) != n:
            ssap += str(0)
        ssap = ssap[::-1]
        ssap = ssap.replace("1", "#")
        ssap = ssap.replace("0", " ")
        answer.append(ssap)

    return answer