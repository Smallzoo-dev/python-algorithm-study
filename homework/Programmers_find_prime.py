def solution(numbers):
    numbers_arr = []
    for i in numbers:
        numbers_arr.append(int(i))
    print(numbers_arr)
    len_arr = len(numbers_arr)
    level = 0
    num = 0
    answer_arr=[]
    for i in set(numbers_arr):
        if is_prime(i):
            answer_arr.append(i)
    def dfs(level, num):
        nonlocal len_arr
        nonlocal numbers_arr
        nonlocal answer_arr
        if level == len_arr:
            if is_prime(num):
                answer_arr.append(num)
            return
        else:
            dfs(level + 1, num * 10 + numbers_arr[level])
            dfs(level + 1, num)

    dfs(level, num)
    return answer_arr


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


print(solution("011"))