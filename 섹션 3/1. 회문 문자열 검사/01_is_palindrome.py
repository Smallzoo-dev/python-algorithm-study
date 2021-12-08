import sys
sys.stdin=open("in3.txt", "rt")

n = int(input())
for i in range(n):
    s = input().upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d No" %(i+1))
            break
    else:
        print("#%d Yes" %(i+1))
