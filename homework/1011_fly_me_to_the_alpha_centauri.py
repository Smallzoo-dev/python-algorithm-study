import sys
import math
data = list(map(int,sys.stdin.readline().split()))
def get_left_year_by_max_speed(left_distance, max_speed):
    year_counter = 0
    current_left_distance = left_distance
    while max_speed >= 1:
        if max_speed > left_distance:
            max_speed -= 1
            continue
        elif current_left_distance % max_speed == 0:
            year_counter += (current_left_distance // max_speed)
            break
        else:
            year_counter += (current_left_distance // max_speed)
            current_left_distance = current_left_distance % max_speed
            max_speed -= 1

    return year_counter

def get_year_by_distance(distance):
    if(distance <= 3):
        return distance
    year_counter = 0
    max_speed = int(math.sqrt(distance))
    year_counter += 2 * max_speed - 1
    left_distance = distance - max_speed**2
    year_counter += get_left_year_by_max_speed(left_distance, max_speed)
    return year_counter

def solution(input_array):
    input_array.pop(0)
    distance_arr = []
    solution_arr = []
    for i in range(0, len(input_array) - 1, 2):
        distance_arr.append(input_array[i+1] - input_array[i])

    for distance in distance_arr:
        solution_arr.append(get_year_by_distance(distance))
    return solution_arr

result = solution(data)
for i in result:
    print(i)

