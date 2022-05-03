#1937 욕심쟁이 판다
import sys
sys.setrecursionlimit(10**5)
num = int(input())
initList = [list(map(int, input().split())) for _ in range(num)]
checkList = [[0]*num for _ in range(num)]
fVList = [[-1, 0], [0, 1], [1, 0], [0, -1]]
res = 0
def search(s):
    global num, initList, checkList, fVList
    if checkList[s[0]][s[1]]!=0:
        return checkList[s[0]][s[1]]
    else:
        maxN = 0
        for v in fVList:
            ar = s[0]+v[0]
            ac = s[1]+v[1]
            if 0<=ar<num and 0<=ac<num and initList[s[0]][s[1]]<initList[ar][ac]:
                maxN = max(maxN, search([ar,ac]))
        checkList[s[0]][s[1]] = 1+maxN
        return 1+maxN
for r in range(num):
    for c in range(num):
        res = max(res, search([r,c]))
print(res)