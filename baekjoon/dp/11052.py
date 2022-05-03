#11052 카드 구매하기
num = int(input())
initList = list(map(int, input().split()))
checkList = [0]*num
checkList[0] = initList[0]
def search(n):    
    global num, initList, checkList
    if checkList[n-1]!=0:  
        return checkList[n-1]
    else:
        maxN = 0
        for i in range(n//2): 
            maxN = max(maxN, search(i+1)+search(n-2-i+1))  
        checkList[n-1] = max(maxN, initList[n-1])
        return checkList[n-1]
print(search(num))
        