from collections import defaultdict
def solution(genres, plays):
    answer = []
    genres_dict = defaultdict(int)
    for i in range(len(genres)):
        genres_dict[genres[i]]
        genres_dict[genres[i]] += plays[i]

    sorted_dict = sorted(genres_dict.keys(), key= lambda item: item[1], reverse=True)
    for i in sorted_dict:
        print(i)
        first = 0
        first_idx = 0
        second = 0
        second_idx = 0
        for idx in range(len(genres)):
            print(idx)
            if genres[idx] == i and plays[idx] > second:
                if plays[idx] > first:
                    second, second_idx = first, first_idx
                    first, first_idx = plays[idx], idx
                    continue
                second = plays[idx]
                second_idx = idx

        answer.append(first_idx)
        if second != 0:
            answer.append(second_idx)

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))