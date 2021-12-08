import sys
sys.stdin=open("in1.txt", "rt")

length, target = map(int, input().split())
num_arr = list(map(int, input().split()))
answer = []
print(num_arr)
for i in range(length):
    for j in range(i+1, length+1):

        if target == sum(num_arr[i:j]):
            print(i, j, num_arr[i:j])
            answer.append(num_arr[i:j])


