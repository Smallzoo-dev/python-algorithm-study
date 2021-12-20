import sys
sys.stdin=open("in1.txt", "rt")
board = [list(map(int, input().split())) for _ in range(9)]
dx = [-1, 0, 1, 0, -1, +1, -1, +1]
dy = [0, 1, 0, -1, -1, +1, +1, -1]

result = True
for i in range(1, 9, 3):
    for j in range(1, 9, 3):
        if all(board[i][j] != board[i + dx[k]][j + dy[k]] for k in range(8)):
            continue
        else:
            result = False
            break

for i in board:
    if len(i) != len(set(i)) or sum(i) != 45:
        result = False

for i in range(9):
    temp_board = []
    for j in range(9):
        temp_board.append(board[j][i])
    if len(temp_board) != len(set(temp_board)) or sum(temp_board) != 45:
        result = False


print("YES" if result == True else "NO")