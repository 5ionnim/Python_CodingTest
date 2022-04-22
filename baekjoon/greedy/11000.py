#11000 강의실 배정 
import sys
import heapq

lectureNum = int(sys.stdin.readline())
lectureList = []
resList = []

for i in range(lectureNum):
    lectureList.append(list(map(int, sys.stdin.readline().split())))

lectureList.sort(key = lambda x: (x[0], x[1]))

if(lectureNum > 0):
    heapq.heappush(resList, lectureList[0][1])
    del lectureList[0]

for lecture in lectureList:
    if (resList[0] <= lecture[0]): 
        heapq.heappop(resList)
        heapq.heappush(resList, lecture[1])
    else :
        heapq.heappush(resList, lecture[1])

print(len(resList))
    

        