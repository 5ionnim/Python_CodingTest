#11399 ATM 

num = int(input())
timeList = list(map(int, input().split()))
total = 0
finalTotal = 0

timeList.sort()
for i in timeList:
    total = total + i
    finalTotal = finalTotal + total
    
print(finalTotal)
