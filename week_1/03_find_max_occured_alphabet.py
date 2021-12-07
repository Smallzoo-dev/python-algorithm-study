input = "hello my name is sparta bbbbbbbbbbbbbbbbbbbbbbbbbbbb"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    # 이 부분을 채워보세요!
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    max_occurence = 0
    max_index = 0
    for i in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[i] > max_occurence:
            max_occurence = alphabet_occurrence_array[i]
            max_index = i
    max_index += ord("a")

    return chr(max_index)


result = find_max_occurred_alphabet(input)
print(result)