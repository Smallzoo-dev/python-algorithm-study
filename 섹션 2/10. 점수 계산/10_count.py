import sys
sys.stdin=open("in3.txt", "rt")
n = int(input())
a = list(map(int, input().split()))

serial_counter = 0
total_point = 0
for i in range(0, n-1):
    if a[i] == 1:
        serial_counter += 1
    else:
        total_point += (serial_counter*(serial_counter+1)//2)
        serial_counter = 0
else:
    if serial_counter != 0:
        total_point += (serial_counter * (serial_counter + 1) // 2)

print(total_point)