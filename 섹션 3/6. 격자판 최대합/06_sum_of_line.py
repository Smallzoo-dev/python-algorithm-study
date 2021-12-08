import sys
sys.stdin=open("in1.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
max = -1
for i in range(n):
    sum1 = sum2 = sum3 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]

    if sum1 > max:
        max = sum1

    if sum2 > max:
        max = sum2


sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]

if sum1 > max:
    max = sum1

if sum2 > max:
    max = sum2


print(max)