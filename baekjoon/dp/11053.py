#11053 가장 긴 증가하는 부분 수열
num = int(input())
initList = list(map(int, input().split()))
checkList = [0]*num
maxN = 0
def search(index):
    global initList, checkList, num
    if checkList[index] != 0:
        return checkList[index]
    else:
        checkList[index] = 1
        ret = [0]
        for i in range(index+1, num):
            if initList[index] < initList[i]:
                ret.append(search(i))
        checkList[index] += max(ret)
        return checkList[index]
for n in range(num):
    if checkList[n] == 0:
        maxN = max(maxN, search(n))
print(maxN)