input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    temp_array = []
    for i in string:
        if len(temp_array) == 0:
            temp_array.append(int(i))
        elif len(temp_array) != 0 and temp_array[-1] != int(i):
            temp_array.append(int(i))

    serial_zero_count = temp_array.count(0)
    serial_one_count = temp_array.count(1)

    return serial_one_count if serial_one_count <= serial_zero_count else serial_zero_count


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)