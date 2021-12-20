def solution(numbers):
    answer = [i for i in range(10)]
    numbers.sort()
    for i in numbers:
        if i == 0:
            continue
        answer[i] = 0
    return sum(answer)


print(solution([1,2,3,4,6,7,8,0]))