import sys
# data = list(map(int,sys.stdin.readline().split()))
data = [5, 1, 6]
def solution(data):
    return (data[2] // data[0]-data[1]) + 1 if data[2] % (data[0] - data[1]) != 0 else (data[2] // data[0]-data[1])
print(solution(data))