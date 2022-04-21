#5585 거스름돈 
changes = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
changesNum = 0
for c in coins:
    cNum = changes//c
    changes -= (c * cNum)
    changesNum += cNum
    
print(changesNum)
    
