input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    result_value = 0
    for i in array:
        if result_value == 0:
            result_value += i
        else:
            if i <= 1:
                result_value += i
            else:
                result_value *= i
    return result_value



result = find_max_plus_or_multiply(input)
print(result)