import sys
sys.stdin=open("in1.txt", "rt")
n, m = map(int, input().split())
num_list = [0 for i in range(n + m + 3)]
max = -1
for i in range(1, n+1):
    for j in range(1, m+1):
        num_list[i+j] += 1
for i in range(n+m+1):
    if num_list[i] > max:
        max = num_list[i]
for i in range(n+m+1):
    if num_list[i] == max:
        print(i, end=' ')
