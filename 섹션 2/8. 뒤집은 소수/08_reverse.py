import sys
sys.stdin=open("in1.txt", "rt")
n = int(input())
a=list(map(int, input().split()))

def reverse_num(number):
    result = 0
    while(number > 0):
        temp = number % 10
        result = result * 10 + temp
        number = number // 10
    return result

def is_prime(number):
    if number == 1:
        return False

    for i in range(2, number//2 +1):
        if number % i == 0:
            return False

    else:
        return True


for x in a:
    temp = reverse_num(x)
    if is_prime(temp):
        print(temp, end=" ")