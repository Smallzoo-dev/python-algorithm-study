def solution(record):
    answer = []
    tmp = []
    id_nic = {}
    str_in = "님이 들어왔습니다."
    str_out = "님이 나갔습니다."
    for i in record:
        tmp.append(list(i.split()))
    for i in tmp:
        if i[0] == "Enter" or i[0] == "Change":
            id_nic[i[1]] = i[2]

    for i in tmp:
        if i[0] == "Enter":
            answer.append(id_nic[i[1]] + str_in)
        elif i[0] == "Leave":
            answer.append(id_nic[i[1]] + str_out)

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))