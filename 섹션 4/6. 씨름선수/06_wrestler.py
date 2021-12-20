import sys
sys.stdin=open("in1.txt", "rt")

players_cnt = int(input())
players = []
for i in range(players_cnt):
    height, weight = map(int, input().split())
    players.append((height,weight))

players.sort(reverse=True)
max = 0
picked_player = 0
for i in players:
    if i[1] > max:
        picked_player +=1
        max = i[1]

print(picked_player)