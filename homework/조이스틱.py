from string import ascii_uppercase
def solution(name):
    answer = 0
    alpha_arr = [i for i in ascii_uppercase]
    alpha_num1 = [x for x in range(14)]
    alpha_num2 = [x for x in range(1,13)]
    alpha_num2.sort(reverse=True)
    alpha_num = alpha_num1 + alpha_num2
    alpha_dict = {name:value for name, value in zip(alpha_arr, alpha_num)}
    for char in name:
        answer += alpha_dict[char]
    
    return answer


solution("abc")