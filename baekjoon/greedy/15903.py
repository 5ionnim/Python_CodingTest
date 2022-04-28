#15903 카드 합체 놀이
import heapq
cardNum, addNum = map(int, input().split())
heap = list(map(int, input().split()))
heapq.heapify(heap)
for i in range(addNum):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a+b)
    heapq.heappush(heap, a+b)
print(sum(heap))