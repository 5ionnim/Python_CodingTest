#2812 시간초과 
num, delNum = map(int, input().split())
tNumList = list(map(int, list(input())))
bNum = 0
while True:
    if delNum == 0:
        break
    elif len(tNumList[bNum:]) == delNum:
        tNumList = tNumList[:bNum]
        break
    tList = tNumList[bNum:bNum + delNum + 1]
    maxN = max(tList)
    i = tList.index(maxN)
    if i == 0:
        bNum += 1
        continue
    else :
        for _ in range(i):
            del tNumList[bNum]
        bNum += 1
        delNum -= i
print("".join(list(map(str, tNumList))))
            