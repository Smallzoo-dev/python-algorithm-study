import sys
sys.stdin=open("in1.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in a:
    cnt += i
avg = round(sum(a)/n)
min = 101
for idx, x in enumerate(a):
    tmp = abs(x-avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res=idx

print(avg, res)