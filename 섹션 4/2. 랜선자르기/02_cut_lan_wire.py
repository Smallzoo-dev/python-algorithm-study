import sys
sys.stdin=open("in1.txt", "rt")
k, n = map(int, input().split())
line = []
result = 0
largest = 0
def count(len, line):
    cnt = 0
    for x in line:
        cnt += (x//len)
    return cnt

for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest

while lt <= rt:
    mid=(lt+rt)//2

    if count(mid, line) >= n:
        result = mid
        lt = mid + 1

    else:
        rt = mid-1

print(result)

