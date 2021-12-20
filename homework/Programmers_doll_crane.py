def solution(board, moves):
    answer = 0
    size = len(board)
    stack = []
    while moves:
        tmp = moves.pop(0) -1
        for i in range(size):
            if board[i][tmp] == 0:
                continue
            if not stack:
                stack.append(board[i][tmp])
                board[i][tmp] = 0
                break
            if board[i][tmp] == stack[-1]:
                stack.pop()
                board[i][tmp] = 0
                answer += 2
                break
            else:
                stack.append(board[i][tmp])
                board[i][tmp] = 0
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))