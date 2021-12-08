import sys
sys.stdin=open("in1.txt", "rt")
board_size = int(input())
board = [list(map(int, input().split())) for _ in range(board_size)]

for i in board:
    i.insert(0, 0)
    i.append(0)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
board.insert(0, [0] * (board_size + 2))
board.append([0] * (board_size + 2))
mountain_count = 0
for i in range(1, board_size+1):
    for j in range(1, board_size+1):
        if all(board[i][j] > board[i + dx[k]][j + dy[k]] for k in range(4)):
            mountain_count += 1
        else:
            continue

print(mountain_count)
