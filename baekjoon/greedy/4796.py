#4796 캠핑 배정 
outputList = []
while True:
    li = list(map(int, input().split()))
    if (sum(li)==0):
        break
    quotient = li[2]//li[1]
    remainder = li[2]%li[1]
    s = quotient * li[0] + min([remainder, li[0]])
    outputList.append(s)

for outputNum in range(len(outputList)):
    print("Case "+str(outputNum+1)+": "+str(outputList[outputNum]))
