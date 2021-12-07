input = 20

def is_prime_num(num):
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    result = []
    for i in range(2, number):
        if is_prime_num(i):
            result.append(i)
    return result




result = find_prime_list_under_number(input)
print(result)