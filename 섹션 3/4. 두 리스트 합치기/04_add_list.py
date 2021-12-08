import sys
sys.stdin=open("in3.txt", "rt")

max_arr_1 = int(input())
arr_1 = list(map(int, input().split()))
pointer_1 = 0
max_arr_2 = int(input())
arr_2 = list(map(int, input().split()))
pointer_2 = 0

result = []
while pointer_1 <= max_arr_1 - 1 and pointer_2 <= max_arr_2 - 1:
    if arr_1[pointer_1] <= arr_2[pointer_2]:
        result.append(arr_1[pointer_1])
        pointer_1 += 1
    else:
        result.append(arr_2[pointer_2])
        pointer_2 += 1
if pointer_1 == max_arr_1:
    result = result + arr_2[pointer_2 - 1:]
else:
    result = result + arr_1[pointer_1:]

print(result)
