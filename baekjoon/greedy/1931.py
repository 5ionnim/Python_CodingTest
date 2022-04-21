#1931 회의실 배정 

conTotal = int(input())
conferences = []
lastNum = 0
maxNum = 0

for c in range(conTotal):
    conferences.append(list(map(int, input().split())))

conferences.sort(key = lambda x: (x[1], x[0]))

for con in conferences:
    if con[0] >= lastNum:
        maxNum += 1
        lastNum = con[1]
print(maxNum)