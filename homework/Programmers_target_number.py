def solution(numbers, target):
    answer = 0
    total = sum(numbers)

    def dfs(level, numbers, is_positive):
        nonlocal target
        nonlocal answer
        if level == len(numbers):
            return
        elif sum(numbers[:level]) - sum(numbers[level + 1:]) > target:
            return
        elif sum(numbers[:level]) + sum(numbers[level + 1:]) < target:
            return
        else:
            numbers[level] = numbers[level] * is_positive
            if sum(numbers) == target:
                answer += 1
            dfs(level + 1, numbers, 1)
            dfs(level + 1, numbers, -1)

    dfs(0, numbers, 1)
    dfs(0, numbers, -1)
    return answer


print(solution([1,1,1,1,1], 3))