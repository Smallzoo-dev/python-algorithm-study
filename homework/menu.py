def solution(orders, course):
    answer = []
    orders_str = "".join(orders)
    for i in course:
        answer = answer + how_many_course(orders_str, i)
    return answer.sort()


def is_course(str_orders):
    min = ord(str_orders[0])
    for char in range(1,len(str_orders)):
        if ord(str_orders[char]) <= min:
            return False
    return True

def how_many_course(orders_str, length):
    max_course_count = 0
    max_course = ""
    left, right = 0, length
    while right <= len(orders_str):
        if is_course(orders_str[left:right]):
            course_count = orders_str[right:].count(orders_str[left:right])
            if course_count > max_course_count:
                max_course_count = course_count
                max_course = orders_str[left:right]
            elif course_count == max_course:
                max_course = max_course + " " + orders_str[left:right]
            left += 1
            right += 1
        else:
            left +=1
            right +=1
    print(max_course)
    print(max_course.split())
    return max_course.split()
solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))

