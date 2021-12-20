from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        stack = deque()
        compare = prices.popleft()
        for i in prices:
            if i >= compare:
                count += 1
            else:
                break
        answer.append(count)
    return answer