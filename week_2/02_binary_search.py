finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16]


def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    if len(array) <= 1 and array[0] != target:
        return False
    current = 0
    mid_value = len(array) // 2
    if(array[mid_value] == target):
        return True
    elif(array[mid_value] > target):
        array = array[0:mid_value]
        return is_existing_target_number_binary(target, array)
    else:
        array = array[mid_value:]
        return is_existing_target_number_binary(target, array)



result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)