import sys
sys.stdin=open("in1.txt", "rt")
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e))

meeting.sort(key=lambda x : (x[1],x[0]))
et = 0
count = 0

for s, e in meeting:
    if s >= et:
        et = e
        count += 1

print(count)