#1715 카드 정렬하기 
import heapq

dackNum = int(input())
dacks = []
res = 0
for i in range(dackNum):
    heapq.heappush(dacks, int(input()))

while True:
    if (len(dacks) < 2):
        break
    elif (len(dacks) == 2):
        first = heapq.heappop(dacks)
        second = heapq.heappop(dacks)
        res += (first + second)
        break
    else :
        first = heapq.heappop(dacks)
        second = heapq.heappop(dacks)
        res += (first + second)
        heapq.heappush(dacks, first + second)
    
print(res)
            
    
