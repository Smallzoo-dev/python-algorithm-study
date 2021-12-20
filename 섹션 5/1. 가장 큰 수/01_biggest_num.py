import sys
sys.stdin=open("in1.txt", "rt")

numbers, count = map(int, input().split())

numbers_arr = list(map(int, str(numbers)))

answer_stack = []

for i in numbers_arr:
    while answer_stack and count > 0 and answer_stack[-1] < i:
        answer_stack.pop()
        count -= 1
    answer_stack.append(i)

if count != 0:
    answer_stack = answer_stack[:-count]

print(answer_stack)
