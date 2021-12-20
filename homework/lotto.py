from collections import deque
def solution(win_nums, lottos):
    answer = []

    win_nums.sort()
    win_nums = deque(win_nums)
    for i in range(len(win_nums)):
        if win_nums[0] != 0:
            break
        else:
            win_nums.popleft()
    count = 0
    for i in win_nums:
        if i in lottos:
            count += 1
    answer.append(7 - (count + (len(lottos) - len(win_nums))))
    answer.append(7 - count if count >= 1 else 6)

    return answer



print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))