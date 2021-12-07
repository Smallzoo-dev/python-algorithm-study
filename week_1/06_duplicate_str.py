input = "bbacabadea"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    alphabet_dic = {}
    for i in range(ord("a"), ord("z")):
        alphabet_dic[chr(i)] = 0

    for char in string:
        if char.isalpha() and alphabet_dic[char] == 0:
            alphabet_dic[char] += 1
        else:
            return char

    return "_"




result = find_not_repeating_character(input)
print(result)