import math
def solution(m, musicinfos):
    answer = None
    m = str_convert(m)
    for i in musicinfos:
        start, end, title, melody = i.split(",")
        start = total_min(start)
        end = total_min(end)
        duration = end - start
        melody = str_convert(melody)

        melody *= math.ceil(duration/len(melody))
        melody = melody[:duration -1]

        print(start, end, duration, melody)
        if m not in melody:
            continue

        if answer == None:
            answer = (title, duration, start)
        elif duration > answer[1]:
            answer = (title, duration, start)
        elif start < answer[2]:
            answer = (title,duration, start)
    if answer:
        return answer[0]
    else:
        return "(None)"

def str_convert(music_str):
    result = music_str.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    return result

def total_min(time):
    total = 0
    hour, minute = map(int, time.split(":"))
    total += (hour*60)
    total += minute
    return total

print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

# import math
# from datetime import datetime, timedelta
# def solution(m, musicinfos):
#     music_infos_arr = []
#     for i in musicinfos:
#         music_infos_arr.append(i.split(","))
#
#     full_string_dict = get_full_string(music_infos_arr)
#     answer_arr = []
#     for key in full_string_dict:
#         if m in full_string_dict[key]:
#             answer_arr.append(str(key))
#         else:
#             continue
#     answer = which_is_answer(answer_arr, full_string_dict)
#     return answer
#
# def str_convert(music_str):
#     music_str.replace("C#", "c")
#     music_str.replace("D#", "d")
#     music_str.replace("F#", "f")
#     music_str.replace("G#", "g")
#     music_str.replace("A#", "a")
#     return music_str
#
#
# def time_between(start, end):
#     time_start = datetime.strptime(start, "%H:%M")
#     time_end = datetime.strptime(end, "%H:%M")
#     total_time = 0
#     split = str(time_end - time_start)[:-3].split(":")
#     total_time += (int(split[0]) * 60)
#     total_time += int(split[1])
#     return total_time
#
# def get_full_string(music_infos):
#     result_dict = {}
#     for music_arr in music_infos:
#         converted = str_convert(music_arr[3])
#         music_arr[3] = converted
#         total_time = time_between(music_arr[0], music_arr[1])
#         total_count = math.ceil(total_time / len(music_arr[3]))
#         full_string = music_arr[3] * total_count
#         full_string = full_string[:total_time]
#         result_dict[music_arr[2]] = full_string
#     return result_dict
#
#
# def which_is_answer(answer_arr, full_string_dict):
#     answer = ""
#     if len(answer_arr) == 0:
#         answer = "(None)"
#     elif len(answer_arr) == 1:
#         answer = answer_arr[0]
#     else:
#         max_counter = 0
#         max_answer = ""
#         for i in answer_arr:
#             if len(full_string_dict[i]) > max_counter:
#                 max_counter = len(full_string_dict[i])
#                 max_answer = i
#         answer = max_answer
#     return answer

