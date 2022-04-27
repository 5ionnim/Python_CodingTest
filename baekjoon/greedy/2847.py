#2847 게임을 만든 동준이
levelNum = int(input())
initList = [int(input()) for _ in range(levelNum)]
initList.reverse()
stdNum = initList[0]
cnt = 0
for i in initList[1:]:
    a = i
    while stdNum <= a:
        a -= 1
        cnt += 1
    stdNum = a
print(cnt)
    
