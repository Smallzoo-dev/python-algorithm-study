input = "abcba"


def is_palindrome(string):
    if len(string) <= 1:
        return True
    str_arr = list(string)
    if str_arr.pop() == str_arr.pop(0):
        is_palindrome(''.join(str_arr))
    else:
        return False


print(is_palindrome(input))