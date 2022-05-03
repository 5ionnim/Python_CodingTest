#14501 퇴사  
num = int(input())
initList = [list(map(int,input().split())) for _ in range(num)]
checkList = [0]*(num+1)
for n in range(num):
    for i in range(n+initList[n][0],num+1):
        checkList[i] = max(checkList[i], checkList[n]+initList[n][1])
print(max(checkList))