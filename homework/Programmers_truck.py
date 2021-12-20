from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque(maxlen=bridge_length)
    trucks = deque(truck_weights)
    while len(trucks) > 0:
        next_truck = trucks.popleft()
        if sum(bridge) + next_truck <= weight:
            bridge.append(next_truck)
        else:
            answer += bridge_length
            answer += (len(bridge)-1)
            bridge.clear()
            bridge.append(next_truck)

    return answer


print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))