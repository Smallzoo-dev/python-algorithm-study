def solution(n, lost, reserve):
    answer = 0

    training_suit = [1] * n

    for i in lost:
        training_suit[i - 1] -= 1

    for i in reserve:
        training_suit[i - 1] += 1

    for i in range(len(training_suit)):
        if i == 0:
            if training_suit[i] >=1:
                answer += 1
                continue
            else:
                if training_suit[i + 1] >= 2:
                    answer += 1
                    training_suit[i + 1] -= 1
                    continue
        if i >= len(training_suit):
            if training_suit[i] >=1:
                answer += 1
                continue
            else:
                if training_suit[i - 1] >= 2:
                    answer += 1
                    training_suit[i - 1] -= 1
                    continue

        if training_suit[i] >= 1:
            answer += 1
            continue
        elif training_suit[i - 1] >= 2:
            answer += 1
            training_suit[i - 1] -= 1
            continue

        elif training_suit[i + 1] >= 2:
            answer += 1
            training_suit[i + 1] -= 1
            continue

    return answer


print(solution(3, [3], [1]))