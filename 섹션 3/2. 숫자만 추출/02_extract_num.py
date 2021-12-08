import sys
sys.stdin=open("in3.txt", "rt")

s=input()
res = 0
for char in s:
    if char.isdigit():
       res = res * 10 + int(char)
print(res)
for i in range(1, res + 1):
    if res % i == 0:
        print(i, end=" ")
