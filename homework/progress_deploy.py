def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    while len(progresses) > 0:
        count = 0
        for i in range(0,len(progresses) -1):
            tmp2 = progresses[i]
            progresses[i] = speeds[i] + tmp2
        if progresses[-1] >= 100:
            while True:
                print("loop here")
                progresses.pop()
                speeds.pop()
                count += 1
                if progresses[-1] < 100:
                    break
        answer.append(count)



    return answer

print(solution(	[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))