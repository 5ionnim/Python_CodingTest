#2212 센서
import heapq
num = int(input())
ins = int(input())
insList = list(set(map(int, input().split())))
insList.sort()
cList = []
res = 0
for i in range(0, len(insList)-1):
    s = insList[i+1] - insList[i]
    heapq.heappush(cList, (-s, s))
if ins < num:
    for i in range(ins - 1):
        heapq.heappop(cList)
    for i in range(len(cList)):
        res += cList[i][1]
print(res)

