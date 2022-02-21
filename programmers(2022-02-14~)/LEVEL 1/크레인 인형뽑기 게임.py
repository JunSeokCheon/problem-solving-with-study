# 0 0 0 0 0
# 0 0 1 0 3
# 0 2 5 0 1
# 4 2 4 4 2
# 3 5 1 3 1

# 1 5 3 5 1 2 1 4

# 0 0 0 4 3
# 0 0 2 2 5
# 0 1 5 4 1
# 0 0 0 4 3
# 0 3 1 2 1

# result 4 3 1 1 3 2 4
# stack 4 2 4
def solution(board, moves):
    answer = 0
    result = []
    stack = []
    new_board = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            new_board[i].append(board[j][i])
    
    for move in moves:
        for i in range(len(new_board[move-1])):
            if new_board[move-1][i] != 0:
                result.append(new_board[move-1][i])
                new_board[move-1][i] = 0            
                break
                
    stack.append(result[0])      
    for num in result[1:]:
        if len(stack) != 0 and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)
    
    answer = len(result)-len(stack)
    return answer