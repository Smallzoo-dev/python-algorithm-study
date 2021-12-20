import sys
sys.stdin=open("in1.txt", "rt")

n, m = map(int, input().split())
track_list = list(map(int, input().split()))
maxx = max(track_list)

rt = sum(track_list)
lt = 1
result = 0

def count(volume):
    cnt = 1
    sum = 0
    for x in track_list:
        if sum + x > volume:
            cnt += 1
            sum = x
        else:
            sum += x

while (lt <= rt):
    mid = (lt + rt) // 2
    if mid >= maxx and count(mid) <= m:
        res = mid
        rt = mid -1

    else:
        lt = mid +1



