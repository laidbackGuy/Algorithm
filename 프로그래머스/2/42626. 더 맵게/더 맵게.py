import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville:
        a = heapq.heappop(scoville)
        if a >= K:
            return answer
        if not scoville:
            return -1
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b*2)
        answer += 1
    return answer