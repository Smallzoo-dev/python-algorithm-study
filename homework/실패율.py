def solution(N, stages):
    answer = []
    stage_player = [0]*(N+1)
    stages_fail = [0]*(N+1)
    for i in stages:
        for j in range(i):
            stage_player[j] += 1

    for i in stages:
        stages_fail[i-1] += 1
    return answer