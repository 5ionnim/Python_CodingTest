#1541 잃어버린 괄호 
numStr = input().split('-')
maxNums = 0
maxNumsI = 0
for i in range(1,len(numStr)):
    nums = sum(list(map(int, numStr[i].split('+'))))
    if (maxNums < nums):
        maxNums = nums
        maxNumsI = i
if (maxNums != 0):
    numStr[maxNumsI] = str(maxNums)
total = sum(list(map(int, numStr[0].split('+'))))
for i in range(1,len(numStr)):
    total -= sum(list(map(int, numStr[i].split('+'))))

print(total)