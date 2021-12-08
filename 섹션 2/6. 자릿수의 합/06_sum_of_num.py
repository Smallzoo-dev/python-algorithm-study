import sys
sys.stdin=open("in1.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
max = -1
max_num = 0
def parse_sum_number(number):
    count = 0
    while(number > 0):
        count += number % 10
        number = number // 10
    return count
for i in a:
    if parse_sum_number(i) > max:
        max = parse_sum_number(i)
        max_num = i

print(max_num)
