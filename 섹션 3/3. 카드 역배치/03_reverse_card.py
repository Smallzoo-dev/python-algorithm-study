import sys
sys.stdin=open("in3.txt", "rt")

card_list = [i + 1 for i in range(20)]
for i in range(10):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    while(start < end):
        card_list[start], card_list[end] = card_list[end], card_list[start]
        start += 1
        end -= 1
print(card_list)